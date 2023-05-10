import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree

## Reading csv file
dataset = pd.read_csv('/Users/Nikhil/Downloads/Social_Network_Ads.csv')
x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:,-1].values
print(dataset)
#print(dataset.iloc[:,1:3])

## Splitting test and train data
from sklearn.model_selection  import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.25, random_state=0)

## Feature Scaling
from sklearn.preprocessing import StandardScaler
sc =StandardScaler()
X_train = sc.fit_transform(X_train)
x_test = sc.transform(X_test)

## Training the decision Tree Classifier model on the training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state=0)
classifier.fit(X_train, y_train)

## Predicting the test set results
y_pred = classifier.predict(X_test)
print(y_pred)

#tree.plot_tree(classifier)

## Making Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
