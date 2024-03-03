import spacy
nlp = spacy.load("en_core_web_sm")
text="""Inflation rose again in April, continuing a climb that has pushed consumers to the brink and is threatening the economic expansion, the Bureau of Labor Statistics reported Wednesday.\n\nThe consumer price index, a broad-based measure of prices for goods and services, increased 8.3% from a year ago, higher than the Dow Jones estimate for an 8.1% gain. That represented a slight ease from Marchâ€™s peak but was still close to the highest level since the summer of 1982.\n\nRemoving volatile food and ene"""
doc=nlp(text)
all_nouns=[]
all_num=[]
for token in doc:
    if token.pos_=='NOUN':
        all_nouns.append(token)
    elif token.pos_=='NUM':
        all_num.append(token)
        
print(all_nouns)
print('-------------------------------')
print(all_num)
print('-------------------------------')
count = doc.count_by(spacy.attrs.POS)
print(count)
print('-------------------------------')
for k,v in count.items():
    print(doc.vocab[k].text, "|",v)