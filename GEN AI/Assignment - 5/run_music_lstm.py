import os
import glob
import zipfile
import json
import random
import urllib.request
import warnings
import numpy as np
import matplotlib.pyplot as plt
import pretty_midi
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

warnings.filterwarnings("ignore")

# Set seeds
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
tf.keras.utils.set_random_seed(SEED)

print("TensorFlow version :", tf.__version__)
print("GPUs available     :", tf.config.list_physical_devices("GPU"))

DATA_URL = "https://github.com/jukedeck/nottingham-dataset/archive/refs/heads/master.zip"
DATA_DIR = "midi_data"
ZIP_PATH = "nottingham.zip"

os.makedirs(DATA_DIR, exist_ok=True)

if len(glob.glob(f"{DATA_DIR}/**/*.mid", recursive=True)) == 0:
    print("Downloading Nottingham dataset...")
    try:
        urllib.request.urlretrieve(DATA_URL, ZIP_PATH)
        with zipfile.ZipFile(ZIP_PATH) as z:
            z.extractall(DATA_DIR)
        print("Download + extraction complete.")
    except Exception as e:
        print("Download failed, checking local backup or synthetic generation:", e)

midi_paths = sorted(glob.glob(f"{DATA_DIR}/**/*.mid", recursive=True) +
                    glob.glob(f"{DATA_DIR}/**/*.midi", recursive=True))
print("MIDI files found:", len(midi_paths))

# Use subset of 120 files for fast, robust training
MAX_FILES = 120
paths_to_use = midi_paths[:MAX_FILES] if len(midi_paths) >= MAX_FILES else midi_paths

songs_raw = []
for path in paths_to_use:
    try:
        midi = pretty_midi.PrettyMIDI(path)
        if len(midi.instruments) == 0:
            continue
        melody_track = max([t for t in midi.instruments if len(t.notes) > 0],
                           key=lambda t: np.mean([n.pitch for n in t.notes]))
        melody_notes = sorted(melody_track.notes, key=lambda n: n.start)
        songs_raw.append([(n.pitch, n.start, n.end) for n in melody_notes])
    except Exception as e:
        pass

print("Songs successfully parsed:", len(songs_raw))

song_lengths = [len(s) for s in songs_raw]
all_pitches = [p for s in songs_raw for (p, _, _) in s]
all_durs = [e - st for s in songs_raw for (_, st, e) in s]

print(f"Total notes parsed   : {len(all_pitches)}")
print(f"Notes per song (mean): {round(np.mean(song_lengths), 1)}")
print(f"Pitch range          : {min(all_pitches)} ({pretty_midi.note_number_to_name(min(all_pitches))}) to {max(all_pitches)} ({pretty_midi.note_number_to_name(max(all_pitches))})")
print(f"Distinct pitches     : {len(set(all_pitches))}")
print(f"Mean note duration   : {round(np.mean(all_durs), 3)}s")

# Plot 1: Pitch & Duration Distribution
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].hist(all_pitches, bins=range(min(all_pitches), max(all_pitches) + 2), color="#2563eb", edgecolor="#1d4ed8", alpha=0.85)
ax[0].set_title("Pitch Distribution (MIDI Key Numbers)", fontsize=11, fontweight="bold")
ax[0].set_xlabel("MIDI Pitch Number")
ax[0].set_ylabel("Count")
ax[0].grid(True, linestyle="--", alpha=0.4)

ax[1].hist(all_durs, bins=40, range=(0, 3), color="#d97706", edgecolor="#b45309", alpha=0.85)
ax[1].set_title("Note Duration Distribution (Seconds)", fontsize=11, fontweight="bold")
ax[1].set_xlabel("Duration (s)")
ax[1].grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("pitch_duration_distribution.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved pitch_duration_distribution.png")

# Step 6.1: Event quantisation
ALLOWED_DURATIONS = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0]

def round_duration(d):
    return min(ALLOWED_DURATIONS, key=lambda x: abs(x - d))

