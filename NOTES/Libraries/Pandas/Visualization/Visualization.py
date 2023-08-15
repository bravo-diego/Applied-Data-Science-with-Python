# Visualization in Pandas 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('seaborn-colorblind') # color palette more color vision deficiency friendly 

np.random.seed(123)

df = pd.DataFrame({'A': np.random.randn(365).cumsum(0), 'B': np.random.randn(365).cumsum(0) + 20, 'C': np.random.randn(365).cumsum(0) - 20}, index=pd.date_range('1/1/2017', periods=365))

print(df.head())

df.plot()
plt.show()

df.plot('A', 'B', kind = 'scatter')
plt.show()

df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis') # color c; size s to change based on the value of column B
plt.show()

ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')
plt.show()

df.plot.box() # box plots 
plt.show()

df.plot.hist(alpha=0.7) # histograms
plt.show()

df.plot.kde() # kernel density estimation plots
plt.show()

# Pandas Tools Plotting

iris = pd.read_csv('/home/aspphem/Desktop/CSV/iris.csv')
print(iris.head())

# Scatter matrix -- way of comparing each column in a data frame to every other column in a pairwise fashion; creates scatter plots between the different variables and histograms along the diagonals

pd.plotting.scatter_matrix(iris) # allows us to quickly see some of the more obvious patterns in the data set
plt.show()

plt.figure()
pd.plotting.parallel_coordinates(iris, 'Name')
plt.show()




