import spacy

nlp = spacy.load('ja_ginza')


# 係り受け解析
def dependency_parsing(s: str):
    doc = nlp(s)

    for sent in doc.sents:
        for token in sent:
            print(token.orth_, token.dep_, token.head.orth_)
        print('EOS')


# 述語を先頭に移動
def put_predicate_to_first(s: str) -> str:
    doc = nlp(s)

    tokens = [[token for token in sent] for sent in doc.sents]

    for sent_no in range(len(tokens)):
        root_no = None
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
        # dependency_parsing(s)
        print(put_predicate_to_first(s))
