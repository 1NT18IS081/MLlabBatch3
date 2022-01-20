import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report

zoo = pd.read_csv("zoo.csv")
zoo.drop("animal_name",axis=1,inplace=True)

feature_names = ['hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venomous','fins','legs','tail','domestic',]
X = zoo[feature_names]
y = zoo['class_type']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.2, test_size=.8)

clf = DecisionTreeClassifier().fit(X_train, y_train)

pred = clf.predict(X_test)
print('Accuracy of classifier on test set: {:.2f}' .format(clf.score(X_test, y_test)))
print(classification_report(y_test, pred))
print(confusion_matrix(y_test,pred))
Accuracy of classifier on test set: 0.84
              precision    recall  f1-score   support

           1       1.00      1.00      1.00        33
           2       1.00      1.00      1.00        16
           3       0.00      0.00      0.00         5
           4       0.56      1.00      0.71        10
           5       0.00      0.00      0.00         4
           6       1.00      0.20      0.33         5
           7       0.62      1.00      0.76         8

    accuracy                           0.84        81
   macro avg       0.60      0.60      0.54        81
weighted avg       0.80      0.84      0.79        81

[[33  0  0  0  0  0  0]
 [ 0 16  0  0  0  0  0]
 [ 0  0  0  4  0  0  1]
 [ 0  0  0 10  0  0  0]
 [ 0  0  0  4  0  0  0]
 [ 0  0  0  0  0  1  4]
 [ 0  0  0  0  0  0  8]]
