import pandas as pd
import pickle

# File paths
file_path = "/Users/amarjahiji/Projects/Python/autoCorrect/Kosovo-News-Articles.csv"
vocab_file = "vocabulary.pkl"

# Initialize an empty set to store unique words
vocabulary = set()

# Set chunk size and maximum vocabulary size
chunk_size = 1000  # Adjust based on available memory
max_vocab_size = 2000

# Read the CSV in chunks
for chunk in pd.read_csv(file_path, usecols=["content"], chunksize=chunk_size):
    # Process each chunk: drop NaN values, convert text to lowercase, split into words, and update the vocabulary set
    chunk["content"].dropna().str.lower().str.split().apply(vocabulary.update)
    
    # Check if we've reached (or exceeded) the desired vocabulary size
    if len(vocabulary) >= max_vocab_size:
        print("Reached vocabulary limit:", len(vocabulary))
        break

# Limit the vocabulary to exactly max_vocab_size words (if there are more)
vocabulary = list(vocabulary)[:max_vocab_size]

# Save the vocabulary using pickle
with open(vocab_file, "wb") as f:
    pickle.dump(vocabulary, f)

print(f"Vocabulary saved successfully with {len(vocabulary)} words.")
