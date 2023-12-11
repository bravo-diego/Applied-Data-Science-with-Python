# Ferreira, N., Fisher, D., & Konig, A. C. (2014, April). Sample-oriented task-driven visualizations: allowing users to make better, more confident decisions. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 571-580). ACM. 

# In this paper the authors describe the challenges users face when trying to make judgements about probabilistic data generated through samples. As an example, they look at a bar chart of four years of data (replicated below in Figure 1). Each year has a y-axis value, which is derived from a sample of a larger dataset. For instance, the first value might be the number votes in a given district or riding for 1992, with the average being around 33,000. On top of this is plotted the 95% confidence interval for the mean (see the boxplot lectures for more information, and the yerr parameter of barcharts).

# A challenge that users face is that, for a given y-axis value (e.g. 42,000), it is difficult to know which x-axis values are most likely to be representative, because the confidence levels overlap and their distributions are different (the lengths of the confidence interval bars are unequal). One of the solutions the authors propose for this problem (Figure 2c) is to allow users to indicate the y-axis value of interest (e.g. 42,000) and then draw a horizontal line and color bars based on this value. So bars might be colored red if they are definitely above this value (given the confidence interval), blue if they are definitely below this value, or white if they contain this value.

# Implement the bar coloring as described above - a color scale with at least three colors, (e.g. blue, white, and red). Assume the user provides the y axis value of interest as a parameter or variable.
	
	# Loading libraries

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import math 

	# Use the following data for this assignment

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000, 3650), np.random.normal(43000,100000, 3650), np.random.normal(43500,140000, 3650), np.random.normal(48000,700000, 3650)], index=[1992, 1993, 1994, 1995])

print(df)

df = df.transpose()
print(df.describe())

	# Implementing the easiest option 

mean = list(df.mean())
std = list(df.std())

ye1 = []

for i in range(4):
    ye1.append(1.96*(std[i]/math.sqrt(len(df))))
    
print(ye1)

nearest = 100
Y = 39500

df_p = pd.DataFrame()
df_p['diff'] = nearest*((Y - df.mean())//nearest)
df_p['sign'] = df_p['diff'].abs()/df_p['diff']
old_range = abs(df_p['diff']).min(), df_p['diff'].abs().max()
new_range = .5,1
df_p['shade'] = df_p['sign']*np.interp(df_p['diff'].abs(), old_range, new_range)

shade = list(df_p['shade'])
blues = cm.Blues
reds = cm.Reds
color = ['White' if x == 0 else reds(abs(x)) if x<0 else blues(abs(x)) for x in shade]

plt.figure(num=None, figsize=(6,6), dpi=80, facecolor='w', edgecolor='k')
plt.bar(range(len(df.columns)), height = df.values.mean(axis = 0), yerr=ye1, error_kw={'capsize': 10, 'elinewidth': 2, 'alpha':0.7}, color=color)
plt.axhline(y=Y, color='black', label = 'Y')
plt.text(3.5, 40000, "39500")
plt.xticks(range(len(df.columns)), df.columns)
plt.title('Data Between 1992 - 1995')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
    
plt.show()
