import spacy
nlp=spacy.load('en_core_web_sm')
doc = nlp("running painting walking dressing likely children who good ate fishing")
for token in doc:
    print(token.text," | ",token.lemma_)