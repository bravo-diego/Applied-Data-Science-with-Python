# Subplots

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure() # create a new figure

linear_data = np.array([1,2,3,4,5,6,7,8]) # data
exponential_data = linear_data**2

ax1 = plt.subplot(1, 2, 1) # subplot(rows, columns, plot number)
plt.plot(linear_data, '-o')

ax2 = plt.subplot(1, 2, 2, sharey=ax1) 
plt.plot(exponential_data, '-x')

plt.show()

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, sharex=True, sharey=True) # 3x3 grid of subplots, using tuple unpacking
ax5.plot(linear_data, '-') # plot linear_data on the 5th subplot axes
ax1.plot(exponential_data, '-o')

plt.show()

fig = plt.gcf() # get current figure
for i in range(1, 7): # iterate over 6 potential spots in our figure 
# N O T E: Matplotlib index starts at 1, NOT 0.
    if i != 5 and i != 3: # if we are at position 5 or 3, we'll leave these as holes
        ax = fig.add_subplot(2, 3, i) # plot with 2 rows and 3 columns
        ax.text(0.5, 0.2, str((i)), fontsize=18, ha='center') # add some text to the figures to make it more clear; text goes at the bottom left corner by default; relative positioning
        
plt.show()

# Data Science Visual Exploration Technique -- Scatter plot matrices (SPLOM)

# Set of visuals that look at related data but slice that data into different small visuals so that you can see both the trees and the forest all at once.

df = pd.read_csv("/home/aspphem/Desktop/CSV/iris.csv")
cols = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']

fig, axs = plt.subplots(len(cols), len(cols), figsize=(10, 10)) # 4x4 grid

for i in range(len(cols)): # iterate across each column in our data frame and compare it to each other column in our data frame
    for j in range(len(cols)):
        axs[i,j].scatter(df[cols[j]], df[cols[i]], s=5) # plot a scatter plot comparing the columns i and j; sometime this will be the same column, so we would expect to see a diagonal line trend; marker size to 5
        
        axs[i,j].get_xaxis().set_visible(False) # axis tickmarks turned off
        axs[i,j].get_yaxis().set_visible(False)

        if i == len(cols) - 1: # turn them back on only if we are the last row
            axs[i,j].get_xaxis().set_visible(True)
            axs[i,j].set_xlabel(cols[j])
            
        if j == 0: # and similarly, only show the y axis labels for the first column
            axs[i,j].get_yaxis().set_visible(True)
            axs[i,j].set_ylabel(cols[i])

plt.show()
