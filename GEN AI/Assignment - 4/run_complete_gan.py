import os
import sys
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers

print("TensorFlow Version:", tf.__version__, flush=True)
np.random.seed(42)
tf.random.set_seed(42)

target_dir = r"C:\Users\adity\Desktop\Subjects\GEN AI\Assignment - 4"

# 1. Load MNIST Dataset
(x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32')
# Normalize to [-1, 1] range for Tanh activation
x_train = (x_train - 127.5) / 127.5
print(f"Dataset successfully prepared: {x_train.shape} samples in range [{x_train.min()}, {x_train.max()}]", flush=True)

# Save Real Samples
fig, axes = plt.subplots(4, 4, figsize=(6, 6))
for i, ax in enumerate(axes.flatten()):
    img = (x_train[i, :, :, 0] + 1.0) / 2.0
    ax.imshow(img, cmap='gray')
    ax.axis('off')
plt.suptitle("Real MNIST Dataset Samples (Ground Truth)", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(target_dir, "real_mnist_samples.png"), dpi=200)
plt.close()
print("Saved real_mnist_samples.png", flush=True)

# 2. Generator Architecture
def make_generator_model():
    model = tf.keras.Sequential(name="DCGAN_Generator")
    model.add(layers.Input(shape=(100,)))
    model.add(layers.Dense(7 * 7 * 128, use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(negative_slope=0.2))
    model.add(layers.Reshape((7, 7, 128)))
    
    # Upsample to 14x14
    model.add(layers.Conv2DTranspose(64, (4, 4), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(negative_slope=0.2))
    
    # Upsample to 28x28
    model.add(layers.Conv2DTranspose(1, (4, 4), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
    return model

# 3. Discriminator Architecture
def make_discriminator_model():
    model = tf.keras.Sequential(name="DCGAN_Discriminator")
    model.add(layers.Input(shape=(28, 28, 1)))
    
    # Downsample to 14x14
    model.add(layers.Conv2D(64, (4, 4), strides=(2, 2), padding='same'))
    model.add(layers.LeakyReLU(negative_slope=0.2))
    model.add(layers.Dropout(0.3))
    
    # Downsample to 7x7
    model.add(layers.Conv2D(128, (4, 4), strides=(2, 2), padding='same'))
    model.add(layers.LeakyReLU(negative_slope=0.2))
    model.add(layers.Dropout(0.3))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(1)) # Logit output
    return model

generator = make_generator_model()
discriminator = make_discriminator_model()

print("\n--- GENERATOR SUMMARY ---", flush=True)
generator.summary()
print("\n--- DISCRIMINATOR SUMMARY ---", flush=True)
discriminator.summary()

# 4. Losses & Optimizers
cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)

def discriminator_loss(real_output, fake_output):
    # One-sided label smoothing for real images (0.9 instead of 1.0)
    real_loss = cross_entropy(tf.ones_like(real_output) * 0.9, real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    return real_loss + fake_loss

def generator_loss(fake_output):
    return cross_entropy(tf.ones_like(fake_output), fake_output)

generator_optimizer = tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5)
discriminator_optimizer = tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5)

# Fixed seed for tracking progression
fixed_seed = tf.random.normal([16, 100], seed=42)

def save_generated_images(model, epoch, label=""):
    predictions = model(fixed_seed, training=False)
    fig, axes = plt.subplots(4, 4, figsize=(6, 6))
    for i in range(predictions.shape[0]):
        img = (predictions[i, :, :, 0].numpy() + 1.0) / 2.0
        axes.flatten()[i].imshow(img, cmap='gray')
        axes.flatten()[i].axis('off')
    title = f"DCGAN Output - {label}" if label else f"DCGAN Generated Digits - Epoch {epoch}"
    plt.suptitle(title, fontsize=12, fontweight='bold')
    plt.tight_layout()
    fname = f"generated_epoch_{epoch:02d}.png"
    plt.savefig(os.path.join(target_dir, fname), dpi=200)
    plt.close()
    print(f"Saved {fname}", flush=True)

# 5. Training Step with tf.function
@tf.function
def train_step(images, batch_size):
    noise = tf.random.normal([batch_size, 100])
    
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)
        
        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)
        
        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)
        
    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)
    
    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))
    
    return gen_loss, disc_loss

# 6. Optimized Fast Dataset Pipeline (30 batches of 128 per epoch = 300 total steps)
BATCH_SIZE = 128
STEPS_PER_EPOCH = 30
EPOCHS = 10

train_dataset = tf.data.Dataset.from_tensor_slices(x_train).shuffle(10000).batch(BATCH_SIZE, drop_remainder=True)

g_loss_history = []
d_loss_history = []

print(f"\nStarting Optimized Training: {EPOCHS} Epochs ({STEPS_PER_EPOCH} steps/epoch, batch size={BATCH_SIZE})...", flush=True)
start_time = time.time()

