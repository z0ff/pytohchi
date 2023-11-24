import spacy

nlp = spacy.load('ja_ginza')


# 係り受け解析
def dependency_parsing(s: str):
    doc = nlp(s)

    for sent in doc.sents:
        for token in sent:
            print(token.orth_, token.dep_, token.head.orth_)
        print('EOS')


# 述語(root)を先頭に移動
def put_root_to_head(sentence: str) -> str:
    doc = nlp(sentence)

    tokens = [[token for token in sent] for sent in doc.sents]

    for sent_no in range(len(tokens)):
        root_no: int = None
        punct = None if tokens[sent_no][-1].dep_ != 'punct' else tokens[sent_no][-1]
        for token_no in range(len(tokens[sent_no])):
            if tokens[sent_no][token_no].dep_ == 'ROOT':
                root_no = token_no
                break
        if root_no is not None:
            pred_no = root_no - 1 if tokens[sent_no][root_no - 1].dep_ == 'compound' else root_no
            predicate = tokens[sent_no][pred_no:]
            tokens[sent_no][pred_no:] = []
            tokens[sent_no][0:0] = predicate
            if tokens[sent_no][-1].dep_ == 'punct':
                tokens[sent_no].pop(-1)
            if punct is not None:
                tokens[sent_no].append(punct)

    inverted = ''

    for sent in tokens:
        for token in sent:
            inverted += token.orth_

    return inverted


# 述語(root)に従属する斜格名刺(obl)を先頭に移動
def put_obl_to_head(sentence: str) -> str:
    doc = nlp(sentence)

    tokens = [[token for token in sent] for sent in doc.sents]

    for sent_no in range(len(tokens)):
        root_no: int = None
        punct = None if tokens[sent_no][-1].dep_ != 'punct' else tokens[sent_no][-1]
        for token_no in range(len(tokens[sent_no])):
            if tokens[sent_no][token_no].dep_ == 'ROOT':
                root_no = token_no
                break
        if root_no is not None:
            pred_no = root_no
            obl_no: int = None
            for token_no in range(root_no, 0, -1):
                if tokens[sent_no][token_no].head == tokens[sent_no][root_no]:
                    if tokens[sent_no][token_no].dep_ == 'obl':
                        pred_no = token_no
                        obl_no = token_no
                if obl_no is not None:
                    if tokens[sent_no][token_no].head == tokens[sent_no][obl_no]:
                        pred_no = token_no
            predicate = tokens[sent_no][pred_no:]
            tokens[sent_no][pred_no:] = []
            tokens[sent_no][0:0] = predicate
            if tokens[sent_no][-1].dep_ == 'punct':
                tokens[sent_no].pop(-1)
            if punct is not None:
                tokens[sent_no].append(punct)

    inverted = ''

    for sent in tokens:
        for token in sent:
            inverted += token.orth_

    return inverted


if __name__ == '__main__':
    while True:
        print('文を入力。終了するときはexit=> ', end='')
        s = input()
        if s == 'exit':
            break
        dependency_parsing(s)
        print(put_root_to_head(s))
        print(put_obl_to_head(s))
