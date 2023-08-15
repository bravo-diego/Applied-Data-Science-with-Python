# Logistic Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Generalized linear regression; the logistic regression model still computes a weighted sum of the input features Xi and the intercept term b, but it runs this result through a special non-linear function: the logistic function.

# The effect of applying the logistic function is to compress the output of the linear function so that it's limited ti a range between 0 and 1; transforms real-valued input to an output number y between 0 and 1, interpreted as the probability the input object belongs to the positive class, given its input features (X0, X1,..., Xn).

# L2 regularization is on by default; parameter C controls amount of regularization (default 1.0). As with regularized linear regression, it can be important to normalize all features so that they are on the same scale.

    # Application to real dataset

cancer = load_breast_cancer()
(X_cancer, y_cancer) = load_breast_cancer(return_X_y = True)

X_train, X_test, y_train, y_test = train_test_split(X_cancer, y_cancer, random_state=0)

clf = LogisticRegression().fit(X_train, y_train)

print("Breast Cancer Dataset")
print("Accuracy of Logistic Regression Classifier on Training Set: {:.2f}".format(clf.score(X_train, y_train)))
print("Accuracy of Logistic Regression Classifier on Test Set: {:.2f}".format(clf.score(X_test, y_test)))
