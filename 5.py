#Lemmatization in Spacy
import spacy
nlp=spacy.load('en_core_web_sm')
doc=nlp("ate news readable feedable sewer riding catching king cracking ability")
for token in doc:
    print(token," | ",token.lemma_)
print(nlp.pipe_names)