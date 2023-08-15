# Loops 

import operator

# While loops instruct your computer to continuosly execute your code based on the value of a condition.
print("While loops\n")

x = 0 # Initializing: to give an initial value to a variable.
while x < 5: # Once the statement is no longer true, the loop exits and the next line of code will be executed.
    print("Not there yet, x=" + str(x))
    x += 1
print("\nx=" + str(x), "\n")

def attempts(n):
    x = 1
    while operator.le(x,n):
        print("Attempt " + str())
        x += 1
    print("Done\n")

attempts(4)

# Note -- If you try ti use a variable without first initializing it, you'll run into a NameError. This is the Python interpreter catching the mistake and telling you that you are using an undefined variable. The fix is pretty simple: initialize the variable by assigning the variable a value before you use it.

print("For Loops\n")

for x in range(5): # a range of numbers will start with the value 0 by default; the list of numbers generated will be one less the given value
    print(x)
    
friends = ['Mandy', 'Robin', 'Moly']
for y in friends:
    print("Hi " + y)
    
# For loops when there is a sequence of elements that you want to iterate.
# While loops when you want to repeat an action until a condition changes.

product = 1
for n in range(1, 10):
    product = product * n
    
print(product, "\n")

def celsius(x):
    return ((x-32)*5)/9

for x in range (0,101,10): # we are using 101 for the upper limit instead of 100 -- range function never includes the last element and in this case we want to include 100 in our range
    print(x, celsius(x))
    
# range() function generates a sequence of integer numbers; can take up to three parameters: range(start, stop, step).

# Start -- the first item in the range() function parameters is the starting position of the range. The default is the first index position, which points to the numeric value 0. N o t e: this value ins included in the range.

# Stop -- the second item in the range() function parameters is the ending position. There is no default index position, so this index must be given to the range() parameters.

# Step -- the third item in the range() function parameters is the incremental step value. The default increment is +1. The default value can be overridden with any valid increment. N o t e: the loop will still end at the end-of-range index position, regardless of the incremental value.