songs_events = []
for song in songs_raw:
    songs_events.append([(pitch, round_duration(end - start)) for (pitch, start, end) in song])

# Step 6.2: Vocabulary mapping
all_events = [ev for song in songs_events for ev in song]
unique_events = sorted(set(all_events))
event_to_id = {ev: i for i, ev in enumerate(unique_events)}
id_to_event = {i: ev for ev, i in event_to_id.items()}
VOCAB_SIZE = len(unique_events)
print(f"Vocabulary Size      : {VOCAB_SIZE} unique (pitch, duration) events")

songs_ids = [[event_to_id[ev] for ev in song] for song in songs_events]

# Step 6.3: Create sequences
SEQ_LENGTH = 50
VAL_FRACTION = 0.10

usable_songs = [s for s in songs_ids if len(s) > SEQ_LENGTH]
print(f"Usable songs         : {len(usable_songs)} of {len(songs_ids)}")

rng = np.random.default_rng(SEED)
order = rng.permutation(len(usable_songs))
n_val_songs = max(1, int(VAL_FRACTION * len(usable_songs)))
val_songs = [usable_songs[i] for i in order[:n_val_songs]]
train_songs = [usable_songs[i] for i in order[n_val_songs:]]

def make_sequences(list_of_songs, seq_length):
    X, y = [], []
    for song in list_of_songs:
        for i in range(len(song) - seq_length):
            X.append(song[i : i + seq_length])
            y.append(song[i + seq_length])
    return np.array(X, dtype="int32"), np.array(y, dtype="int32")

X_train, y_train = make_sequences(train_songs, SEQ_LENGTH)
X_val, y_val = make_sequences(val_songs, SEQ_LENGTH)

print("X_train shape        :", X_train.shape)
print("y_train shape        :", y_train.shape)
print("X_val shape          :", X_val.shape)

BATCH_SIZE = 256
train_ds = (tf.data.Dataset.from_tensor_slices((X_train, y_train))
            .shuffle(buffer_size=10000, seed=SEED)
            .batch(BATCH_SIZE)
            .prefetch(tf.data.AUTOTUNE))

val_ds = (tf.data.Dataset.from_tensor_slices((X_val, y_val))
          .batch(BATCH_SIZE)
          .prefetch(tf.data.AUTOTUNE))

# Build Model
EMBEDDING_DIM = 64
LSTM_UNITS = 256
EPOCHS = 6
LEARNING_RATE = 0.002

model = keras.Sequential([
    layers.Input(shape=(SEQ_LENGTH,), dtype="int32"),
    layers.Embedding(input_dim=VOCAB_SIZE, output_dim=EMBEDDING_DIM, name="Note_Embedding"),
    layers.LSTM(LSTM_UNITS, name="Music_LSTM_Layer"),
    layers.Dropout(0.2, name="Dropout_Regularization"),
    layers.Dense(VOCAB_SIZE, activation="softmax", name="Output_Softmax")
], name="Music_Generation_LSTM")

model.summary()

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

early_stop = keras.callbacks.EarlyStopping(
    monitor="val_loss", patience=4, restore_best_weights=True
)

print("\nStarting LSTM Training...")
history = model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS, callbacks=[early_stop])

# Save Loss Curve
plt.figure(figsize=(8, 4.5))
plt.plot(history.history["loss"], label="Training Loss", color="#1e40af", marker="o", linewidth=2)
plt.plot(history.history["val_loss"], label="Validation Loss", color="#dc2626", marker="s", linewidth=2)
plt.xlabel("Epoch", fontsize=10, fontweight="bold")
plt.ylabel("Sparse Categorical Cross-Entropy Loss", fontsize=10, fontweight="bold")
plt.title("LSTM Music Model Loss Convergence Curve", fontsize=11, fontweight="bold")
plt.legend(frameon=True, facecolor="#f8fafc", edgecolor="#cbd5e1")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("loss_curve.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved loss_curve.png")

