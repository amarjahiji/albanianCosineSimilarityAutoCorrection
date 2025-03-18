import pandas as pd
import pickle

# File paths
file_path = "/Users/amarjahiji/Projects/Python/autoCorrect/Kosovo-News-Articles.csv"
vocab_file = "fullvocab.pkl"

# Initialize an empty set to store unique words
vocabulary = set()

# Set chunk size
chunk_size = 1000

# Read the CSV in chunks and update the vocabulary
for chunk in pd.read_csv(file_path, usecols=["content"], chunksize=chunk_size):
    # For each chunk, drop missing values, lower case the text, split into words, and update the vocabulary set
    chunk["content"].dropna().str.lower().str.split().apply(vocabulary.update)
    print(f"Processed chunk, current vocabulary size: {len(vocabulary)}")

vocabulary = list(vocabulary)

with open(vocab_file, "wb") as f:
    pickle.dump(vocabulary, f)

print(f"Vocabulary saved successfully with {len(vocabulary)} words.")
