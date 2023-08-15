# Multi-Class Classification

# Scikit-learn converts a multiclass classification problem into a series of binary problems. Scikit-learn creates one binary classifier that predicts that class against all the other classes. 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC

# In the fruit dataset there are four categories of fruit. So scikit-learn learns four different binary classifiers.

fruits = pd.read_table('/home/aspphem/Desktop/Files/TXT/fruit_data_with_colors.txt')

feature_names_fruits = ['height', 'width', 'mass', 'color_score']
X_fruits = fruits[feature_names_fruits]
y_fruits = fruits['fruit_label']
target_names_fruits = ['apple', 'mandarin', 'orange', 'lemon']

X_fruits_2d = fruits[['height', 'width']]
y_fruits_2d = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X_fruits_2d, y_fruits_2d, random_state = 0)

clf = LinearSVC(C= 5, random_state = 67).fit(X_train, y_train)
print("Coefficients:\n", clf.coef_)
print("Intercepts:\n", clf.intercept_)

plt.figure(figsize=(6,6))
colors = ['r', 'g', 'b', 'y']
cmap_fruits = ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#FFFF00'])

plt.scatter(X_fruits_2d[['height']], X_fruits_2d[['width']], c = y_fruits_2d, cmap = cmap_fruits, edgecolor = 'black', alpha = 0.7)

x_0_range = np.linspace(-10, 15)

for w, b, color in zip(clf.coef_, clf.intercept_, ['r', 'g', 'b', 'y']):
    plt.plot(x_0_range, -(x_0_range * w[0] + b) / w[1], c = color, alpha = 0.8)
    
plt.legend(target_names_fruits)
plt.xlabel('Height')
plt.ylabel('Width')
plt.xlim(-2, 12)
plt.ylim(-2, 15)

plt.show()
