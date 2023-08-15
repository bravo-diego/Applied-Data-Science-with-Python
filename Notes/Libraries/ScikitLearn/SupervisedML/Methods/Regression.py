# K-Nearest Neighbors : Regression

import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Synthetic data set for simple regression

X_R1, y_R1 = make_regression(n_samples = 100, n_features = 1, n_informative = 1, bias = 150.0, noise = 30, random_state = 0)

X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1, random_state = 0)

knnreg = KNeighborsRegressor(n_neighbors = 5).fit(X_train, y_train)

print(knnreg.predict(X_test))
print("R-squared test score: {:.3f}".format(knnreg.score(X_test, y_test))) # r-squared score or coefficient of determination

# R-squared regression score measures how well a prediction model for regression fits the given data; the score is between 0 and 1. A value of 0 corresponds to a constant model that predicts the mean value of all training target values. A value of 1 corresponds to perfect prediction.

fig, subaxes = plt.subplots(1, 2 ,figsize=(8,4))
X_predict_input = np.linspace(-3, 3, 50).reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X_R1[0::5], y_R1[0::5], random_state = 0)

for thisaxis, K in zip(subaxes, [1, 3]):
    knnreg = KNeighborsRegressor(n_neighbors = K).fit(X_train, y_train)
    y_predict_output = knnreg.predict(X_predict_input)
    thisaxis.set_xlim([-2.5, 0.75])
    thisaxis.plot(X_predict_input, y_predict_output, '^', markersize = 10, label = "Predicted", alpha = 0.8)
    thisaxis.plot(X_train, y_train, 'o', label = "True Value", alpha = 0.8)
    thisaxis.set_xlabel("Input Feature")
    thisaxis.set_ylabel("Target Value")
    thisaxis.set_title("KNN Regression (K={})".format(K))
    thisaxis.legend()

plt.tight_layout()
plt.show()

fig, subaxes = plt.subplots(5, 1 ,figsize=(5,20))
X_predict_input = np.linspace(-3, 3, 500).reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1, random_state = 0)

for thisaxis, K in zip(subaxes, [1, 3, 7, 15, 55]):
    knnreg = KNeighborsRegressor(n_neighbors = K).fit(X_train, y_train)
    y_predict_output = knnreg.predict(X_predict_input)
    train_score = knnreg.score(X_train, y_train)
    test_score = knnreg.score(X_test, y_test)
    thisaxis.plot(X_predict_input, y_predict_output) 
    thisaxis.plot(X_train, y_train, 'o', label = "Train", alpha = 0.9)
    thisaxis.plot(X_test, y_test, '^', label = "Test", alpha = 0.9)
    thisaxis.set_xlabel("Input Feature")
    thisaxis.set_ylabel("Target Value")
    thisaxis.set_title("KNN Regression (K={})\n\Train $R^2 = {:.3f}$, Test $R^2 = {:.3f}$".format(K, train_score, test_score))
    thisaxis.legend()
    plt.tight_layout(pad = 0.4, w_pad = 0.5, h_pad = 1.0)

plt.show()

# Small values of k give models with higher complexity, and large values of k result in simpler models with lower complexity.

# Important parameters :

    # Model Complexity 
        
        # n_neighbors -- number of nearest neighbors (k) to consider 
        
    # Model fitting
        
        # metric -- distance function between data points (Euclidean distance)

linreg = LinearRegression().fit(X_train, y_train)

plt.subplot(121)
plt.scatter(X_R1, y_R1, marker = 'o', s = 50, alpha = 0.8)
plt.plot(X_R1, linreg.coef_ * X_R1 + linreg.intercept_, 'r-')
plt.title("Least-squares linear regression")
plt.xlabel("Feature value (x)")
plt.ylabel("Target value (y)")

plt.subplot(122)
knnreg = KNeighborsRegressor(n_neighbors = 7).fit(X_train, y_train)
y_predict_output = knnreg.predict(X_predict_input)
train_score = knnreg.score(X_train, y_train)
test_score = knnreg.score(X_test, y_test)
plt.plot(X_predict_input, y_predict_output) 
plt.plot(X_train, y_train, 'o', label = "Train", alpha = 0.9)
plt.plot(X_test, y_test, '^', label = "Test", alpha = 0.9)
plt.xlabel("Input Feature")
plt.ylabel("Target Value")
plt.title("KNN Regression (K = 17)\n\Train $R^2 = {:.3f}$, Test $R^2 = {:.3f}$".format( train_score, test_score))
plt.legend()
plt.tight_layout(pad = 0.4, w_pad = 0.5, h_pad = 1.0)

plt.show()

print("Linear Model Coeff (w): {}".format(linreg.coef_))
print("Linear Model Intercept (b): {:.3f}".format(linreg.intercept_))
print("R-squared Score (training): {:.3f}".format(linreg.score(X_train, y_train)))
print("R-squared Score (test): {:.3f}".format(linreg.score(X_test, y_test)))
