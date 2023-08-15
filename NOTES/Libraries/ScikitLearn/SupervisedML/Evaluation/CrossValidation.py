# Supervised Learning Methods.
    
    # Partitioning the data set into training and test sets using the train_test_split function; using test set as a way to estimate how well the model trained on the training data would generalize to new previously unseen data.
    
        # Test set represented data that had not been seen during training had the same general attributes as the original data set.
    
    # Creating and applying a scaler to both training and test sets (min max scaler);
    
    # Calling the fit method on the training set to estimate the model;
    
    # Applying the model by using the predict method to estimate the a target value for the new data instances; or by using the score method to evaluate the trained model's performance on the test set.
    
# Cross-Validation. 

# Cross-validation is NOT used to PRODUCE a model; is used to compare two different model types, using k-fold cross-validation. The point is don't rely on just a single train test split when computing your evaluation numbers.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


fruits = pd.read_table('/home/aspphem/Desktop/Files/TXT/fruit_data_with_colors.txt')

feature_names_fruits = ['height', 'width', 'mass', 'color_score']
X_fruits = fruits[feature_names_fruits]
y_fruits = fruits['fruit_label']
target_names_fruits = ['apple', 'mandarin', 'orange', 'lemon']

X_fruits_2d = fruits[['height', 'width']]
y_fruits_2d = fruits['fruit_label']

clf = KNeighborsClassifier(n_neighbors = 5)
X = X_fruits_2d
y = y_fruits_2d

cv_scores = cross_val_score(clf, X, y)

print("Cross-Validation Scores (5-fold):", cv_scores)
print("Mean Cross-Validation Score (5-fold): {:.3f}".format(np.mean(cv_scores)))
