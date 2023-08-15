# Confusion Matrices

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.dummy import DummyClassifier
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

    # Accuracy = True Negatives + True Positives / (True Negatives + True Positives  + False Negatives + False Positives)
             # = Total Number of correct predictions / Total number of instances
             
    # Classification Error = False Positives + False Negatives / (True Negatives + True Positives + False Negatives + False Positives)
             # = Total Number of incorrect predictions / Total number of instances
             
# It is more important to avoid false positives, or false negatives? Precision is used as a metric when our objective is to minimize false positives. Recall is used when the objective is to minimize false negatives.

    # Recall (True Positive Rate) = True Positives / (True Positives + False Negatives)
    
        # What fraction of all positive instances does the classifier correctly identify as positive?
        
    # Precision = True Positives / (True Positives + False Positives)
    
        # What fraction of positive predictions are correct?
        
    # Specificity (False Positive Rate) = False Positives / (True Negatives + False Positives)
    
        # What Fraction of all negative instances does the classifier incorrectly identify as positive?
        
dataset = load_digits()

X, y = dataset.data, dataset.target     

y_binary_imbalanced = y.copy()
y_binary_imbalanced[y_binary_imbalanced != 1] = 0
        
X_train, X_test, y_train, y_test = train_test_split(X, y_binary_imbalanced, random_state = 0)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

dt = DecisionTreeClassifier(max_depth = 2).fit(X_train, y_train)
tree_predicted = dt.predict(X_test)
confusion = confusion_matrix(y_test, tree_predicted)

print("Decision tree classifier (max_depth = 2)\n", confusion)

print("Accuracy: {:.2f}".format(accuracy_score(y_test, tree_predicted)))
print("Precision: {:.2f}".format(precision_score(y_test, tree_predicted)))
print("Recall: {:.2f}".format(recall_score(y_test, tree_predicted)))
print("F1: {:.2f}".format(f1_score(y_test, tree_predicted)))

from sklearn.metrics import classification_report

print(classification_report(y_test, tree_predicted, target_names=['not 1', '1']))
