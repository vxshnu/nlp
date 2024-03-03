#Read currency along with the amount
import spacy
nlp=spacy.blank('en')
doc=nlp('Tony gave two $ to Peter, Bruce gave 500 € to Steve')
for token in doc:
    if token.like_num and doc[token.i+1].is_currency:
        print(token.text, doc[token.i+1].text)