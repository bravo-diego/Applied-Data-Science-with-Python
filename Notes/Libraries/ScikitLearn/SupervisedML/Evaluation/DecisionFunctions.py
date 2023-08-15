# Classifier Decision Function

# Given a set of test points, the decision function method provides for each one a classifier score value that indicates how confidently classifier predicts the positive class (large magnitude positive values) or the negative class (large magnitude negative values).

# Choosing a fixed decision threshold gives a classification rule; by sweeping the decision threshold through the entire range of possible score values, we get a series of classification outcomes that form a curve (precision recall curve).

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression

dataset = load_digits()

X, y = dataset.data, dataset.target     

y_binary_imbalanced = y.copy()
y_binary_imbalanced[y_binary_imbalanced != 1] = 0
        
X_train, X_test, y_train, y_test = train_test_split(X, y_binary_imbalanced, random_state = 0)

lr = LogisticRegression().fit(X_train, y_train) # logistic regression classifier

# Decision Scores

y_scores_lr = lr.fit(X_train, y_train).decision_function(X_test)
y_score_list = list(zip(y_test[0:20], y_scores_lr[0:20]))

print(y_score_list)

# Predicted Probabilities

# predict_proba function provides predicted probabilities of class membership. Typically a classifier would use the more likely class; that is in a binary classifier.

y_proba_lr = lr.fit(X_train, y_train).predict_proba(X_test)
y_proba_list = list(zip(y_test[0:20], y_proba_lr[0:20,1]))

print(y_proba_list)

# A higher threshold means that a classifier has to be more confident in predicting the class.


