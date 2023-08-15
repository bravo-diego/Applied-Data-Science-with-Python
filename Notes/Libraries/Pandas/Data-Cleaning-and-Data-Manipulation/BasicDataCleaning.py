# Manipulating DataFrame -- Basic Data Cleaning Process

# Import pandas module
import pandas as pd

# Load our dataset
df = pd.read_csv("/home/aspphem/Desktop/CSV/presidents.csv")
print(df.head(10))

# Let's start with cleaning up that name into first name and last name. I want to create two new columns and apply a REGEX to the projection of the President column.

# We could make a copy of the president column.
df["First"] = df["President"]

# Then we call replace() and just have a pattern that matches the last name and set it to an empty string.
df["First"] = df["First"].replace("[ ].*", "", regex=True)
print(df.head())

del(df["First"])

# The apply function on a dataframe will take some arbitrary function you have written and apply it to either a Series (single column) or a DataFrame across all rows or columns. Lets write a function which splits a string into two pieces using a single row of data.

def splitname(row):
    # The row is a single Series object which is a single row indexed by column values
    row["First"]= row["President"].split(" ")[0]
    row["Last"]= row["President"].split(" ")[-1]
    return row # Now we just return the row and the pandas .apply() function will take of merging them back into a DataFrame
    
# Now we apply this to the DataFrame indicating we want to apply it across columns.
df = df.apply(splitname, axis='columns')
print(df.head())

del(df["First"])
del(df["Last"])

# .extract() function takes a regular expression as input and specifically requires you to set capture groups that correspond to the output columns you are interested in.
pattern = "(^[A-Za-z]*)(\s)([A-Za-z]*$)"

# Extract function is built into the str attribute of the series object, so we can call it using Series.str.extract(pattern).
print(df["President"].str.extract(pattern).head())

# If we name the groups we get named columns out.
pattern = "(?P<First>^[\w]*)(?:\s)(?P<Last>[\w]*$)" # NOTE -- ?: means that it is not capturing group

# Now call extract.
names = df["President"].str.extract(pattern)
print(names.head())

# We can just copy these into our main DataFrame.
df["First Name"] = names["First"]
df["Last Name"] = names["Last"]
print(df.head())

# Lets move on to clean up the Born column. First, lets get rid of anything that isn't in the pattern of Month Day and Year.
df["Born"] = df["Born"].str.extract("([\w]{3} [\w]{1,2}, [\w]{4})")
print(df["Born"].head())

# That cleans up the date format. But the type of this column is object. Lets update this column to the write data type as well.
df["Born"]=pd.to_datetime(df["Born"])
print(df["Born"].head())

print(df.head())
