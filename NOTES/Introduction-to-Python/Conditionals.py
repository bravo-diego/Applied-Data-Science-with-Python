# Conditionals

print("cat" == "dog") # Equality operator == 
# We use this operator to test whether two things are equal to each other.

print(1 != 2) # Not equals operator !=
# Negated form of the equality operator. 

print(2 >= 2) # Bigger or equal to >=; Smaller or equal to <=

print(1 == "1", "\n")

# Logical Operators

print("Logical Operators\n")

print("and")
print("Yellow" > "Cyan" and "Brown" > "Magenta", "\n") # and operator would need both expressions to be true at the same time.

print("or")
print(25 > 50 or 1 != 2, "\n") # or operator, instead, the expression will be true if either of the expressions are true, and false only when both expressions are false.

print("not")
print(not 42 == "Answer", "\n") # not operator inverts the value of the expression that's in front of it; if the expression is True it becomes False, if it's False becomes True.

# If & Else statements

print("If and Else statements\n")

def is_positive(number):
    if number > 0: # If the comparison is True, the code inside the body is executed; if the comparison evaluates to False, then the code block is skipped and will not be run.
        return True 

print(is_positive(1))
print(is_positive(0), "\n")

def user_name(user):
    if len(user) < 3:
        print("Invalid username. Must be at least 3 char long.")
    else:
        print("Valid username.")
        
user_name("Mandy")
user_name("MA")

def is_even(number):
    if number % 2 == 0: # Modulo operator % - returns the remainder of the integer division between two numbers.
        return True # When a return statement is executed, the functions exits, so that code that follows doesn't get executed.
    return False
    
print("\n")

# Elif statements

print("Elif statements\n")

def user_name(user):
    if len(user) < 3:
        print("Invalid username. Must be at least 3 char long.")
    elif len(user) > 15:
        print("Invalid username. Must be at most 15 char long.")
    else:
        print("Valid username.")
        
user_name("Mandilona")
user_name("Mandilona Come Croques")
user_name("MA")
