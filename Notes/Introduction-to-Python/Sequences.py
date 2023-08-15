# Sequences

# Strings -- sequences of characters. Strings are immutable (they can't change).

# Lists -- lists in Python are defined using square brackets, with the elements stored in the list separated by commas. Lists are mutable (they can change).

# Strings and lists are both examples of sequences of data. Sequences have similar properties; 1) being able to iterate over them using loops, 2) support indexing, 3) using the len() function to find the length of the sequence, 4) using the plus operator (+), in order to concatenate, and 5) using the in keyword to check if the sequence contains a value.

print("Lists\n")

x = ["Now", "we", "are", "coocking :)"] # list example

print(x)
print(type(x))
print(len(x))
print("are" in x, "\n")

print("List Indexing\n")

print(x[0]) # first element
print(x[3]) # last element
print(x[1:3], "\n") # second and third element; [x:y] range includes x, but excludes y

def get_word(sentence, n):
    if n > 0: # if n > 0
        words = sentence.split()
        if n <= len(words): # if n is not more than number of words
            return(words[n-1])
    return("")
    
print("Lists Methods\n")

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
print(fruits)
fruits.append("Kiwi") # adds the element at the end of the list
print(fruits)
fruits.insert(0, "Orange") # takes an index as the first parameter and an element as the second parameter
fruits.remove("Melon") # removes from the list the element we pass to it
print(fruits)
fruits.pop(0) # returns the element that was removed at the index that was passed
print(fruits) 
fruits[1] = "Strawberry" # change an item by assigning something else to that position
print(fruits, "\n")

print("Tuples\n")

# Tuples -- sequences of elements of any type, that are immutable (they can't change). We write tuples in parentheses instead of square brackets.

names = ("Mandy", "Robin", "Molly")
print(names)
print(len(names))
print(type(names), "\n")

# The position of the elements inside the tuple have meaning. It's common to use tuples to represent data that has mote than one value and that needs to be kept together.

def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format(size/1024))
    
print("Iterating over Lists and Tuples\n")

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
    
print("Total characters: {}. Average length: {}.".format(chars, chars/len(animals)), "\n")

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
    
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
    
print(full_emails([("mandy@gmail.com", "Mandy Mandilona"), ("rocky@gmail.com", "Robin Roqueto")]))

def skip_elements(elements):
    result = []
    for index, element in enumerate(elements): # enumerate() function takes a list as a parameter and returns a tuple for each element in the list; the first value of the tuple is the index and the second value is the element itself
        if index % 2 == 0:
            result.append(element)
    return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g", "h"]))
print(skip_elements(["Mandy", "Bruno", "Robin", "Coqueta", "Molly"]), "\n")

print("List Comprehensions\n")

multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

multiples_short = [x*8 for x in range(1,11)] # create new lists based on sequences or ranges
print(multiples_short)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C++"]
lenghts = [len(language) for language in languages]
print(lenghts)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

def odd_numbers(n):
    return [x for x in range(n+1) if x % 2 != 0]

print(odd_numbers(10))

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = [files.split(".")[0] + ".h" if files[-4:] == ".hpp" else files for files in filenames]
print(newfilenames, "\n")

print("Dictionaries\n")

# The data inside dictionaries take the form of pairs of keys and values.

files = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(files, type(files), len(files))
print("There are {} files in .py format".format(files["py"]))

files["html"] = 9
print(files, type(files), len(files))

files["csv"] = 100 # keys are unique; if we try to store two different values for the sames key, we'll just replace one with the other
print(files, type(files), len(files))

del files["html"]
print(files, type(files), len(files))

for extension in files:
    print(extension)
    
for ext, amount in files.items(): # key value pair
    print("There are {} files with the .{} extension".format(amount, ext))
    
print(files.keys(), files.values()) # keys() to get the keys; values() to get just the values

for value in files.values():
    print(value)
    
beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for beast, feature in beasts.items():
    print("{} have {}".format(beast, feature))
