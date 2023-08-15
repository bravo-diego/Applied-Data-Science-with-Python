# Querying a DataFrame

# A Boolean mask is an array which can be of one dimension like a series, or two dimensions like a data frame, where each of the values in the array are either true or false. This array is essentially overlaid on top of the data structure that we are querying. And any cell aligned with the true value will be admitted into our final result, and any cell aligned with a false value will not.

import pandas as pd

df = pd.read_csv('/home/aspphem/Desktop/CSV/Admission_Predict.csv', index_col=0)

df.columns = [x.lower().strip() for x in df.columns]

print(df.head())

# Boolean masks are created by applying operators directly to the Pandas Series or DataFrame objects. For instance, in our graduate admission dataset we might be interested in seeing only those students that have a chance higher than 0.7.

# To build a Boolean mask for this query, we want to project the chance of admit column using the indexing operator and apply the greater than operator with a comparison of 0.7. 

admit_mask = df['chance of admit'] > 0.7
print(admit_mask)

# The resultant Series is indexed where the value of each cell is either True or False depending on whether a student has a chance of admit higher than 0.7, since only one column is being operator on.

# We can "hide" the data don't want, which is represented by all of the False values. We do this using the .where() function on the original DataFrame.

print(df.where(admit_mask).head())

# The resulting data frame keeps the original indexed values, and only data which met the condition was retained. All the rows which did not meet the condition have NaN data instead, but these rows were not dropped from our dataset.

# The next step is, if we don't want the NaN data, we use dropna() function.

print(df.where(admit_mask).dropna().head())

# where() is not actually used that often. Instead Pandas has a shorthand syntax which combines where() and dropna(), doing both at once.

print(df[df['chance of admit'] > 0.7].head())

# It can be called with a string parameter to project a single column.

print(df['gre score'].head())
print(type(df['gre score'].head())) # Series

# Or can send it a list of columns as strings

print(df[['gre score', 'toefl score']].head())
print(type(df[['gre score', 'toefl score']].head())) # DataFrame

# Or you can send it a boolean mask

print(df[df['gre score']>330].head())

# Combining multiple boolean masks, such as multiple criteria for including. 

# '&' if both masks must be True for a True value to be in the final mask, or '|' if only needs one to be True.

print((df['chance of admit'] > 0.7) & (df['chance of admit'] < 0.9))

# Note: A common error for new pandas users is to try and do boolean comparisons using the & operator but not putting parentheses around the individual terms you are interested in.

# Another way to do this is to just get rid of the comparison operator completely, and instead use the built in functions which mimics this approach.

print(df['chance of admit'].gt(0.7) & df['chance of admit'].lt(0.9))

print(df['chance of admit'].gt(0.7).lt(0.9)) # gt(a, b) == a > b; lt(a, b) == a < b



