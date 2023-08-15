# Mergin DataFrames

# Database terminology.

# Full Outer Join -- Returns all rows from both pandas DataFrames. In set theory it's called a union.

# Inner Join -- Returns a DataFrame with only those rows that have common characteristics.

import pandas as pd

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director HR'}, {'Name': 'Sally', 'Role': 'Course liasion'},{'Name': 'James', 'Role': 'Grader'}])

staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},{'Name': 'Mike', 'School': 'Law'},{'Name': 'Sally', 'School': 'Engineering'}])

student_df = student_df.set_index('Name')

print(staff_df)
print(student_df)

# If we want the union of these, we would call merge() passing in the DataFrame on the left and the DataFrame on the right and telling merge that we want it to use an outer join. We want to use the left and right indices as the joining columns.

print(pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)) # By default how parameter is inner

# If we wanted to get the intersection, that is, just those who are a student AND a staff, we could set the how attribute to inner.

print(pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True))

# If we want to get a list of all staff regardless of whether they were students or not. But if they were students, we would want to get their student details as well. To do this we would use a left join. 

print(pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True))

# Note -- The order of DataFrames in this function: the first DataFrame is the left DataFrame and the second is the right.

# List of all students and their roles if they were also staff. 

print(pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True))

# Merge method has a couple of other interesting parameters. First, you don't need to use indices to join on, you can use columns as well. 

# First, we need to remove our index from both of our DataFrames.

staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

print(pd.merge(staff_df, student_df, how='right', on='Name')) # ON parameter

# Conflicts between DataFrames.

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director HR', 'Location': 'State Street'}, {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},{'Name': 'James', 'Role': 'Grader', 'Location': 'Sesame Street'}]) # office location

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},{'Name': 'Mike', 'School': 'Law', 'Location': '1024 Billiard Avenue'},{'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}]) # home address

# _x or _y yo help differentiate between which index went with which column of data. The _x is always the left DataFrame information, and the _y is always the right DataFrame information.

print(pd.merge(staff_df, student_df, how='left', on='Name'))

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Last Name': 'Desjardings', 'Role': 'Director HR'}, {'Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},{'Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}]) 

student_df = pd.DataFrame([{'Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},{'Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},{'Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])

# James Wilde and James Hammond don't match on both keys since they have different last names. So we would expect that an inner join doesn't include these individuals in the output, and only Sally Brooks will be retained.

print(pd.merge(staff_df, student_df, how='inner', on=['Name', 'Last Name'])) # List of columns 

# If we think of merging as joining 'horizontally', meaning we join on similar values in a column found in two DataFrames then concatenating is joining 'vertically', meaning we put DataFrames on top or at the bottom of each other.


