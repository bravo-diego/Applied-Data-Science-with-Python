# Querying a Series

import pandas as pd
import numpy as np
import random

student_classes = {'Alice': 'Physics', 'Jack': 'Chemistry', 'Molly': 'English', 'Sam': 'Biology'}

s = pd.Series(student_classes)
print(s)

# If you wanted to see the 4th entry we would use the iloc attribute with parameter 3.

print(s.iloc[3])

# If you wanted to see what class Molly has, we would use the loc attribute of Molly.

print(s.loc['Molly'])

# iloc and loc are attributes NOT methods, so you don't use parentheses to query them, but square brackets instead.

class_code = {99: 'Physics', 100: 'Chemistry', 101: 'English', 102: 'Biology'}

r = pd.Series(class_code)

# print(r[0])
print(r.iloc[0])

# If we try and call r[0] we get a key error because there is no item in the classes list with an index of zero, instead we have to call iloc explictly.

# A common task is to want to consider all of the values inside of a series and do some sort of operation, find certain number, summarizing data or transforming data.

grades = pd.Series([90, 80, 70, 60])

total = 0

for grade in grades:
    total += grade
    
print(total/len(grades))

total_b = np.sum(grades)
print(total_b/len(grades))

# Series of random numbers

numbers = pd.Series(np.random.randint(0,1000,100))

# Top five items in that series with head() function

print(numbers.head())

print(len(numbers))

# A related feature in Pandas and Numpy is called broadcasting. With broadcasting, you can apply an operation to every value in the series, changing the series. If we wanted to increase every random variable by 2, we could do so quickly using the += operator directly on the series object.

numbers+=2
print(numbers.head())

# Pandas does support iterating through a series much like a dictionary, allowing to unpack values easily; iteritems() function returns a label and a value.

for label, value in numbers.iteritems():
    numbers._set_value(label, value+2)
print(numbers.head())

# The .loc attribute lets you not only modify data in place but also add new data as well. If the value you pass in as the index doesn't exist, then a new entry is added. And keep in mind, indices can have mixed types.

t = pd.Series([1, 2, 3])

t.loc['Biology'] = 102

print(t)

# Index values are not unique

student_classes_b = pd.Series({'Alice': 'Physics', 'Jack': 'Chemistry', 'Molly': 'English', 'Sam': 'History'})

mandy_classes = pd.Series(['Programming', 'Data Analytics'], index=['Mandy', 'Mandy'])

print(mandy_classes)

all_students = student_classes_b.append(mandy_classes)

print(all_students)

# In this example everything is a string, so there is no problems here. Append method doesn't change the underlying series objects, it instead returns a new series which is made up of the two append together. This is a common pattern in pandas -- by default returning a new object instead of modifying in place.

print(all_students.loc['Mandy'])

# Finally we see that when we query the append series for Mandy, we don't get a single value, but a series itself.

