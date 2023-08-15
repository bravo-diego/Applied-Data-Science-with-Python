# Basic Python Syntax Introduction

# Data Types Introduction
print("Data Types\n")

# String -- text between quotes, single or double quotes.
a = "hello, Mandy"
print(a)
print(type(a))

# Integers -- whole number, without a fraction.
x = 7+8
print(x)
print(type(x))

# Float -- real number that can contain a fractional part.
y = 2.5
print(y)
print(type(2.5))

# None -- A special data type in Python used to indicate that things are empty or that they returned nothing
def greeting(name):
    print("Welcome, " + name)
    
result = greeting("Mandy")
print(type(result))

# Boolean -- Represent one of two possible states: either True or False
w = 10>1
print(w)
print(type(w), "\n")

# Variables
print("Variables\n")

# Names that we give to certain values in our programs, the process of storing a value inside a variable is called 'Assignment'.

length = 10
print("lenght = 10")
width = 2
print("width = 2")
area = length * width # Expression -- combination of numbers, symbols, or other variables that produce a result when evaluated.
print("area = lenght * width \n", area, "\n")

# Variable Naming Restrictions

# 1) Don't use keywords or functions that Python reserves for its own.
# 2) Don't use spaces.
# 3) Must start with a letter or an underscore ( _ ).
# 4) Must be made up of only letters, numbers, and underscores.

# NOTE: Python variables are case sensitive, so capitalization matters.

# Expressions, Numbers, and Type Conversions
print("Expressions, Numbers, and Type Conversions\n")

# Implicit Conversion -- The interpreter automatically converts one data type into another.

z = 7 + 8.5
print(z)
print(type(z))

# Explicit Conversion -- Manually convert from one data type to another by calling the relevant function for the data type we want to convert to.

base = 6
height = 3
area = (base * height)/2
print("The area of the triangle is: " + str(area)) # str() function to convert a number into string
