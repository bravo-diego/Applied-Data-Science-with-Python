# Line plots 

import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array([1,2,3,4,5,6,7,8])
exponential_data = linear_data**2

plt.figure() # create new figure and a new axis object
plt.xlabel('Some data') # set x and y labels
plt.ylabel('Some other data')
plt.title('Title')
plt.legend(['Baseline', 'Competition', 'Us']) # add a legend
plt.plot(linear_data, '-o', exponential_data, '-o') # -o means to use a solid line with circle markers; we're passing the data followed by the formatting for each series, so we'll see the result as a two data series, the linear one at the bottom and the quadratic one at the top
plt.plot([22,44,55], '--r')
plt.show()

plt.figure() 
plt.xlabel('Some data') 
plt.ylabel('Some other data')
plt.title('Title')
plt.legend(['Baseline', 'Competition', 'Us']) 
plt.plot(linear_data, '-o', exponential_data, '-o') 
plt.gca().fill_between(range(len(linear_data)), linear_data, exponential_data, facecolor='blue', alpha=0.25) # get the current axis and call fill_between(); we'll just use the same range of data point it's already using, since we didn't specify any x values in our call to plot; transparency value
plt.show()

# New Figure

plt.figure(figsize=(8,6)) # figsize parameter -- 8x6 inch figure at 300 DPI
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]') 
# arrangement of dates at daily intervals just by providing the start and end dates; numpy arange() function 
plt.plot(observation_dates, linear_data, '-o', observation_dates, exponential_data, '-o')
x = plt.gca().xaxis # variable which points at the x axis
for item in x.get_ticklabels(): # iterate trough all thick labels
    item.set_rotation(45) # rotate thick labels for the x axis
ax = plt.gca() # change labels
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title('Exponential ($x^2$) vs. Linear ($x$) performance') # matplotlib supports LaTeX math mode 
plt.show()
