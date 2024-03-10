#Named entity recog (ner)
import spacy

nlp=spacy.load('en_core_web_sm')
print(nlp.pipe_names)
doc=nlp("Tesla is going to buy Twitter for 50 Billion dollars!")

for ent in doc.ents:
    print(ent.text," | ",ent.label_," | ",spacy.explain(ent.label_))
"""
OUTPUT
Tesla  |  ORG  |  Companies, agencies, institutions, etc.
50 Billion dollars  |  MONEY  |  Monetary values, including unit
"""

#here twitter is not recognized as the model is not perfect ...try adding inc before it then it would recognise it as a company

#using span adding twitter as an ORG
from spacy.tokens import Span
s1=Span(doc,5,6,label="ORG")     #5,6 means that from 5th to 6 th charcter(doesnt incude 6th character)
doc.set_ents([s1],default="unmodified")

for ent in doc.ents:
    print(ent.text," | ",ent.label_," | ",spacy.explain(ent.label_))
    
"""
output
Tesla  |  ORG  |  Companies, agencies, institutions, etc.
Twitter  |  ORG  |  Companies, agencies, institutions, etc.
50 Billion dollars  |  MONEY  |  Monetary values, including unit
"""

