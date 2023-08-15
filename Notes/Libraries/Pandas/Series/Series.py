# Introduction to Pandas 

import pandas as pd

import numpy as np

# Easiest way to create a series is to use an array-like object, like a list

students = ['Alice', 'Jack', 'Molly']

print(pd.Series(students))

# The result is a series object, Pandas automatically identified the type of data in this series as object. Values are indexed with integers. starting with 0.

numbers = [1, 2, 3]

print(pd.Series(numbers))

# The result is a dtype of int64 objects -- INT64 stands for 64 bit integer. The 64 refers to the memory allocated to store data in each cell wich effectively relates how many digits it can store in each cell.

students_b = ['Alice', 'Jack', None]

print(pd.Series(students_b))

# If we have one element, o None type, Pandas inserts it as a None and uses th etype object for the underlying array.

numbers_b = [1, 2, None]

print(pd.Series(numbers_b))

# If we have a None type element in a list of numbers, integers or floats, Pandas automatically converts this to a special floating point values designated as NaN (Not a Number). Pandas set the dtype of this series to floating point numbers instead of object or int; Pandas represents NaN as a floating point number, in that way Pandas went and converted our integers to floats.

# None and NaN might be used in the same way, to denote missing data. But these are NOT represented by Pandas in the same way.

# NaN is *NOT equivalent to None

print(np.nan == None)

print(np.isnan(np.nan))

# Special function to test for the presence of not a number. NaN it's meaning is similar to None, but it's a numeric value and treated differently.

students_scores = {'Alice': 'Physics', 'Jack': 'Chemistry', 'Molly': 'English'}

s = pd.Series(students_scores)

print(s)

print(s.index)

# First column is a list of strings

students_c = [("Alice", "Brown"), ("Jack", "White"), ("Molly", "Green")]

print(pd.Series(students_c))

# Each of tuples is stored in the series object, and the type is object

# We can also separate your index creation from the data by passing in the index as a list explicitly to the series

students_scores_b = pd.Series(['Physics', 'Chemistry' , 'English'], index=['Alice', 'Jack', 'Molly'])

r = pd.Series(students_scores, index=['Alice', 'Molly', 'Sam'])
print(r)

# The result is a Series object doesn't have Jack in it, even though he was in our original dataset, but is explicitly does have Sam in it as a missing value.
