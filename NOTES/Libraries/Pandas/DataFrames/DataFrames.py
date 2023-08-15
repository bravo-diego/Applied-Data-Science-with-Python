# DataFrame Data Structure

# The DataFrame is a two-dimensional series object, where there is an index and multiple columns of content, which each column having a label. DataFrame itself as simply a two-axes labeled array.

import pandas as pd

record_1 = pd.Series({'Name': 'Alice', 'Class': 'Physics', 'Score': 85})

record_2 = pd.Series({'Name': 'Jack', 'Class': 'Chemistry', 'Score': 90})

record_3 = pd.Series({'Name': 'Mandy', 'Class': 'Data Science', 'Score': 50})

print(record_1)

# The DataFrame object is index. Here we use a group of series, where each series represents a row of data. 

records = pd.DataFrame([record_1, record_2, record_3], index=['student 1', 'student 2', 'student 3'])

print(records)

# An alternative method is that you could use a list of dictionaries, where each dictionary represents a row of data.

students = [{'Name': 'Robin', 'Class': 'Physics', 'Score': 100}, {'Name': 'Molly', 'Class': 'Physics', 'Score': 80}, {'Name': 'Mandy', 'Class': 'Physics', 'Score': 50}]

records_b = pd.DataFrame(students, index=['student #1', 'student #1', 'student #2'])

print(records_b)

# Similar to series, we can extract data using the .iloc and .loc attributes. Because the DataFrame is two-dimensional, passing a single value to the loc indexing operator will return the series if there is only one row to return.

# If we wanted to select data associated with student 2, we should just query the .loc attribute with one parameter.

print(records_b.loc['student #2'])

print(type(records_b.loc['student #2']))

# Indices and column names along either axes horizontal o vertical could be non-unique. In this example we see two records for student #1, if we use single value with DataFrame loc attribute multiple rows will return as a new DataFrame.

print(records_b.loc['student #1'])

print(type(records_b.loc['student #1']))

# If we wanted to just list the student names for students #1, you would supply two parameters to .loc, one being the row index and the other being the column name.

print(records_b.loc['student #1', 'Name'])

print(type(records_b.loc['student #1', 'Name']))

# iloc and loc are used for row selection, Pandas reserves the indexing operator directly on the DataFrame for column selection. In Pandas DataFrames columns always have a name, so this selection is always label based.

print(records_b['Name'])

# The result of a single column projection is a Series object.

# This also means that you get a key error if you try and use the .loc with a column name.

# print(records_b.loc['Name'])

# We can select all of the rows which related to students #1 using .loc attribute, then project the name column from just those rows.

print(records_b.loc['student #1']['Name'])

print(type(records_b.loc['student #1'])) # DataFrame
print(type(records_b.loc['student #1']['Name'])) # Series

# If we wanted to select all rows, we can use a colon to indicate a full slice from beginning to end. Then we can add a column name as the second parameter as a string. If we wanted to include multiple columns, we could do so in a list.

print(records_b.loc[:,['Name', 'Score']])

# Dropping Data

# It's easy to delete data in Series and DataFrame, and we can use the drop function to do so. This function takes a single parameter, which is the index or row label, to drop. 

# The drop function doesn't change the DataFrame by default. Instead, the drop function returns to you a copy of the DataFrame with the given rows removed.

print(records_b.drop('student #1'))

print(records_b) # Original DataFrame 

# Drop has two interesting optional parameters. The first called inplace, and if it's set to true, the DataFrame will be updated in place, instead of a copy being returned. The second parameter is the axes, which should be dropped. By default this value is 0, indicating the row axis, but you could change it to 1 if you want to drop a column.

copy_records = records_b.copy()

copy_records.drop("Name", inplace=True, axis=1) # Parameter axis=1 to tell it that this is a column.
print(copy_records)

# There is a second way to drop a column, and that's directly through the use of the indexing operator, using the del keyword.

del copy_records['Class']
print(copy_records)

# Adding Data

# Adding a new column to a DataFrame is as easy as assigning it to some value using the indexing operator.

records_b['Class Ranking'] = None
print(records_b)

df=records_b.rename(mapper=lambda x:x.upper(), axis='columns')
print(df)
