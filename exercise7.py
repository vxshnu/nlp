#find the bdays in the text using ner
import spacy

nlp=spacy.load('en_core_web_sm')

text = """Sachin Tendulkar was born on 24 April 1973, Virat Kholi was born on 5 November 1988, Dhoni was born on 7 July 1981
and finally Ricky ponting was born on 19 December 1974."""

doc = nlp(text)

for ent in doc.ents:
    if ent.label_=="DATE":
        print(ent.text)