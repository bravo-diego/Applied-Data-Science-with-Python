# Animation

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n = 100
x = np.random.randn(n)

def update(curr): # function that will do the plotting; curr is the current frame -- integer value starting at zero
    if curr == n: # check if the animation is the last frame, and if so, stop the animation a 
        a.event_source.stop() # a it's an object that we'll define later; we can still acces it since python allows us to access variables in the global scope
        
plt.cla() # clear the current access

bins = np.arange(-4, 4, 0.5) # set bins 

plt.hist(x[:curr], bins=bins) # plot a histogram using the current frame number which was passed into the function and out global values array

plt.axis([-4,4,0,30]) # set axes limits

plt.gca().set_title('Sampling the Normal Distribution')
plt.gca().set_ylabel('Frequency')
plt.gca().set_xlabel('Value')
plt.annotate('n = {}'.format(curr), [3,27])

a = animation.FuncAnimation(plt.figure(), update, interval=100) # assign FuncAnimation constructor to a variable a; first parameter is the figure that we're working with, the second parameter the name of our function, and the third parameter the amount of time we want between updates (100 milliseconds)

plt.show()
