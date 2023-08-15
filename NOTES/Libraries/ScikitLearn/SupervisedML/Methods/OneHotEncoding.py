# One-Hot Encoding.

# Problem: Some variables (features, labels) are categories, not numbers; many predictors cannot take categorical input directly (least squares linear regression, logistic regression, support vector machines), but some can (decision trees).

# Sometimes these categories are encoded as numbers (e.g. red = 1; yellow = 2, etc.).

# One-Hot Encoding turns a single categorical value into a vector of 0/1 values (one column per possible category); exactly one columns is 1 (selected category), the rest are 0.

# Using 1-hot encoding whit Pandas.

import pandas as pd

s = pd.Series(list('abcadb'))
encoding = pd.get_dummies(s) # in statistics is called dummy encoding or 1 of k encoding
print(encoding)

# Using 1-hot encoding with SciKit-Learn

from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown='ignore') # create an object
X = [['Male', 1], ['Female', 3], ['Female', 2]]
print(enc.fit(X))
print(enc.categories_) # what categories did you find in our data? returns categories and unique values
print(enc.transform([['Female', 1], ['Male', 4]]).toarray())

# Applying 1-hot encoding.

    # Always split the training and test sets first before fitting.
    
    # Fit the One Hot Encoder using the training data.
    
    # Use transform to apply this same One Hot Encoder to both training and test data. This ensures that dummy variables match across train and test data; All categories are represented.
    
        # What if test set has extra categories not seen during training?
            
            # Map these to a special other category.
            
            # Ignore them and allow an all-zero 1-hot vector.
    
