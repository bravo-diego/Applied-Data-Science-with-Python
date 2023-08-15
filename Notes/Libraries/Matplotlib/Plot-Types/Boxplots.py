# Box Plots  -- method of showing aggregate statistics and various samples in a concise manner. Summarizes the distribution of your data through a visualization of what's called the five number summary (minimum and maximum values, median, first and third quartiles).

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample, 'random': random_sample, 'gamma': gamma_sample})

print(df.head())

print(df.describe())

plt.boxplot(df['normal'])
plt.show()

plt.boxplot([df['normal'], df['random'], df['gamma']], whis=[0,100])
plt.show()

plt.hist(df['gamma'], bins=100) # right skewed distribution
plt.show()

plt.figure(figsize=(9,9))
plt.boxplot([df['normal'], df['random'], df['gamma']]) # show outliers
plt.show()

# Main Figure -- Boxplot

plt.figure(figsize=(9,9)) # Size

plt.title('Boxplots in Matplotlib') # Title
plt.xlabel('Groups') # x Label
plt.ylabel('Proportion') # y Label

plt.gca().spines['top'].set_visible(False) # Get rid of chart borders
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

groups = ['Normal', 'Random', 'Gamma'] 
ax = plt.subplot()
ax.set_xticklabels(groups) # Change y tick labels

plt.boxplot([df['normal'], df['random'], df['gamma']], whis=[0,100]) # Boxplot of our three samples

# Secondary Figure -- Histogram

ax2 = plt.gca().inset_axes([0,0.6,0.4,0.4], title='Gamma Histogram', frame_on=False) # Plot on that axes a new axes object; this will be overlayed on top; bounding box of (0,0.6) as bottom left, and (0.4,0.4) as width and height

ax2.set_xticks([1.0, 2.0, 3.0], labels=None)

ax2.hist(df['gamma'], bins=100, density=True) # Plot histogram there

ax2.yaxis.tick_right() # Flip y tick labels to the right

# Show figure

plt.show()
