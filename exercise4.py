import spacy
nlp=spacy.load('en_core_web_sm')
text = """Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
"""
all_words=[]
doc=nlp(text)
for token in doc:
    all_words.append(token.lemma_)

sentences=" ".join(all_words)
print(sentences)