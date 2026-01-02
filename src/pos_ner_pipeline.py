import re
import pandas as pd
import spacy
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


bbc_data = pd.read_csv("bbc_news.csv")
titles = bbc_data["title"].astype(str)


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)


titles_clean = titles.apply(clean_text)


nlp = spacy.load("en_core_web_sm")
docs = list(nlp.pipe(titles_clean))


pos_records = []
ner_records = []


for doc in docs:
    for token in doc:
        if token.is_alpha:
            pos_records.append({
                "token": token.text,
                "pos_tag": token.pos_
            })

    for ent in doc.ents:
        ner_records.append({
            "token": ent.text,
            "ner_tag": ent.label_
        })


pos_df = pd.DataFrame(pos_records)
ner_df = pd.DataFrame(ner_records)


pos_counts = (
    pos_df
    .groupby(["token", "pos_tag"])
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)

ner_counts = (
    ner_df
    .groupby(["token", "ner_tag"])
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)


print("\nTop Nouns:")
print(pos_counts[pos_counts.pos_tag == "NOUN"].head(10))

print("\nTop Verbs:")
print(pos_counts[pos_counts.pos_tag == "VERB"].head(10))

print("\nTop Adjectives:")
print(pos_counts[pos_counts.pos_tag == "ADJ"].head(10))


print("\nTop Persons:")
print(ner_counts[ner_counts.ner_tag == "PERSON"].head(10))

print("\nTop Locations:")
print(ner_counts[ner_counts.ner_tag == "GPE"].head(10))
