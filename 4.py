#Pipelines
import spacy
nlp=spacy.blank('en')
nlp=spacy.load('en_core_web_sm')
doc=nlp('Infosys is going to be a trillion dollar company.')

print('---------------------------------------')

print(nlp.pipe_names)

print('---------------------------------------')

for token in doc:
    print(token," | ",token.pos_," | ",token.lemma_)
    
print('---------------------------------------')

for ent in doc.ents:
    print(ent.text," | ",ent.label," | ",spacy.explain(ent.label_))
    
print('---------------------------------------')
