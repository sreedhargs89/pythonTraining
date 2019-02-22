import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'What is the url link for the aws us10 hotfix')

allowed_list = ["NN", "NNP", "JJ", "FW", "VBG"]

result = ""
for token in doc:
    if token.tag_ in allowed_list:
    	result += token.text +  " "
    	##print(token.text, token.pos_, token.tag_)

print (result)
doc = nlp(u'What is the url link for the aws us10 hotfix')

print ("----------------------")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
