# Bar charts

import matplotlib.pyplot as plt
import numpy as np
from random import randint

linear_data = np.array([1,2,3,4,5,6,7,8])

xvals = range(len(linear_data)) # values along x axis

new_xvals = []
exponential_data = linear_data**2

for item in xvals:
    new_xvals.append(item+0.3) # adjust x values to make up for the first set of bars plotted

plt.bar(xvals, linear_data, width = 0.3) # first bar
plt.bar(new_xvals, exponential_data, width = 0.3, color='red') # second bar
plt.show()

linear_err = [randint(1,4) for x in range(len(linear_data))]# error bars
plt.bar(xvals, linear_data, width= 0.3, yerr=linear_err) 
plt.show()

xvals = range(len(linear_data)) # x values are the same for both bars (x values superposed); bottom parameter specifies which column is at the bottom
plt.bar(xvals, linear_data, width = 0.3, bottom = exponential_data, color='b') 
plt.bar(xvals, exponential_data, width = 0.3, color='r')
plt.show()

xvals = range(len(linear_data)) # barh() function switch to horizontal bar charts
plt.barh(xvals, linear_data, height = 0.3, color='b')
plt.barh(new_xvals, exponential_data, height = 0.3, color='r')
plt.show()


