# Introduction to Pandas

# To use pandas, you'll typically start with the following line of code:

import pandas as pd

# There are two core objects in Pandas: DataFrame and Series.

print("DataFrame\n")

# A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.

NY = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(NY, "\n", type(NY), "\n")

# DataFrames entries are not limited to integers. For instance, here's a DataFrame whose values are strings:

NA = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Good.', 'Bland']}, index=['Pizza', 'Tacos'])
print(NA, "\n", type(NA), "\n")

# The syntax for declaring a new DataFrame is a dictionary whose keys are the COLUMN NAMES, and whose values are a list of entries.

# The list of row labels used in a DataFrame is known as an Index; we can assign values to it by using an index parameter in our constructor.

print("Series\n")

# A Series, is a sequence of data values. If a DataFrame is a table, a Series is a list.

NU = pd.Series([1, 2, 3, 4, 5])
print(NU, "\n", type(NU), "\n")

# A Series is, in essence, a single column of a DataFrame. So you can assign row labels to the Series the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name.

SA = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(SA, "\n", type(SA), "\n")

# Series and DataFrames are intimately related, it's helpful to think of a DataFrame as actually being just a bunch of Series.

print("Reading Data Files\n")

# Data can be stored in any number of different forms and formats. By far the most basic of these is the humble CSV file. A CSV file is a table of values separated by commas; "Comma-Separated Values", or CSV.

# We'll use the pd.read_csv() function to read the data into a DataFrame.

admission_dataset = pd.read_csv("/home/aspphem/Desktop/CSV/Admission_Predict.csv")
print("Our Admission dataset has ", admission_dataset.shape, "records.\n") # We can use the shape attribute to check how large the resulting DataFrame is

# We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows.

print(admission_dataset.head())

# The pd.read_csv() function is well-endowed, whit over 30 optinal parameters you can specify. For example, you can make Pandas use the first column as the index, instead of creating a new one from scratch, we can specify an index_col.

admission_dataset = pd.read_csv("/home/aspphem/Desktop/CSV/Admission_Predict.csv", index_col=0)
print(admission_dataset.head())

# In Python we can access the property of an object by accessing it as an attribute. A book object, for example, might have a tittle property, which we can access by calling book.tittle. Columns in a Pandas DataFrame work in much the same way.

print(admission_dataset.CGPA) # Access the Research property of admission dataset.
print(type(admission_dataset.CGPA))

# If we have a Python dictionary, we can access its values using the indexing ([]) operator, we can do the same with columns in a DataFrame.

print(admission_dataset['CGPA'])
print(type(admission_dataset['CGPA']))

# To drill down a single specific value we need only use the indexing operator [] once more.

print(admission_dataset['CGPA'][1], "\n")

print("Indexing in Pandas \n")

# Pandas has its own accessor operators, loc and iloc.

# Index-based selection -- selecting data based on its numerical position in the data 'iloc'. To select the first row of data in a DataFrame, we may use the following:

print(admission_dataset.iloc[0], "\n")

# loc and iloc are row-first, column-second. This means that it's easier to retrieve rows and a little bit harder to retrieve columns. To get a column with iloc, we can do the following:

print(admission_dataset.iloc[:, 0]) # GRE Score column (1st column)
print(admission_dataset.iloc[:, 1]) # TOEFL Score (2nd column)
