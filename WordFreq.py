#!/usr/bin/env python
# coding=UTF-8
#
# Outputs 200 most-used words from a text file
#
# Usage:
#
#   ./WordFreq.py input.txt
#
# Sample output:
#
# man;591
# old;528
# mrs.;479
# eyes;430
# ...
#
# Requires NLTK. Official installation docs: http://www.nltk.org/install.html
#
# sudo apt-get install python-pip
# sudo pip install -U nltk
# python
# >>> import nltk
# >>> nltk.download('stopwords')
# >>> nltk.download('punkt')
# >>> exit()

import sys
import codecs
import nltk
from nltk.corpus import stopwords

# NLTK's default German stopwords
default_stopwords = set(nltk.corpus.stopwords.words('english'))

# We're adding some on our own - could be done inline like this...
# custom_stopwords = set((u'–', u'dass', u'mehr'))
# ... but let's read them from a file instead (one stopword per line, UTF-8)

stopwords_file = './stopwords.txt'
custom_stopwords = set(codecs.open(stopwords_file, 'r', 'utf-8').read().splitlines())
all_stopwords = default_stopwords | custom_stopwords


input_file = sys.argv[1]

fp = codecs.open(input_file, 'r', 'utf-8')

words = nltk.word_tokenize(fp.read())

# Remove single-character tokens (mostly punctuation)
words = [word for word in words if len(word) > 3]
#nwords = [word for word in words if len(word) > 3]

#Calculating total length of the Novel
totallen = len(words)
print("Total Length: %d" %totallen)

#Calculating total length of the Novel
totalwords=len(set(words))
print("Total number of words: %d" %totalwords)

# Remove numbers
words = [word for word in words if not word.isnumeric()]

# Lowercase all words (default_stopwords are lowercase too)
words = [word.lower() for word in words]

# Stemming words seems to make matters worse, disabled
# stemmer = nltk.stem.snowball.SnowballStemmer('german')
# words = [stemmer.stem(word) for word in words]

# Remove stopwords
words = [word for word in words if word not in all_stopwords]

# Calculate frequency distribution
#fdist = nltk.FreqDist(words)

#seldom used words
#distr = nltk.FreqDist(word for word in words)
#nwords = distr .keys()
#seldomwords = nwords [:100]

#print(seldomwords)



# Output top 200 words
for word, frequency in fdist.most_common(200):
    print(u'{};{}'.format(word, frequency))



