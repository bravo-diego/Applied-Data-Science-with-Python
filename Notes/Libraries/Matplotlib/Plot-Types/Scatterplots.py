# Scatterplots -- Two dimensional plot, takes an x-axis value as the first argument and a y-axis value as the second.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

plt.figure() # new figure
plt.scatter(x,y) # similar to plt.plot(x, y, '.')
plt.show()

x = np.array([1,2,3,4,5,6,7,8])
y = x

colors = ['green']*(len(x)-1) # list of colors for each point to have
colors.append('red') # ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'red',]  

plt.figure # new figure
plt.scatter(x, y, s=100, c=colors) # point with size 100 and chosen color list
plt.show() 

zip_generator = zip([1,2,3,4,5], [6,7,8,9,10]) # zip convert two lists into a list of pairwise tuples
print(list(zip_generator))

zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
print(*zip_generator) # single star * unpacks a collection into positional arguments

x = np.array([1,2,3,4,5,6,7,8])
y = x

plt.figure() # new figure
plt.scatter(x[:2], y[:2], s=100, c='red', label='Tall students') # first two elements of x and y
plt.scatter(x[2:], y[2:], s=100, c='blue', label='Short students') # last two elements of x and y
plt.xlabel('Number of times the child kicked the ball') # label to x axis
plt.ylabel('Grade of student') # label to y axis
plt.title('Relationship between ball kicking and grades') # title
plt.legend(loc=4, frameon=False, title='Legend') # add a legend
plt.show()




