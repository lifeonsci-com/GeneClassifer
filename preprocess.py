#coding=utf8

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

le = preprocessing.LabelEncoder()

Label = pd.read_csv('./data/metadata.txt', sep="	", index_col=0)
# data = data.to_dict()
train_data = pd.read_csv('./data/train_data.txt', sep="	", header=0)
# train_data = pd.read_csv('./data/temp_train_data.txt', sep="	", header=0)
train_data = train_data.transpose()


FinalData = pd.concat([train_data, Label], axis=1)

y = FinalData['CellType']
X = FinalData.drop(['CellType'], axis=1)
X_embedded = TSNE(n_components=2).fit_transform(X)

le.fit(y)
y = le.transform(y)



X_train, X_test, y_train, y_test = train_test_split(X_embedded, y, test_size=0.3)


print (X_train)
print (X_test)
print (y_train)
print (y_test)

X_train.to_csv("./data/X_train.csv")
X_test.to_csv("./data/X_test.csv")
y_train.to_csv("./data/y_train.csv")
y_test.to_csv("./data/y_test.csv")



































    