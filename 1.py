#Introduction to spacy
import spacy
nlp=spacy.blank("en")
doc=nlp("Dr. Strange loves pav bhaji of mumbai as it costs only 2$ per plate.")
for token in doc:
    print(token)