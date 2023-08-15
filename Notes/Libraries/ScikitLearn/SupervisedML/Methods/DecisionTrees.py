# Decision Trees.

# Supervised Learning Method; can be used for both regression and classification. Basically, decision trees learn a series of explicit if then rules on feature values that result in a decision that predicts the target value.

# Supervised algorithms learn and figure out all these rules to get an accurate decision quickly.

# Build a Decision Tree.

    # To build a decision tree, the algorithm starts by finding the FEATURE that leads to the **most informative split.
    
        # We can further improve the accuracy of the classification by continuing this process of finding the best split for the remaining subsets.
        
        # We continue with this process recursively until we are left with data points in the decision tree that all have the same or at least a predominant majority of a target value (class).
        
# Trees whose leaf nodes each have all the same target value are called pure; as opposed to mixed where the leaf nodes are allowed to contain at least some mixture of the classes.

# Decision trees can also be used for regression using the same process of testing the feature values at each node and predicting the target value based on the contents of the leaf node.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state = 3)

clf = DecisionTreeClassifier().fit(X_train, y_train)

print("Accuracy of Decision Tree Classifier on Training Set: {:.2f}".format(clf.score(X_train, y_train))) # accuracy of 1.0

print("Accuracy of Decision Tree Classifier on Test Set: {:.2f}".format(clf.score(x_test, y_test))) # accuracy of 0.97; indicates tree is likely overfitting 

print("Feature Importances: {}".format(clf.feature_importances_))

# One strategy to prevent overfitting is to prevent the tree from becoming really detailed and complex by stopping its growth early; this is called pre-pruning. 

    # Scikit-Learn only implements pre-pruning; we can control tree complexity via pruning by limiting either the maximum depth of the tree using max_depth parameter or the maximum number of leaf nodes using the max_leaf_nodes parameter.

# Another strategy is to build a complete tree with pure leaves but then to prune back the tree into a simpler form; this is called post-pruning or just pruning.

clf2 = DecisionTreeClassifier(max_depth = 3).fit(X_train, y_train)

print("Accuracy of Decision Tree Classifier on Training Set: {:.2f}".format(clf2.score(X_train, y_train))) # accuracy of 0.98; now the accuracy on the training data is slightly worse but the accuracy on the test data is slightly better

print("Accuracy of Decision Tree Classifier on Test Set: {:.2f}".format(clf2.score(x_test, y_test))) # accuracy of 0.97

# Feature Important Calculation.

# Summary Analysis you can perform on a supervised learning model. Feature importance is typically a number between 0 and 1 that is assigned to an individual feature. It indicates how important that feature is to the overall prediction accuracy.

    # Feature importance of 0 indicates the feature was NOT used in prediction.
    
    # Feature importance of 1 indicates the feature predicts the target perfectly.
    
        # All feature importances are normalized to sum to 1.0.
        
print("Feature Importances: {}".format(clf2.feature_importances_))

cancer = load_breast_cancer()
(X_cancer, y_cancer) = load_breast_cancer(return_X_y = True)

X_train, X_test, y_train, y_test = train_test_split(X_cancer, y_cancer, random_state=0)

clf3 = DecisionTreeClassifier(max_depth = 4, min_samples_leaf = 8, random_state = 0).fit(X_train, y_train) # max_depth controls maximum depth (number of split points); min_samples_leaf threshold for the minimum number of data instances a leaf can have to avoid further splitting; max_leaf_nodes limits total number of leaves in the tree

# In practice adjusting only one of these parameters is enough to reduce overfitting.

print("Accuracy of Decision Tree Classifier on Training Set: {:.2f}".format(clf3.score(X_train, y_train))) 

print("Accuracy of Decision Tree Classifier on Test Set: {:.2f}".format(clf3.score(X_test, y_test))) 

print("Feature Importances: {}".format(clf3.feature_importances_))

# Pros -- Decision tree rules are easily to be interpreted and visualized; no feature normalization or scaling typically needed; working well with data sets using a mixture of feature types (continuous, categorical, binary)

# Cons -- Even after tuning, decision trees can often still overfit.
