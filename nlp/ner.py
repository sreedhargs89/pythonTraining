import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

ex = 'What is link for aws us10 hotfix'


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent

sent = preprocess(ex)

pattern = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print (cs)

