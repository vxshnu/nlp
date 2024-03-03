#Reading file and using some inbuilt functions such as like_email
import spacy
with open("Spacy\2.txt") as f:
    text=f.readlines()
nlp=spacy.blank("en")
text=' '.join(text)
doc=nlp(text)
emails=[]
for token in doc:
    if token.like_email:
        emails.append(token)
print(emails)