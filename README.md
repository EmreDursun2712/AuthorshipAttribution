# Authorship Attribution (NLP Midterm) — 30 Columnists

This project performs **authorship attribution** on the **30 Columnists** dataset using classic NLP features and baseline ML models.
It loads raw text articles, applies preprocessing, extracts vector features (e.g., bag-of-words / TF-IDF), trains multiple classifiers,
and reports accuracy/F1 with confusion matrices.

## Repository Structure

- `notebooks/` → main Jupyter notebook (end-to-end pipeline)
- `data/30Columnists/` → dataset (raw texts + ARFF files as provided)
- `docs/REPORT.md` → short GitHub-friendly report
- `requirements.txt` → Python dependencies

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
jupyter notebook
```

Open: `notebooks/authorship_attribution.ipynb`

> The notebook downloads required NLTK resources (`stopwords`, `wordnet`) automatically on first run.

## Notes
- This repo includes the dataset for course submission convenience. If you prefer, you can remove `data/` and re-download from the original source.
