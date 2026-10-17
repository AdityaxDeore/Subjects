"""
Assignment No. 8
Title: Text Generation: Implement a Long Short-Term Memory (LSTM) network using TensorFlow 2 for text generation tasks.
Train the LSTM model on a dataset of text sequences and generate new text samples.

Student Details:
Name: Aditya Chandrajit Deore
PRN: 124B1F116
Course: Generative AI (GEN AI)
"""

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

print("==========================================================")
print("PART A: Load and Understand Data")
print("==========================================================")
print("TensorFlow version:", tf.__version__)

text = """
Generative AI can create new text, images and music.
Language models learn the patterns of words from large amounts of text.
An LSTM network can remember important information from earlier words.
Text generation predicts the next word in a sentence.
Deep learning models are trained using large datasets.
Neural networks learn patterns by adjusting their weights.
Data preprocessing makes the dataset clean and ready for training.
A tokenizer converts words into numbers for the model.
The embedding layer turns each word into a dense vector.
The LSTM layer learns the order of words in a sentence.
The dense layer predicts the probability of every word.
Training a model needs many epochs to reduce the loss.
A good model can generate new sentences from a seed text.
Machine learning helps computers learn from data.
Artificial intelligence is changing education and healthcare.
Recurrent neural networks are used for sequence data.
The forget gate decides which information the LSTM should remove.
The input gate decides which new information the LSTM should store.
The output gate decides what the LSTM should pass to the next step.
Generative models can create content that looks like real data.
Students use Python and TensorFlow to build deep learning models.
A seed text is the starting point for text generation.
The model predicts one word at a time to build a sentence.
Cleaning the text improves the quality of the training data.
Good training data helps the model generate meaningful text.
"""

# Store each line as a row in a DataFrame
lines = [l.strip() for l in text.split('\n') if l.strip() != ""]
df = pd.DataFrame({'sentence': lines})

print("Number of sentences:", len(df))
print("Number of words:", sum(len(s.split()) for s in lines))
print("\nFirst 10 sentences:")
print(df.head(10))

print("\n==========================================================")
print("PART B: Preprocess Text")
print("==========================================================")
# 1. Clean and normalize: Lowercase and remove punctuation
df['clean'] = (df['sentence'].str.lower()
               .str.replace(r'[^a-z\s]', '', regex=True)
               .str.strip())
print("Cleaned text sample:")
print(df[['sentence', 'clean']].head(5))

# 2. Tokenize with the Keras Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(df['clean'])

total_words = len(tokenizer.word_index) + 1  # +1 because index 0 is reserved for padding
print("\nVocabulary size:", total_words)
print("First 15 entries of word index:")
print(dict(list(tokenizer.word_index.items())[:15]))

# 3. Convert words into numerical sequences
sample = df['clean'][0]
print("\nSample clean sentence:", sample)
print("Tokenized sequence:", tokenizer.texts_to_sequences([sample])[0])

print("\n==========================================================")
print("PART C: Create Sequences")
print("==========================================================")
# 1. Divide each sentence into growing sequences (n-grams)
input_sequences = []

for line in df['clean']:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(2, len(token_list) + 1):
        input_sequences.append(token_list[:i])

print("Total sequences:", len(input_sequences))
print("Example sequences:", input_sequences[:3])

# 2. Apply padding so all sequences have the same length
max_len = max(len(seq) for seq in input_sequences)
input_sequences = pad_sequences(input_sequences, maxlen=max_len, padding='pre')

print("Maximum sequence length:", max_len)
print("Padded shape:", input_sequences.shape)

# 3. Input (X) = all words except the last, target (y) = the last word
X = input_sequences[:, :-1]
y = input_sequences[:, -1]

print("X shape:", X.shape)
print("y shape:", y.shape)

print("\n==========================================================")
print("PART D: Build the LSTM Model")
print("==========================================================")
model = Sequential([
    Input(shape=(max_len - 1,)),
    Embedding(input_dim=total_words, output_dim=64),
    LSTM(128),
    Dense(total_words, activation='softmax')
])

# Integer targets, so sparse categorical cross-entropy is used (no one-hot needed)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

print("\n==========================================================")
print("PART E: Train the Model")
print("==========================================================")
history = model.fit(X, y, epochs=200, batch_size=32, verbose=1)

print("\n==========================================================")
print("PART F: Generate Text")
print("==========================================================")
index_to_word = {index: word for word, index in tokenizer.word_index.items()}

def generate_text(seed_text, next_words, temperature=0.7):
    for _ in range(next_words):
        # Convert the current text to a padded sequence
        tokens = tokenizer.texts_to_sequences([seed_text.lower()])[0]
        tokens = pad_sequences([tokens], maxlen=max_len - 1, padding='pre')
        
        # Predict probabilities of the next word
        probs = model.predict(tokens, verbose=0)[0].astype('float64')
        
        # Apply temperature and pick the next word
        probs = np.log(probs + 1e-8) / temperature
        probs = np.exp(probs) / np.sum(np.exp(probs))
        next_index = np.random.choice(len(probs), p=probs)
        
        seed_text += " " + index_to_word.get(next_index, "")
    return seed_text

print("\n--- Generated Samples ---")
print("Seed: 'generative ai' (temp=0.7):")
print(generate_text("generative ai", 8))

print("\nSeed: 'the lstm layer' (temp=0.7):")
print(generate_text("the lstm layer", 8))

print("\nSeed: 'a good model' (temp=1.0):")
print(generate_text("a good model", 8, temperature=1.0))

print("\nSeed: 'text generation' (temp=0.5):")
print(generate_text("text generation", 8, temperature=0.5))
