# Model Evaluation and Selection

# Accuracy is the fraction of samples that were classified correctly. That is where the classifier's predicted label matched the correct or true label.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.dummy import DummyClassifier
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

dataset = load_digits()

X, y = dataset.data, dataset.target

for class_name, class_count in zip(dataset.target_names, np.bincount(dataset.target)):
    print(class_name, class_count)
    
y_binary_imbalanced = y.copy()
y_binary_imbalanced[y_binary_imbalanced != 1] = 0

print("Original labels:\t", y[1:30])
print("New binary labels:\t", y_binary_imbalanced[1:30])

print(np.bincount(y_binary_imbalanced))

X_train, X_test, y_train, y_test = train_test_split(X, y_binary_imbalanced, random_state = 0)

svm = SVC(kernel = 'rbf', C = 1).fit(X_train, y_train)
svm.score(X_test, y_test)

# Dummy Classifier is a classifier that makes predictions using simple rules, which can be useful as a baseline for comparison against actual classifiers, especially with imbalanced classes.

dummy_majority = DummyClassifier(strategy = 'most_frequent').fit(X_train, y_train)
y_dummy_predictions = dummy_majority.predict(X_test) # most_frequent strategy predicts the most frequent label in the training set; stratified random predictions based on training set class distribution; uniform generates predictions uniformly at random; constant always predicts a constant label provided by the user

print(y_dummy_predictions)

print(dummy_majority.score(X_test, y_test))

svm = SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
print(svm.score(X_test, y_test))

# Confusion Matrices

dummy_majority = DummyClassifier(strategy = 'most_frequent').fit(X_train, y_train)
y_majority_predicted = dummy_majority.predict(X_test)
confusion = confusion_matrix(y_test, y_majority_predicted)

print("Most frequent class (dummy classifier)\n", confusion) # possible outcomes of a binary classifier

    # A = [[TN FP], [FN TP]] True Negative, False Positive; False Negative True Positive
    
    # Successful predictions of the classifier are on the diagonal of the matrix, where the true class matches the predicted class

dummy_classprop = DummyClassifier(strategy = 'stratified').fit(X_train, y_train)
y_classprop_predicted = dummy_classprop.predict(X_test)
confusion = confusion_matrix(y_test, y_classprop_predicted)

print("Random class-proportional prediction (dummy classifier)\n", confusion)

svm = SVC(kernel='linear', C=1).fit(X_train, y_train)
svm_predicted = svm.predict(X_test)
confusion = confusion_matrix(y_test, svm_predicted)

print("Support vector machine classifier (linear kernel, C=1)\n", confusion)

lr = LogisticRegression().fit(X_train, y_train)
lr_predicted = lr.predict(X_test)
confusion = confusion_matrix(y_test, lr_predicted)

print("Logistic regression classifier (default settings)\n", confusion)

dt = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train)
tree_predicted = dt.predict(X_test)
confusion = confusion_matrix(y_test, tree_predicted)

print("Decision tree classifier (max_depth = 2)\n", confusion)


