# Idiomatic Python

import pandas as pd
import numpy as np
import timeit

df = pd.read_csv('/home/aspphem/Desktop/CSV/census.csv')
print(df.head())

# Method chaining 

# Pandorable way -- Began statement with a parenthesis, which tells Python we are going to span the statement over multiple lines for readability.

print(
(df.where(df['SUMLEV'] == 50) # filter data which has a summary level of 50
.dropna() # drop NA values
.set_index(['STNAME', 'CTYNAME']) # set multiple index; list of column names
.rename(columns={'ESTIMATEBASE2010': 'Estimates Base 2010'})) # rename column
)

# Non-pandorable way 

df = df[df['SUMLEV']==50] # overloades indexing operator [] which drops NA values
df.set_index(['STNAME', 'CTYNAME'], inplace=True) # update dataframe to have a new index
print(df.rename(columns={'ESTIMATEBASE2010': 'Estimate Base 2010'})) # set the column names

# Map 

# In applymap, you provide some function which should operate on each cell of a DataFrame, and the return set is itself a DataFrame. Also we can map all of the rows in a DataFrame through apply function.

df = pd.read_csv('/home/aspphem/Desktop/CSV/census.csv')

def min_max(row):
    data = row[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

# Then we just need to call apply on the DataFrame. Apply takes the function and the axis on which to operate as parameters. This parameter is really the parameter of the index to use. So, to apply to across all rows, which is applying on all columns, you pass axis equal to 'columns'.

results = df.apply(min_max, axis='columns').head(10)
print(results)
print(type(results))

# Add new data to the existing DataFrame; in this case you just take the row values and add in new columns indicating the max and minimum scores. 

# Bringing in data and building summary or descriptive statistics. 

def min_max(row):
    data = row[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']]
    row['max'] = np.max(data) # new entry for max
    row['min'] = np.min(data) # new entry for min
    return row
    
print(df.apply(min_max, axis='columns'))

# Apply with lambdas

rows = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']

print(df.apply(lambda x: np.max(x[rows]), axis=1).head()) # 1 is synonymous of columns; 0 is synonymous of rows

# Let's say we want to divide the states into four categories: Northeast, Midwest, South and West.

def get_state_region(x):
    northeast = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont', 'New York', 'New Jersey', 'Pennsylvania']
    midwest = ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin', 'Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']
    south = ['Delaware', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virgina', 'District of Columbia', 'West Virginia', 'Alabama', 'Kentucky', 'Mississippi', 'Tennessee', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas']
    west = ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 'Wyoming', 'Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']
    
    if x in northeast:
        return "Northeast"
    elif x in midwest:
        return "Midwest"
    elif x in south:
        return "South"
    else:
        return "West"
        
# Let's create a new column called Region, which shows the state's region, we can use the customized function and the apply function to do so. The customized function is supposed to work on the state name column STNAME. So we will set the apply function on the state name column and pass the customized function into the apply function.

df['Region'] = df['STNAME'].apply(lambda x: get_state_region(x))

print(df[['STNAME', 'Region']].head())
