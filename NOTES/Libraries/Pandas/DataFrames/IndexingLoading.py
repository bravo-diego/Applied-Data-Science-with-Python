# Data Frame Indexing and Loading

import pandas as pd

df = pd.read_csv('/home/aspphem/Desktop/CSV/Admission_Predict.csv')

print(df.head())

# By default index starts with 0 while students serial number starts from 1. If you jump back to the CSV output you'll deduce that Pandas has create a new index.

# We can set the serial number as the index if we want to by using the index_col.

df_2 = pd.read_csv('/home/aspphem/Desktop/CSV/Admission_Predict.csv', index_col = 0)

print(df_2.head())

# We have two columns 'SOP' and 'LOR' and probably not everyone knows what they mean. So let's change our column names to make it more clear. 

# In Pandas we can use the rename() function. It makes a parameter called columns, and we need to pass into a dictionary which the keys are the old column name and the value is the corresponding new column name.

new_df = df_2.rename(columns={'GRE Score':'GRE Score', 'TOEFL Score':'TOEFL Score', 'University Rating':'University Rating', 'SOP':'Statement of Purpose', 'LOR':'Letter of Recommendation', 'CGPA':'CGPA', 'Research':'Research', 'Chance of Admit':'Chacne of Admit'})

print(new_df.head())

print(new_df.columns)

# There is actually a space right after 'LOR'. For this reason our rename dictionary does not work for 'LOR'. 

# One way would be change a column by including the space in the name

updated_df = new_df.rename(columns={'LOR ': 'Letter of Recomendation'})
print(updated_df.columns)

# Python comes with a handy string function to strip white space called strip(). when we pass this in to rename we pass the function as the mapper parameter, and then indicate whether the axis should be columns or index (row labels)

trimmed_df = updated_df.rename(mapper=str.strip, axis='columns')
print(trimmed_df.columns)

# Note: Remember though that rename function is not modifying the original data frame.

# We can also use the df.columns attribute by assigning to it a list of column names which will directly rename the columns. This will directly modify the original dataframe and is very efficient especially when you have a lot of columns and you only want to change a few.

cols = list(df_2.columns)

cols = [x.lower().strip() for x in cols]

df_2.columns = cols

print(df_2.head())
print(df_2.columns)
