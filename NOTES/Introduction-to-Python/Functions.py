# Functions

print("Functions\n")

# Define our own functions through def keyword, followed by the name we want to give our function. After the name we have parameters, also called arguments, for the function enclosed in parentheses.

# A function can have no parameters, or it can have multiple parameters.

def greeting(name, department): # def keyword + function name + parameters + colon
    print("Welcome, " + name)
    print("You are part of " + department)
    
greeting("Mandilona", "Data Science Team \n")

def area_triangle(base, height):
    return (base*height)/2 # we use the return keyword which tells the function to pass data back, we can store the return value in a variable

area_a = area_triangle(100, 200)
area_b = area_triangle(122, 221)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum), "\n")

# Principles of Code Reuse

def lucky_number(name): # reusable code
    num = len(name) * 9
    print("Hey " + name + "!. Your lucky number is " + str(num))
    
lucky_number("Mandy")
lucky_number("Molino")









