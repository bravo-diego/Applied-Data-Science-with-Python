# Data Types and Scales

# As a Data Scientists there is at least four different scales.

# Ratio Scale -- Units are equally spaced; mathematical operations of +-/* are valid (e.g. height and weight).

# Interval Scale -- Units are equally spaced, but there is no true zero; operations like multiplication and division are not valid (e.g. temperature in Fahrenheit or Celsius, there's never an absence of temperature, zero degrees is actually a meaningful value itself).

# Ordinal Scale -- Order of units is important, but not evenly spaced (e.g. letter grades such as A+, A).

# Nominal Scale (Categorical Data) -- Categories of data, but the categories have no order with respect to one another; categorical values are very common and we generally refer to categories where there are only two possibles values as binary categories (e.g. teams of a sport). 

import pandas as pd
import numpy as np

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'], index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'], columns=["Grades"])

print(df)
print(df.dtypes)

# We can change the type to category using the astype() funtion

print(df["Grades"].astype("category").head()) # 11 categories

# We can tell Pandas that the data is ordered by first creating a new categorical data type which the list of the categories (in order) and the ordered=True flag.

my_categories = pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'], ordered=True)

grades = df["Grades"].astype(my_categories)
print(grades.head()) # 11 categories but is also aware of the order of those categories

# Comparisons and boolean masking

print(df[df["Grades"] > "C"])

print(grades[grades > "C"]) # operator works as we would expect

# We can then use a certain set of mathematical operator, like minimum, maximum, etc., on the ordinal data.

# Converting a scale from something that is on the interval o ratio scale, like a numeric grade, into one which is categorical. Now, this might seem a bit counter intuitive to you, since you are loosing information about the value.

# Pandas has a function called cut which takes as an argument some array-like structure like a column of a DataFrame or a Series. It also takes a number of bins to be used, and all bins are kept at equal spacing.

df = pd.read_csv("/home/aspphem/Desktop/CSV/census.csv") # loading dataset
df = df[df['SUMLEV'] == 50] # creating and applying a boolean mask; filtering NA values
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg(np.average) # setting a new index; grouping by level parameter; aggregating average 2010 population ('CENSUS2010pop' column)

print(df.head())

# Now if we just want to make 'bins' of each of these, we can use cut() function.

print(pd.cut(df, 10))

# Cutting is just one way to build categories from your data. Cut gives you interval data, where the spacing between each category is equal sized.
