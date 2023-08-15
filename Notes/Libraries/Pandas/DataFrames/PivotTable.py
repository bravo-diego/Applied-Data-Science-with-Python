# Pivot Table

# A pivot table is a way of summarizing data in a DataFrame for a particular purpose. Is itself a DataFrame, where the rows represent one variable that you are interested in, the columns another, and the cell's some aggregate value. A pivot table tends to includes marginal values as well, which are the sums for each column and row, this allows you to be able to see the relationship between two variables at just a glance. 

import pandas as pd
import numpy as np

df = pd.read_csv('/home/aspphem/Desktop/CSV/cwurData.csv')
print(df.head())

def create_category(ranking): # since rank is just an integer, we just do a bunch of if/elif statements
    if (ranking >= 1) & (ranking <= 100):
        return "First Tier Top University"
    elif (ranking >= 101) & (ranking <= 200):
        return "Second Tier Top University"
    elif (ranking >= 201) & (ranking <= 300):
        return "Third Tier Top University"
    return "Other Top University"

df['Rank_Level'] = df['world_rank'].apply(lambda x: create_category(x)) # apply this to a single column of data to create a new series

print(df.head())

# A pivot table allows us to pivot out one of these columns a new column headers and compare it against another column as row indices. Let's say we want to compare rank level versus country of the universities and we want to compare in terms of overall score.

# We want the values to be Score; and index to be the country; and the columns to be the rank levels. Then we specify that the aggregation function, and here we need to use the NumPy mean to get the average rating for universities in that country.

print(df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean]).head()) # NaN values -- indicate that in some countries there aren't observations in one or more categories

print(df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max]).head()) 

# We can also summarize the values within a given top level column. For instance, if we want to see an overall average for the country for the mean and want to see the max of the max, we can indicate that we want pandas to provide marginal values.

print(df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max], margins=True).head()) 

# A pivot table is just a multi-level DataFrame, and we can access series or cells in the DataFrame in a similar way as we do so for a regular DataFrame. 

new_df = df.pivot_table(values='score', index='country', columns='Rank_Level', aggfunc=[np.mean, np.max], margins=True)

print(new_df.index) # index
print(new_df.columns) # columns hierarchical; top level columns indices have two categories: mean and max, and the lower level column indices have four categories, which are the four rank levels. 

print(new_df['mean']['First Tier Top University'].head()) # average scores of the First Tier Top University levels in each country
print(type(new_df['mean']['First Tier Top University'])) # Series object

print(new_df['amax']['Second Tier Top University'].head()) # max scores of the Second Tier Top University levels in each country; Series object

# What if we want to find the country that has the maximum average score on First Tier Top University level? idxmax() function.

print(new_df['mean']['First Tier Top University'].idxmax()) # idxmax() it's a built in function to the Series object

# Stack and unstack functions

# Stacking is pivoting the lowermost column index to become the innermost row index. Unstacking is the inverse of stacking, pivoting the innermost row index to become the lowermost column index.

print(new_df.head())

# Stacking -- this should move the lowermost column, so the tiers of the university rankings, to the inner most row

print("Stacking\n")
stack_df = new_df.stack() # column just transposed essentially into the rows 
print(stack_df.head())

print("Unstacking\n")
unstack_df = new_df.unstack() # unstacking all the way to just a single column (i.e. a Series object is returned)
print(unstack_df.head())
