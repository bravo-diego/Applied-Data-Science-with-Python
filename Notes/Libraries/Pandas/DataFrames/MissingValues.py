# Missing Values

# Missing values in Pandas using the None type and NumPy NaN values. 

# Missing values are pretty common in data cleaning activities. And, missing values can be there for any number of reasons.

# If you are running a survey and a respondant didn't answer a question the missing value is actually an omission. This kind of missing data is called -- Missing at Random -- if there are other variables that might be used to predict the variable which is missing. If there is no relationship to other variables, then we call this data -- Missing Completely at Random (MCAR)--

import pandas as pd
 
# Most missing values are often formatted as NaN, NULL, None, or N/A, sometimes missing values are not labeled so clearly.

# Pandas read_csv() function has a parameter called na_values to let us specify the form of missing values. It allows scalar, string, list, or dictionaries to be used.

df = pd.read_csv('/home/aspphem/Desktop/CSV/class_grades.csv')
print(df.head(10))

# We can use the function .isnull() to create a boolean mask of the whole dataframe. This effectively broadcasts the .isnull() function to every cell of data.

mask = df.isnull()
print(mask.head(10))

# Another useful operation is to be able to drop all of those rows which have any missing data, which can be done with the dropna() function.

print(df.dropna().head(10))

# One of the functions that Pandas has for working with missing values is the filling function, fillna(). This function takes a number of parameters. You could pass in a single value which is called scalar value to change all of the missing data to one value. 

# So, if we wanted to fill all missing values with 0, we would use fillna().

df.fillna(0, inplace=True) # Most DataFrame operations returned copies of DataFrames; so if you want to do it in place you often have to use the 'in place' parameter.

print(df.head(10))

# We can do customized fill-in to replace values with the replace() function. It allows replacement from several approaches: value-to-value, list, dictionary, regex.

df = pd.DataFrame({'A': [1, 1, 2, 3, 4], 
                   'B': [3, 6, 3, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
                   
print(df)

# Value-to-value

print(df.replace(1, 100))

print(df.replace([1, 3], [100, 300]))

# Pandas replacement supports REGEX.

df = pd.read_csv('/home/aspphem/Desktop/CSV/logs.csv')
print(df.head(20))

# To replace using regex we make the first parameter to replace the regex pattern we want to match, the second parameter the value that we want to emit upon match, and then we pass in a third parameter "regex=True".

# Context - We want to detect all HTML pages in the "video" column, lets say that jsut means they end with ".html", and we want to overwrite that with the keyword "webpage".

print(df.replace(to_replace=".*.html$", value="webpage", regex=True))

# One last note on missing values; when yo use statistical function on DataFrames, these functions typically ignore missing values. For instance, if you try to calculate the mean value, the underlying NumPy functions may ignore those missing values.
