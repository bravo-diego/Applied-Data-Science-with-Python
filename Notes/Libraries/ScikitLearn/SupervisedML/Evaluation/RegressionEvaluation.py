# Regression Evaluation

# Typically r2 score is enough; it computes how well future instances will be predicted. Best possible score is 1.0.

# Alternative metrics include mean absolute error; mean squared error; and median absolute error.

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()

X = diabetes.data[:, None, 6]
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

lm = LinearRegression().fit(X_train, y_train)
lm_dummy_mean = DummyRegressor(strategy = 'mean').fit(X_train, y_train)

y_predict = lm.predict(X_test)
y_predict_dummy_mean = lm_dummy_mean.predict(X_test)

print("Linear Model Coefficients: ", lm.coef_)
print("Mean squared error (dummy): {:.2f}".format(mean_squared_error(y_test, y_predict_dummy_mean)))
print("Mean squared error (linear model): {:.2f}".format(mean_squared_error(y_test, y_predict)))
print("r2 Score (dummy): {:.2f}".format(r2_score(y_test, y_predict)))

plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_predict, color='green', linewidth=2)
plt.plot(X_test, y_predict_dummy_mean, color='red', linestyle='dashed', linewidth=2, label='dummy')

plt.show() # dummy regressor achieves a r2 score of 0.0, since it always makes a constant prediction without looking at the output
