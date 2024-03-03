#Adding exception cases for lemmatization by adding the new words into attribute_ruler eg:bro as brother, brah as brother
import spacy
nlp=spacy.load('en_core_web_sm')
print(nlp.pipe_names)
ar=nlp.get_pipe('attribute_ruler')
ar.add([[{'TEXT':'bro'}],[{'TEXT':'brah'}]],{"LEMMA":"Brother"})
doc=nlp("bro how can you do this to me. brah!")
for token in doc:
    print(token," | ",token.lemma_)