# Multi-Class Evaluation.

# Multi-class evaluation is an extension of the binary case.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

dataset = load_digits()
X, y = dataset.data, dataset.target
X_train_mc, X_test_mc, y_train_mc, y_test_mc = train_test_split(X, y, random_state = 0)

svm = SVC(kernel = 'linear').fit(X_train_mc, y_train_mc)
svm_predicted_mc = svm.predict(X_test_mc)
confusion_mc = confusion_matrix(y_test_mc, svm_predicted_mc)
df_cm = pd.DataFrame(confusion_mc, index = [i for i in range(0, 10)], columns = [i for i in range(0, 10)])

plt.figure(figsize = (5.5, 4))
sns.heatmap(df_cm, annot = True)
plt.title('SVM Linear Kernel \n Accuracy: {0:.3f}'.format(accuracy_score(y_test_mc, svm_predicted_mc)))

plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show() # looking at the confusion matrix to get some insight into what errors that is making for each class

svm = SVC(kernel = 'rbf').fit(X_train_mc, y_train_mc)
svm_predicted_mc = svm.predict(X_test_mc)
confusion_mc = confusion_matrix(y_test_mc, svm_predicted_mc)
df_cm = pd.DataFrame(confusion_mc, index = [i for i in range(0, 10)], columns = [i for i in range(0, 10)])

plt.figure(figsize = (5.5, 4))
sns.heatmap(df_cm, annot = True)
plt.title('SVM RBF Kernel \n Accuracy: {0:3f}'.format(accuracy_score(y_test_mc, svm_predicted_mc)))

plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()

print(classification_report(y_test_mc, svm_predicted_mc)) # summarizes multiple evaluation metrics for a multi-class classifier with an average metric computed for each class
