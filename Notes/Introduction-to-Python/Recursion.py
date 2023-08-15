# Recursion

# Repeated application of the same procedure to a smaller problem. In Python by default, you can call a recursive function 1,000 times until you reach the limit.

print("Factorial Example\n")
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2: # base case returns a value without calling the same function
        print("Returning 1")
        return 1
    result = n * factorial(n-1) # recursive case calls the function again, with a different value
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result
    
factorial(4)
print("\n")

print("Sum Example\n")
def sum_positive_numbers(n):
    if n < 1: # base case
        return n
    return n + sum_positive_numbers(n-1) # recursive case
    
print(sum_positive_numbers(3))
print(sum_positive_numbers(5))

# Recursive function structure

# def recursive_function(parameters):
#   if base_case_condition(parameters):
#       return base_case_value
#   recursive_function(modified_parameters)