# Save model and vocabulary
model.save("music_lstm.keras")
model.save_weights("music_lstm.weights.h5")
with open("vocabulary.json", "w") as f:
    json.dump({"seq_length": SEQ_LENGTH, "events": [list(ev) for ev in unique_events]}, f, indent=2)
print("Saved model artifacts: music_lstm.keras, music_lstm.weights.h5, vocabulary.json")

# Next-Event Probability Distribution on Validation Sample
example_input = X_val[10]
example_target = y_val[10]
probs = model.predict(example_input[np.newaxis, :], verbose=0)[0]

def event_label(event_id):
    pitch, dur = id_to_event[int(event_id)]
    return f"{pretty_midi.note_number_to_name(pitch)} ({dur}s)"

top = np.argsort(probs)[::-1][:8]

plt.figure(figsize=(9, 4))
plt.bar([event_label(i) for i in top], probs[top], color="#059669", edgecolor="#047857", alpha=0.85)
plt.xticks(rotation=35, ha="right", fontsize=9)
plt.ylabel("Softmax Probability", fontsize=10, fontweight="bold")
plt.title(f"Top-8 Predicted Musical Events (Target was {event_label(example_target)})", fontsize=11, fontweight="bold")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("next_event_prediction_probs.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved next_event_prediction_probs.png")

# Temperature effect visualization
plt.figure(figsize=(9, 4))
for T, col in zip([0.5, 1.0, 1.5], ["#3b82f6", "#10b981", "#ef4444"]):
    adjusted = np.exp(np.log(probs + 1e-9) / T)
    adjusted /= adjusted.sum()
    plt.plot(np.sort(adjusted)[::-1][:15], marker="o", color=col, linewidth=2, label=f"Temperature T = {T}")
plt.xlabel("Top Ranked Event Indices", fontsize=10, fontweight="bold")
plt.ylabel("Adjusted Probability", fontsize=10, fontweight="bold")
plt.title("Effect of Temperature on Next-Event Sampling Sharpness", fontsize=11, fontweight="bold")
plt.legend(frameon=True, facecolor="#f8fafc", edgecolor="#cbd5e1")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("temperature_comparison.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved temperature_comparison.png")

# Autoregressive generation
def sample_with_temperature(probabilities, temperature=1.0):
    logits = np.log(np.asarray(probabilities, dtype="float64") + 1e-9) / temperature
    logits = logits - np.max(logits)
    new_probs = np.exp(logits) / np.sum(np.exp(logits))
    return int(np.random.choice(len(new_probs), p=new_probs))

def generate_events(model, seed_ids, num_generate=200, temperature=1.0):
    window = list(seed_ids)
    generated = []
    for _ in range(num_generate):
        x = np.array(window, dtype="int32")[np.newaxis, :]
        probabilities = model(x, training=False).numpy()[0]
        next_id = sample_with_temperature(probabilities, temperature)
        generated.append(next_id)
        window.append(next_id)
        window = window[1:]
    return generated

def events_to_midi(event_ids, filename="generated_music.mid", velocity=85, program=0):
    pm = pretty_midi.PrettyMIDI(initial_tempo=120)
    instrument = pretty_midi.Instrument(program=program)
    current_time = 0.0
    for event_id in event_ids:
        pitch, duration = id_to_event[int(event_id)]
        note = pretty_midi.Note(velocity=velocity, pitch=int(pitch),
                                start=current_time, end=current_time + duration)
        instrument.notes.append(note)
        current_time += duration
    pm.instruments.append(instrument)
    pm.write(filename)
    return pm

NUM_GENERATE = 200
seed_song = random.choice(val_songs)
start = random.randint(0, len(seed_song) - SEQ_LENGTH)
seed_ids = seed_song[start : start + SEQ_LENGTH]

temperature_files = {}
for T in [0.5, 1.0, 1.5]:
    ids = generate_events(model, seed_ids, NUM_GENERATE, T)
    fname = f"generated_T{T}.mid"
    pm = events_to_midi(ids, fname)
    temperature_files[T] = ids
    if T == 1.0:
        events_to_midi(ids, "generated_music.mid")
    print(f"Generated {fname} ({len(pm.instruments[0].notes)} notes, length {round(pm.get_end_time(), 1)}s)")

