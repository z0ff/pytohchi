import spacy

nlp = spacy.load('ja_ginza')

def hoge(s: str):
    doc = nlp(s)

    for sent in doc.sents:
        for token in sent:
            print(token.i, token.orth_, token.lemma_, token.pos_, 
                token.tag_, token.dep_, token.head.i)