# Save Epoch 0 (Untrained state)
save_generated_images(generator, 0, "Epoch 0 (Initial Random Noise)")

for epoch in range(1, EPOCHS + 1):
    epoch_start = time.time()
    batch_g_loss = []
    batch_d_loss = []
    
    dataset_iter = iter(train_dataset)
    for step in range(STEPS_PER_EPOCH):
        image_batch = next(dataset_iter)
        gl, dl = train_step(image_batch, BATCH_SIZE)
        batch_g_loss.append(float(gl))
        batch_d_loss.append(float(dl))
        
        if (step + 1) % 10 == 0 or (step + 1) == STEPS_PER_EPOCH:
            print(f"Epoch [{epoch:02d}/{EPOCHS:02d}] Step [{step+1:02d}/{STEPS_PER_EPOCH:02d}] | D_Loss: {float(dl):.4f} | G_Loss: {float(gl):.4f}", flush=True)
            
    mean_gl = np.mean(batch_g_loss)
    mean_dl = np.mean(batch_d_loss)
    g_loss_history.append(mean_gl)
    d_loss_history.append(mean_dl)
    
    elapsed = time.time() - epoch_start
    print(f"--> Epoch {epoch:02d} Finished in {elapsed:.1f}s | Mean D_Loss: {mean_dl:.4f} | Mean G_Loss: {mean_gl:.4f}", flush=True)
    
    # Save checkpoint plots
    if epoch in [1, 2, 3, 5, 8, 10]:
        save_generated_images(generator, epoch, f"Epoch {epoch:02d}")

total_elapsed = time.time() - start_time
print(f"\nTraining successfully finished in {total_elapsed:.1f}s ({total_elapsed/60:.2f} mins).", flush=True)

# 7. Plot Loss Curves
plt.figure(figsize=(10, 5))
plt.plot(range(1, EPOCHS + 1), d_loss_history, label='Discriminator Loss (D_Loss)', color='#dc2626', linewidth=2.5, marker='o')
plt.plot(range(1, EPOCHS + 1), g_loss_history, label='Generator Loss (G_Loss)', color='#2563eb', linewidth=2.5, marker='s')
plt.title('DCGAN Training Loss Convergence on MNIST Dataset', fontsize=14, fontweight='bold', pad=12)
plt.xlabel('Epoch Number', fontsize=12)
plt.ylabel('Binary Cross-Entropy Loss', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12, loc='upper right')
plt.tight_layout()
plt.savefig(os.path.join(target_dir, "gan_loss_curve.png"), dpi=200)
plt.close()
print("Saved gan_loss_curve.png", flush=True)

# 8. Progression Montage
checkpoints = [0, 1, 3, 5, 10]
fig, axes = plt.subplots(1, len(checkpoints), figsize=(16, 3.6))
labels = ["Epoch 0\n(Random Noise)", "Epoch 1\n(Stroke Emergence)", "Epoch 3\n(Digit Form)", "Epoch 5\n(Distinct Shapes)", "Epoch 10\n(Realistic Digits)"]

for idx, ep in enumerate(checkpoints):
    img_data = plt.imread(os.path.join(target_dir, f"generated_epoch_{ep:02d}.png"))
    axes[idx].imshow(img_data)
    axes[idx].set_title(labels[idx], fontsize=11, fontweight='bold')
    axes[idx].axis('off')

plt.suptitle("Generative Adversarial Network (DCGAN) Visual Evolution Over Epochs", fontsize=14, fontweight='bold', y=1.03)
plt.tight_layout()
plt.savefig(os.path.join(target_dir, "gan_progression_montage.png"), dpi=200)
plt.close()
print("Saved gan_progression_montage.png", flush=True)

# 9. Real vs Generated Comparison Plot
fig, axes = plt.subplots(2, 8, figsize=(14, 4))
for i in range(8):
    axes[0, i].imshow((x_train[i, :, :, 0] + 1.0) / 2.0, cmap='gray')
    axes[0, i].axis('off')
    if i == 0:
        axes[0, i].set_title("Ground Truth\n(Real MNIST)", fontsize=10, fontweight='bold', loc='left')

final_predictions = generator(tf.random.normal([8, 100], seed=99), training=False)
for i in range(8):
    axes[1, i].imshow((final_predictions[i, :, :, 0].numpy() + 1.0) / 2.0, cmap='gray')
    axes[1, i].axis('off')
    if i == 0:
        axes[1, i].set_title("Generated Samples\n(DCGAN Synthetic)", fontsize=10, fontweight='bold', loc='left')

plt.suptitle("Qualitative Comparison: Real MNIST Handwritten Digits vs DCGAN Generated Digits", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(target_dir, "real_vs_generated_comparison.png"), dpi=200)
plt.close()
print("Saved real_vs_generated_comparison.png", flush=True)

# Save Generator model
generator.save(os.path.join(target_dir, "dcgan_generator_mnist.keras"))
print("Saved dcgan_generator_mnist.keras successfully!", flush=True)
