# 📰 POS & NER Analysis on BBC News Headlines

Extract linguistic patterns and named entities from BBC news headlines using spaCy and NLTK. This project demonstrates core NLP techniques: Part-of-Speech tagging and Named Entity Recognition.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![spaCy](https://img.shields.io/badge/spaCy-3.0+-09A3D5.svg)](https://spacy.io/)
[![NLTK](https://img.shields.io/badge/NLTK-3.0+-green.svg)](https://www.nltk.org/)

## 🎯 What It Does

- **Cleans** headlines (lowercase, remove punctuation, stopwords, lemmatization)
- **Tags** parts of speech (nouns, verbs, adjectives)
- **Extracts** named entities (people, locations, organizations)
- **Ranks** most frequent words and entities by category

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Run the script
python src/pos_ner_pipeline.py

# Or explore interactively
jupyter notebook notebook/POS_NER_Analysis_BBC_News.ipynb
```

## 📁 Project Structure

```
pos-ner-analysis-bbc-news/
├── data/
│   └── bbc_news.csv                        # BBC news headlines dataset
├── notebook/
│   └── POS_NER_Analysis_BBC_News.ipynb     # Interactive exploration
├── src/
│   └── pos_ner_pipeline.py                 # Production pipeline
├── requirements.txt                         # Python dependencies
└── README.md                                # Documentation
```

## 🔄 Two Ways to Run

**Notebook** (`POS_NER_Analysis_BBC_News.ipynb`)  
→ For exploration, visualization, and iterative development

**Script** (`pos_ner_pipeline.py`)  
→ For automated execution, batch processing, or integration into workflows

Both implement the same NLP pipeline—use whichever fits your workflow.

## 📊 Sample Output

```
Top Nouns:
   token       pos_tag  count
   government  NOUN     145
   minister    NOUN     98
   market      NOUN     87

Top Persons:
   token       ner_tag  count
   Blair       PERSON   56
   Bush        PERSON   43

Top Locations:
   token       ner_tag  count
   UK          GPE      201
   US          GPE      178
```

## 🛠️ Tech Stack

- **spaCy** - POS tagging & NER
- **NLTK** - Text preprocessing
- **pandas** - Data aggregation
- **re** - Text cleaning

---

⭐ **Star this repo if you found it useful!**
