# Report — Authorship Attribution (30 Columnists)

## Problem
Given a set of newspaper-style articles written by multiple authors, predict **which author** wrote a given text.

## Dataset
**30 Columnists**: raw texts organized by author folders under `data/30Columnists/raw_texts/`.
Each subfolder represents one author; each file is a single article.

## Method
1. Load and label raw text files.
2. Text preprocessing:
   - lowercasing, punctuation cleanup
   - stopword removal (NLTK or sklearn fallback)
   - optional lemmatization (NLTK WordNet)
3. Feature extraction:
   - CountVectorizer / TF-IDF (word n-grams)
   - (Optional) additional engineered features (numbers, stems, etc.) if enabled in the notebook
4. Models compared:
   - Multinomial Naive Bayes
   - Logistic Regression
   - Linear SVM (LinearSVC)
5. Evaluation:
   - train/test split
   - Accuracy, macro-F1, confusion matrix, and classification report

## How to Run
See `README.md` for environment setup and launch `notebooks/authorship_attribution.ipynb`.

## Files Delivered
- Packet: Jupyter notebook + dataset + dependency list.
- Output: metrics printed in-notebook, plus plots displayed inline.
