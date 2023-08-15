# Linear Classifiers: Support Vector Machines.

# Linear models are also used for classification. A linear classifier return a class value (+1 or -1 in a binary problem) by computing a linear function of features (X1, X2,..., Xn). 

    # f(x, w, b) = sign(w o x + b)
    
            # If we have a simple case with X1 and X2 then:
                
                # f(x, w, b) = (w1, w2) o (x1, x2) = w1x1 + w2x2 + b
    
        # where w is a vector of weights; x is a vector of feature values and b is a bias term that gets added in
        
# A way to define a good classifier is to reward classifiers for the amount of separation that can provide between the two classes; to do this we need define the concept of classifier margin.

# Classifier margin is defined as the maximum width the decision boundary area can be increased before hitting a data point.

# Among all classifiers we can define the best classifier as the classifier that has the maximum amount of margin; the maximum margin classifier is called as Linear Support Vector Machine (LSVM).

# C parameter determines regularization; larger values of C less regularization while smaller values of C increases regularization.

# Application to a real dataset.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
(X_cancer, y_cancer) = load_breast_cancer(return_X_y = True)

X_train, X_test, y_train, y_test = train_test_split(X_cancer, y_cancer, random_state=0)

clf = LinearSVC().fit(X_train, y_train)
print("Breast Cancer Dataset")
print("Accuracy of Linear SVC Classifier on Training Set: {:.2f}".format(clf.score(X_train, y_train)))
print("Accuracy of Linear SVC Classifier on Test Set: {:.2f}".format(clf.score(X_test, y_test)))


# Linear Models (linear and logistic regression) are simple and easy to train; prediction are very fast. Scales well to very large datasets. 
