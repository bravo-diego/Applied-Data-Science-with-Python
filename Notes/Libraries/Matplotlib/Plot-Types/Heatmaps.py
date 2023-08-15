# Heatmaps -- heat maps are a way to visualize three dimensions of data (e.g. weather data: latitude, longitude, temperature -- three dimensions).

# In matplotlib a heat map is simply a two-dimensional histogram where the x and y values indicate potential points and the color plotted is the frequency of the observation.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

df = pd.read_csv("/home/aspphem/Desktop/CSV/NYC hourly traffic.csv")
df['Date'] = df['Date'].apply(pd.to_datetime)
print(df.head())

sample = df[(df['Plaza ID'] == 5) & (df['Date'] > '2016-12-30') & (df['Date'] < '2017-05-01')] # boolean masking method; multiple conditions
print(sample)

# Alternative way to query a data frame, it uses a library called numexpr; takes a query as a string and apply it to the data frame (it's a bite like SQL syntax)

    # sample = df.query("`Plaza ID`==5 & Date>'2016-12-30' & Date<'2017-05-01'") 

plt.hist(sample['Hour'], bins=24, weights=sample['# Vehicles - E-ZPass']) # since we have 24 hours in a day I'll set the bins there, and I want to see our frequency -- the weights for each bin -- as the number of vehicles which have the E-ZPass system
plt.show()

sample['Day of Week'] = sample['Date'].dt.dayofweek # series objects in Pandas has an attribute 'dt' which stores numerous data time transformations; in this case we just take the Date column (series object) and extract the day of the weel
plt.hist(sample['Day of Week'], bins=7, weights=sample['# Vehicles - E-ZPass'])


plt.figure(figsize=(12,8)) # figure size
plt.hist2d(sample['Hour'], sample['Day of Week'], bins=[24,7], weights=sample['# Vehicles - E-ZPass']) # we need to set one variable to be the x-axis, another to be the y-axis and then we render our frequency, our weights using different colors showing this third dimension; we specify the bin size for each axis [24, 7] = [hours, days]; 

plt.colorbar() # adds a legend telling the value of each bin (cell) in the histogram
plt.show()
