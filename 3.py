#ADD SPECIAL CASE eg:gimme as gim, me instead of gimme
import spacy
from spacy.symbols import ORTH
nlp=spacy.blank("en")
#the next line should always come first before doc=nlp()
nlp.tokenizer.add_special_case("gimme",[{ORTH:"gim"},{ORTH:'me'}])
doc=nlp("Dr. Strange loves pav bhaji of mumbai as it costs only 2$ per plate. He is gonna gimme some pav bhaji.")
tokens=[token.text for token in doc]
print(tokens)