# Histograms -- bar chart where the x axis is a given observation and the y axis is the frequency for which that observation occurs.

import matplotlib.pyplot as plt
import numpy as np

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True) # 2 x 2 grid of axis objects; sharing x axis between plots
axs = [ax1, ax2, ax3, ax4] 

for n in range(0, len(axs)): # iterate through each axis
    sample_size = 10**(n+1) # 10, 100, 1000, 10000 
    sample = np.random.normal(loc=0.0, scale=1.0, size=sample_size)
    axs[n].hist(sample) # plot that sample; by default Matplotlib uses 10 bins and that's 10 different bars
    axs[n].set_title(f'n={sample_size}')
    
plt.show() # N O T E -- for n equals 10,000 many values have to be combined into a single bin (10 bins by default); bars of n equals 10,000 are actually wider than those of the 10 or 100 plots

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True) 
axs = [ax1, ax2, ax3, ax4] 

for n in range(0, len(axs)):
    sample_size = 10**(n+1) 
    sample = np.random.normal(loc=0.0, scale=1.0, size=sample_size)
    axs[n].hist(sample, bins=100) # 100 bins along the axis
    axs[n].set_title(f'n={sample_size}')
    
plt.show() # N O T E -- How many bins should I plot when using a histogram? Both of these plots are true; when we look at the finest grain granularity in our data plotting with 10,000 bins, then the histogram becomes useless for decision-making since they are not showing any trend between samples as much as they are just actually showing the sample sizes themselves

Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)
plt.scatter(X,Y)
plt.show()

import matplotlib.gridspec as gridspec
plt.figure(figsize=(10,10))
gspec = gridspec.GridSpec(3,3)

top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:, 0])
lower_right = plt.subplot(gspec[1:, 1:])

plt.show()

# data
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)

# figure and gridspec
plt.figure(figsize=(10,10))
gspec = gridspec.GridSpec(3,3)

# subplots all spec'ed out
top_histogram = plt.subplot(gspec[0, 1:])
side_histogram = plt.subplot(gspec[1:, 0])
lower_right = plt.subplot(gspec[1:, 1:])

# data plotted in each subplot
top_histogram.hist(X, bins=100)
side_histogram.hist(Y, bins=100, orientation='horizontal')
lower_right.scatter(X,Y)

# flip the side histogram's x axis
side_histogram.invert_xaxis()


# change axes limits to get rid of whitespace
for ax in [top_histogram, lower_right]:
    ax.set_xlim(0,1)
for ax in [side_histogram, lower_right]:
    ax.set_ylim(-5,5)

plt.show() # two different distributions

# SELECTING THE NUMBER OF BINS IN A HISTOGRAM

#  Smoother densities require less bins in their histogram estimates than rougher densities

