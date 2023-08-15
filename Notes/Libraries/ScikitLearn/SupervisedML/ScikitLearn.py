# An Example Machine Learning Problem

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap, BoundaryNorm

fruits = pd.read_table('/home/aspphem/Desktop/Files/TXT/fruit_data_with_colors.txt') 
# data frame variable

print(fruits.head(3), fruits.shape, "\n", fruits.keys()) # (59 rows, 7 columns) rows corresponds to different pieces of fruit; color_score captures the idea of the color of the fruit; red 0.85-1.00; orange 0.75-0.85 ...

lookup_fruit_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))
print(lookup_fruit_name)

# If we use one of our labeled fruit examples in the data that we use to train the classifier, we can also use that same fruit sample later as a test sample to it also evaluate the classifier.

# To estimate how well the classifier will do on future samples, what we'll do is split the original data set into two parts; 

    # array of labeled samples called the training data set that will be used to train the classifier; remaining labeled samples in a second array called test set, used to evaluate the trained classifier

X = fruits[['height', 'width', 'mass', 'color_score']] # rows of the data without label
y = fruits['fruit_label'] # labels for those rows

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.75, test_size = 0.25, random_state=0) # default values of test and train sizes are None values; so function splits the data set in 75-25 proportion; random state parameter provides a seed value to the function's internal random number generator. So if we want to get the same training and test split each time we just make sure to pass in the same value of the random state parameter

print(X_train.head(3), X_train.shape)
print(X_test.head(3), X_test.shape)

print(y_train.head(3), y_train.shape)
print(y_test.head(3), y_test.shape)

# Plotting a scatter matrix

cmap = cm.get_cmap('gnuplot')
scatter = pd.plotting.scatter_matrix(X_train, c = y_train, marker = 'o', s = 40, hist_kwds={'bins': 15}, figsize=(12,12), cmap=cmap) 

plt.show() # looking at the plot, we can see that some pairs of features like height and color score (top right corner) are good for separating out different classes of fruit;

# Classifier that was trained using those features could likely learn to classify the various fruit types well

# Plotting a 3D scatter plot

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X_train['width'], X_train['height'], X_train['color_score'], c = y_train, marker = 'o', s = 100)
ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('Color Score')

plt.show() # we can clearly see that the different fruit types are in pretty well-defined clusters that are also well-separated in feature space

# K-nearest neighbors (K-NN Classifiers)

# K-nearest neighbors algorithm can be used for classification and regression. K-NN classifiers are an example of what's called instance based or memory based supervised learning (i.e. learning methods work by memorizing the labels examples they see in the training set and then they use those memorized examples to classify new objects later).

# The K in K-NN refers to the number of nearest neighbors the classifier will retrieve and use in order to make its prediction.

# Given a training set X_train with labels y_train and given a new instance x_test to be classified:

    # Find the most similar instances (let's called them X_NN) to x_test that are in X_train; classifier will look into its set of memorized training examples to find the K examples that have the closes features
    
    # Get labels y_NN for the instances in X_NN; classifier will look up the class labels for those K-nearest neighbor examples

    # Predict the label for x_test by combining the labels y_NN by simple majority vote; combine the labels of those examples to make a prediction for the label of the new object
    
# A nearest neighbor algorithm need four thing specified:

    # A distance metric; (e.g. Euclidean distance to measure distance between points)
    
    # How many nearest neighbors to look at; (usually an odd number)
    
    # Optional weighting function on the neighbor points; (some neighbors will have more influence on the outcome)
    
    # Method for aggregating the classes of neighbor points; (how combine the labels of k-neighbors to produce the final prediction (e.g. simple majority vote))
    
X = fruits[['mass', 'width', 'height']] # rows of the data without label
y = fruits['fruit_label'] # labels for those rows

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

knn = KNeighborsClassifier(n_neighbors = 5) # create a classifier object

knn.fit(X_train, y_train) # train the classifier (fit the estimator) using the training data

print(knn.score(X_test, y_test))

fruit_prediction = knn.predict([[20, 4.3, 5.5]])
print(lookup_fruit_name[fruit_prediction[0]])

fruit_prediction = knn.predict([[100, 6.3, 8.5]])
print(lookup_fruit_name[fruit_prediction[0]])

def plot_fruit_knn(X, y, n_neighbors, weights):
    X_mat = X[['height', 'width']].values
    y_mat = y.values

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF', '#AFAFAF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF', '#AFAFAF'])
    clf = KNeighborsClassifier(n_neighbors, weights = weights)
    clf.fit(X_mat, y_mat)

    mesh_step_size = 0.1
    plot_symbol_size = 50

    x_min, x_max = X_mat[:, 0].min() - 1, X_mat[:, 0].max() + 1 
    y_min, y_max = X_mat[:, 1].min() - 1, X_mat[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, mesh_step_size), np.arange(y_min, y_max, mesh_step_size))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)

    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap = cmap_light)

    plt.scatter(X_mat[:, 0], X_mat[:, 1], s = plot_symbol_size, c = y, cmap = cmap_bold, edgecolor = 'black')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    patch0 = mpatches.Patch(color = '#FF0000', label = 'apple')
    patch1 = mpatches.Patch(color = '#00FF00', label = 'mandarin')
    patch2 = mpatches.Patch(color = '#0000FF', label = 'orange')    
    patch3 = mpatches.Patch(color = '#AFAFAF', label = 'lemon')
    plt.legend(handles=[patch0, patch1, patch2, patch3])

    plt.xlabel('height (cm)')
    plt.ylabel('width (cm)')

    plt.show()
    
plot_fruit_knn(X_train, y_train, 1, 'uniform') # when K = 1, prediction is sensitive to noise, outliers, mislabeled data and other sources of variation in individual data points

plot_fruit_knn(X_train, y_train, 5, 'uniform') # for larger values of K the areas assigned to different classes are smoother and not as fragmented, and more robust to noise in the individual points, but possibly with some mistakes, more mistakes in individual points

# How the value of K affects the accuracy of the classifier?

k_range = range(1, 20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))
    
plt.figure()
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.scatter(k_range, scores)
plt.xticks([0, 5, 10, 15, 20])
plt.show() # larger values of K lead to worse accuracy for this particular data set; results for this particular test split
