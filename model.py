import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from keras.models import Sequential

from keras.layers import Dense

import numpy
numpy.random.seed(7)
dataset = numpy.loadtxt("data_pivoted.csv", delimiter=",")

model = Sequential()

model.add(Dense(140, input_dim=140, activation='relu'))

model.add(Dense(140, activation='relu'))

model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

