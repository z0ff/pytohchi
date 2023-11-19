import spacy

nlp = spacy.load('ja_ginza')


# 述語を先頭に移動
def invert_predicate(s: str):
    root = None
    doc = nlp(s)

    tokens = [[token for token in sent] for sent in doc.sents]

    for sent_no in range(len(tokens)):
        for token_no in range(len(tokens[sent_no])):
            if tokens[sent_no][token_no].dep_ == 'ROOT':
                root = tokens[sent_no][token_no].i
                break
        if root is not None:
            predicate = tokens[sent_no][root:]
            tokens[sent_no][root:] = []
            tokens[sent_no][0:0] = predicate

    for sent in tokens:
        for token in sent:
            if token.dep_ == 'ROOT':
                print(token.orth_, end='')
            elif token.i < root:
                print(token.orth_, end='')
            else:
                print(token.orth_, end='')
        print()


if __name__ == '__main__':
    while True:
        print('文を入力。終了するときはexit=> ', end='')
        s = input()
        if s == 'exit':
            break
        invert_predicate(s)
