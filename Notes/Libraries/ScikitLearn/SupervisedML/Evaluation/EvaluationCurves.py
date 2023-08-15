# Precision Recall Curves.

# Evaluation method for machine learning.

    # X-axis shows precision (i.e. fraction of positive predictions are correct)
    
        # Precision = True Positives / (True Positives + False Positives)
        
    # Y-axis shows recall (i.e. fraction of all positive instances that the classifier correctly identify as positive)

        # Recall (True Positive Rate) = True Positives / (True Positives + False Negatives)
        
# The ideal point would be precision value of 1.0 and recall value of 1.0.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression

dataset = load_digits()

X, y = dataset.data, dataset.target     

y_binary_imbalanced = y.copy()
y_binary_imbalanced[y_binary_imbalanced != 1] = 0
        
X_train, X_test, y_train, y_test = train_test_split(X, y_binary_imbalanced, random_state = 0)

lr = LogisticRegression().fit(X_train, y_train) # logistic regression classifier

y_scores_lr = lr.fit(X_train, y_train).decision_function(X_test) # decision scores
y_score_list = list(zip(y_test[0:20], y_scores_lr[0:20]))

from sklearn.metrics import precision_recall_curve

precision, recall, thresholds = precision_recall_curve(y_test, y_scores_lr)
closest_zero = np.argmin(np.abs(thresholds))
closest_zero_p = precision[closest_zero]
closest_zero_r = recall[closest_zero]

plt.figure()
plt.xlim([0.0, 1.01])
plt.ylim([0.0, 1.01])
plt.plot(precision, recall, label = 'Precision-Recall Curve')
plt.plot(closest_zero_p, closest_zero_r, 'o', markersize = 12, fillstyle = 'none', c = 'r', mew = 3)
plt.xlabel('Precision', fontsize = 16)
plt.ylabel('Recall', fontsize = 16)
plt.axes().set_aspect('equal')
plt.show()

# Receiver Operating Characteristic Curves.

# Visualization method that illustrate the performance of a binary classifier.

    # X-axis shows false positive rate (i.e. Specificity)
    
    # Y-axis shows true positive rate (i.e. recall)

# The ideal point is a false positive rate of 0.0 and a true positive rate of 1.0; i.e. a goof ROC curve maximize the true positive rate while minimizing the false positive rate.

# We can quantify the goodness of a classifier by looking at how much area there is underneath the ROC curve (Area Under the Curve; AUC). An AUC of zero represents a very bad classifier, while an AUC of one represents a good classifier.

from sklearn.metrics import roc_curve, auc

fpr_lr, tpr_lr, _ = roc_curve(y_test, y_scores_lr)
roc_auc_lr = auc(fpr_lr, tpr_lr)

plt.figure()
plt.xlim([-0.1, 1.01])
plt.ylim([-0.1, 1.01])
plt.plot(fpr_lr, tpr_lr, lw = 3, label = 'LogRegr ROC Curve (area = {:0.2f})'.format(roc_auc_lr))
plt.xlabel('False Positive Rate', fontsize = 16)
plt.ylabel('True Positive Rate', fontsize = 16)
plt.legend(loc = 'lower right', fontsize = 13)
plt.plot([0, 1], [0, 1], color = 'navy', lw = 3, linestyle = '--')
plt.axes().set_aspect('equal')
plt.show()

# Advantages.

    # AUC gives a single number for easy comparison and does not require a specifying a decision threshold; summarizes an ROC curve in one number.

# Disadvantages.

    # AUC loses information about the shape of the curve, this may be a factor to consider when wanting to compare the performance of classifiers with overlapping ROC curves.