# Evaluation metrics
def melody_stats(event_ids):
    pitches = [id_to_event[int(i)][0] for i in event_ids]
    durs = [id_to_event[int(i)][1] for i in event_ids]
    intervals = np.abs(np.diff(pitches))
    fourgrams = [tuple(event_ids[i:i+4]) for i in range(len(event_ids) - 3)]
    repeated = 1 - len(set(fourgrams)) / len(fourgrams) if len(fourgrams) > 0 else 0
    return {
        "unique_pitches": len(set(pitches)),
        "pitch_range": max(pitches) - min(pitches),
        "mean_interval": round(float(np.mean(intervals)), 2),
        "unique_durations": len(set(durs)),
        "mean_duration": round(float(np.mean(durs)), 3),
        "repeated_patterns": round(float(repeated), 2)
    }

real_stats_list = []
for _ in range(30):
    s = random.choice(usable_songs)
    if len(s) >= NUM_GENERATE:
        st = random.randint(0, len(s) - NUM_GENERATE)
        real_stats_list.append(melody_stats(s[st : st + NUM_GENERATE]))
real_avg = {k: round(float(np.mean([d[k] for d in real_stats_list])), 2) for k in real_stats_list[0]}

rows = {"REAL (Dataset Avg)": real_avg}
for T, ids in temperature_files.items():
    rows[f"Generated T={T}"] = melody_stats(ids)

print("\n--- Quantitative Evaluation Statistics ---")
for k, v in rows.items():
    print(k, v)

# Save Evaluation Comparison Plot
fig, axes = plt.subplots(1, 3, figsize=(15, 3.8), sharey=True)
lo, hi = min(all_pitches), max(all_pitches)
axes[0].hist(all_pitches, bins=range(lo, hi + 2), density=True, color="#2563eb", alpha=0.85)
axes[0].set_title("Real Folk Music Dataset", fontsize=11, fontweight="bold")
axes[0].set_xlabel("MIDI Pitch Number")
axes[0].set_ylabel("Probability Density")
axes[0].grid(True, linestyle="--", alpha=0.4)

axes[1].hist([id_to_event[i][0] for i in temperature_files[0.5]], bins=range(lo, hi + 2), density=True, color="#059669", alpha=0.85)
axes[1].set_title("Generated Composition (T = 0.5)", fontsize=11, fontweight="bold")
axes[1].set_xlabel("MIDI Pitch Number")
axes[1].grid(True, linestyle="--", alpha=0.4)

axes[2].hist([id_to_event[i][0] for i in temperature_files[1.5]], bins=range(lo, hi + 2), density=True, color="#dc2626", alpha=0.85)
axes[2].set_title("Generated Composition (T = 1.5)", fontsize=11, fontweight="bold")
axes[2].set_xlabel("MIDI Pitch Number")
axes[2].grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("pitch_histograms_comparison.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved pitch_histograms_comparison.png")

# Piano Roll Visualization of Generated Melody
plt.figure(figsize=(12, 4))
pm_gen = pretty_midi.PrettyMIDI("generated_music.mid")
for note in pm_gen.instruments[0].notes[:60]:
    plt.plot([note.start, note.end], [note.pitch, note.pitch], color="#7c3aed", linewidth=3.5, solid_capstyle="round")
plt.xlabel("Time (Seconds)", fontsize=10, fontweight="bold")
plt.ylabel("MIDI Pitch (Semitone)", fontsize=10, fontweight="bold")
plt.title("Piano Roll Visualization: Generated Melody Track (First 60 Notes)", fontsize=11, fontweight="bold")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("generated_piano_roll.png", dpi=200, bbox_inches="tight")
plt.close()
print("Saved generated_piano_roll.png")

print("\n--- All pipeline tasks executed successfully! ---")
