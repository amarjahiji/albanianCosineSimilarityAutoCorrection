# Albanian Auto Correct using Cosine Similarity

## Overview
This project is a data mining course homework that implements an Albanian autocorrect tool. The tool takes a user input sentence and suggests corrections by comparing each word with a vocabulary using cosine similarity. The correction is based on TF-IDF vectorization with character n-grams.

## Project Structure
- **dataset.py**  
  Loads the latest version of the Kosovo News Articles Dataset from Kaggle using the `kagglehub` package.  
  *Dataset Source:* [Kosovo News Articles Dataset by Gent Rexha](https://www.kaggle.com/datasets/gentrexha/kosovo-news-articles-dataset/data)

- **vocab.py**  
  Processes the CSV dataset in chunks to create a full vocabulary of unique words. The resulting vocabulary is saved as `fullvocab.pkl`.

- **smallerVocab.py**  
  Similar to `vocab.py`, but limits the vocabulary to 2000 words. The smaller vocabulary is saved as `vocabulary.pkl`.

- **autoCorrection.py**  
  Contains the main logic for autocorrection. It uses a TF-IDF vectorizer (with character n-grams from 2 to 3) and cosine similarity to suggest the closest matching word from the vocabulary for each input word. The script also allows for vocabulary updates if the suggestion is incorrect.

- **requirements.txt**  
  Lists all required Python libraries and their versions needed to run the project.

## Installation
1. **Clone the Repository**  
   Download or clone the project files into your local machine.

2. **Set Up a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use: env\Scripts\activate

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

## Dataset Details
The dataset used in this project is available on Kaggle:
[Kosovo News Articles Dataset by Gent Rexha](/https://www.kaggle.com/datasets/gentrexha/kosovo-news-articles-dataset/data)
