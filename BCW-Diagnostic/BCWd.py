	# Loading libraries and dataset

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()

print(cancer.DESCR)

print(cancer.keys())

# PART A' -- How many features does the breast cancer dataset have?

features = pd.unique(cancer['feature_names'])
print(len(features))

# PART A -- Convert the sklearn.dataset cancer to a DataFrame.

df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
df['target'] = cancer['target']
print(df.head()) # first five rows

# PART B -- Class distribution (i.e. how many instances of malignant and how many benign?)

values = ["malignant" if df['target'][i] == 0 else "benign" for i in range(len(df['target']))]
target = pd.Series(values)
print(target.groupby(target).count())

# PART C -- Split the DataFrame into X (the data) and y (the labels).

X = df.iloc[:, range(30)]
y = df.iloc[:, -1]

print(X)
print(y)

# PART D -- Split X and y into training and test sets (X_train, X_test, y_train, and y_test).

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0) # set random number generator state to 0

# PART E -- Fit a k-nearest neighbors (knn) classifier with X_train, y_train and using one nearest neighbor (n_neighbors = 1).

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# PART F -- Predict the class label using the mean value for each feature.

# Note: You can use cancerdf.mean()[:-1].values.reshape(1, -1) which gets the mean value for each feature, ignores the target column, and reshapes the data from 1 dimension to 2 (necessary for the precict method of KNeighborsClassifier).

values = df.mean()[:-1].values.reshape(1, -1)
mean_predict = knn.predict(values)

# PART G -- Predict the class labels for the test set X_test.

test_predict = knn.predict(X_test)

# PART H -- Find the score (mean accuracy) of your knn classifier using X_test and y_test.

score = knn.score(X_test, y_test)
print(score)














