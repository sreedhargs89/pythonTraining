import nltk

import urllib.request
from nltk.corpus import stopwords

text = "The PHP development team announces the immediate availability of PHP 7.0.33. Five security-related issues were fixed in this release. All PHP 7.0 users are encouraged to upgrade to this version."
tokens = [t for t in text.split()]
 
clean_tokens = tokens[:]
 
sr = stopwords.words('english')
 
for token in tokens:
 
    if token in stopwords.words('english'):
 
        clean_tokens.remove(token)
 
freq = nltk.FreqDist(clean_tokens)
 
for key,val in freq.items():
 
    print (str(key) + ':' + str(val))


# Word stemming means removing affixes from words and return the root word. 
# Ex: The stem of the word working => work.
# Porter stemming algorithm - Most used one
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('increases'))


# Word lemmatizing is similar to stemming, but the difference is the result of lemmatizing is a real word.
# Unlike stemming, when you try to stem some words, it will result in something like this:
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('playing', pos="v"))
print(lemmatizer.lemmatize('increases'))





