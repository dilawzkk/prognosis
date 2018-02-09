import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

corpusdir = 'Data/' # Directory of corpus.

newcorpus = PlaintextCorpusReader(corpusdir, '.*')
