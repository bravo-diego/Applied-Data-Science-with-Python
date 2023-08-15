# Ridge Regression.

# Ridge regression learns w and b using the same least-squares criterion but adds a penalty for large variations in w parameters (regularization); that prevents overfitting by restricting the model, typically to reduce the complexity of the final estimated model.

# Ridge regression uses L2 regularization: minimize sum of squares of w entries. The influence of the regularization term is controlled by the alpha parameter; higher alpha means more regularization and simpler models. Default value of alpha is 1.0; value of alpha 0 means the ordinary least squares linear regression.

# Once the parameters are learned, the ridge regression prediction formula is the same as ordinary least-squares.

import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

crime = pd.read_table('/home/aspphem/Desktop/Files/TXT/CommViolPredUnnormalizedData.txt', sep=',', na_values='?')

columns_to_keep = [5, 6] + list(range(11, 26)) + list(range(32, 103)) + [145]
crime = crime.iloc[:, columns_to_keep].dropna()

X_crime = crime.iloc[:, range(0, 88)]
y_crime = crime['ViolentCrimesPerPop']

X_train, X_test, y_train, y_test = train_test_split(X_crime, y_crime, random_state=0)

linridge = Ridge(alpha=20.0).fit(X_train, y_train) # regularization penalty L2

print('Crime Dataset')
print('Ridge Regression Linear Model Intercept: {}'.format(linridge.intercept_))
print('Ridge Regression Linear Model Coeff:\n{}'.format(linridge.coef_))
print('R-squared score (training): {:.3f}'.format(linridge.score(X_train, y_train)))
print('R-squared score (test): {:.3f}'.format(linridge.score(X_test, y_test)))
print('Number of non-zero features: {}'.format(np.sum(linridge.coef_ != 0)))

# Pre-processing and Normalization.

# Ridge regression regularizes the linear regression by imposing that sum of the squares penalty on the size of the w coefficients. But if the input variables, the features have very different scales, then when this shrinkage happens of the coefficients, input variables with different scales will have different contributions to this L2 penalty. So transforming the input features, so they are on the same scale, means the rich penalty is in some sense applied more fairly to all features.

# Normalization is so important for some ML methods that all features are on the same scale.

    # 'MinMaxScaler' Scaling.
    
scaler = MinMaxScaler()
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train) # scaled version of the input data; 
X_test_scaled = scaler.transform(X_test)

# N O T E: We are applying the same scalar object to both the training and the test data; we are training the scalar object on the training data and not on the test data

# If we use different scalers this could lead to random skew in the data

clf = Ridge().fit(X_train_scaled, y_train)
r2_score = clf.score(X_test_scaled, y_test)

linridge = Ridge(alpha=20.0).fit(X_train_scaled, y_train) # regularization penalty L2

print('Crime Dataset')
print('Ridge Regression Linear Model Intercept: {}'.format(linridge.intercept_))
print('Ridge Regression Linear Model Coeff:\n{}'.format(linridge.coef_))
print('R-squared score (training): {:.3f}'.format(linridge.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'.format(linridge.score(X_test_scaled, y_test)))
print('Number of non-zero features: {}'.format(np.sum(linridge.coef_ != 0)))

# In general regularization works especially well when you have relatively small amounts of training data compared to the number of features in your model.

# Lasso Regression.

# Lasso regression is another form of regularized linear regression that uses an L1 regularization penalty for training; instead of ridge's L2 penalty.

# When to use ridge or lasso regression:

    # Many small/medium sized effects: Ridge regression
    
    # Only a few variables with medium/large effect: Lasso regression
    
X_train, X_test, y_train, y_test = train_test_split(X_crime, y_crime, random_state=0)
    
scaler = MinMaxScaler()
scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train) # scaled version of the input data; 
X_test_scaled = scaler.transform(X_test)

linlasso = Lasso(alpha=2.0, max_iter = 10000).fit(X_train_scaled, y_train)

print('Crime Dataset')
print('Lasso Regression Linear Model Intercept: {}'.format(linlasso.intercept_))
print('Lasso Regression Linear Model Coeff:\n{}'.format(linlasso.coef_))
print('Non-zero features: {}'.format(np.sum(linlasso.coef_ != 0)))
print('R-squared score (training): {:.3f}'.format(linlasso.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'.format(linlasso.score(X_test_scaled, y_test)))
print('Features with non-zero (sorted by absolute magnitude):')

for e in sorted (list(zip(list(X_crime), linlasso.coef_)), key = lambda e: -abs(e[1])):
    
    if e[1] !=0:
        print('\t{}, {:.3f}'.format(e[0], e[1]))
        


