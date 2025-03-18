import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Path to the saved vocabulary file
vocab_file = "/Users/amarjahiji/Projects/Python/autoCorrect/vocabulary.pkl"

# Load saved vocabulary
with open(vocab_file, "rb") as f:
    vocabulary = pickle.load(f)

print("Loaded vocabulary successfully.")

def fit_vectorizer(vocab):
    """Fit a TF-IDF Vectorizer on the given vocabulary and return the vectorizer and TF-IDF matrix."""
    vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 3))
    tfidf_matrix = vectorizer.fit_transform(vocab)
    return vectorizer, tfidf_matrix

# Initial fitting of the vectorizer using the loaded vocabulary
vectorizer, tfidf_matrix = fit_vectorizer(vocabulary)

def autocorrect(word, vectorizer, tfidf_matrix, vocabulary):
    """
    Returns the closest word from the vocabulary using cosine similarity.
    The word and vocabulary are processed in lowercase.
    """
    word = word.lower()
    word_vector = vectorizer.transform([word])
    similarities = cosine_similarity(word_vector, tfidf_matrix)
    best_match_index = similarities.argmax()
    return vocabulary[best_match_index]

while True:
    # Prompt the user for a sentence, exit if the input is "-1"
    sentence = input("Enter a sentence to autocorrect (or '-1' to exit): ").strip()
    if sentence == "-1":
        break

    words = sentence.split()
    
    # Get autocorrection suggestion for each word
    corrected_words = [autocorrect(word, vectorizer, tfidf_matrix, vocabulary) for word in words]
    corrected_sentence = " ".join(corrected_words)
    
    print(f"\nDid you mean: {corrected_sentence}?")
    response = input("Is that correct? (y/n): ").strip().lower()
    
    if response == 'n':
        # Add each word from the original sentence to vocabulary if not already present.
        # Converting to lowercase for consistency.
        new_words = []
        for word in words:
            lower_word = word.lower()
            if lower_word not in (v.lower() for v in vocabulary):
                new_words.append(lower_word)
        if new_words:
            vocabulary.extend(new_words)
            # Save the updated vocabulary
            with open(vocab_file, "wb") as f:
                pickle.dump(vocabulary, f)
            print(f"Added {len(new_words)} new word(s) to the vocabulary.")
            # Re-fit the vectorizer with the updated vocabulary
            vectorizer, tfidf_matrix = fit_vectorizer(vocabulary)
        else:
            print("No new words were added to the vocabulary.")
    else:
        print("Sentence accepted.")

print("Exiting autocorrect loop.")
