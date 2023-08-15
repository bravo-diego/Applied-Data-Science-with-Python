# Dictionaries and Sets

# A DICTIONARY is a data structure that consists of a collection of key-value pairs.

zoo = {'pen_1': 'penguins', 'pen_2': 'zebras', 'pen_3': 'lions'}
print(zoo['pen_3']) # key

pets = dict(coque_1='Mandy', coque_2='Robin', coque_3='Molly')
print(pets['coque_1'])

pets['coque_4'] = 'Roqueto'
print(pets)

toys = dict([['toy_1', 'penguin'], ['toy_2', 'popis'], ['toy_3', 'lion'],])
print(toys['toy_2'])

# Dictionaries are unordered; so you can't access to it trough index (i.e zoo[2]).

team = [('Mandy', 25, 'Come croquetas'), ('Robin', 40, 'Come gatos'), ('Moly', 25, 'Come galletas')]

new_team = {}

for name, age, position in team:
    if position in new_team:
        new_team[position].append((name, age))
    else:
        new_team[position] = [(name, age)]
        
print(new_team['Come croquetas'])

print(new_team.keys())
print(new_team.values())

for keys, values in new_team.items():
    print(keys, values)
    
# A SET is a data structure in Python that contains only unordered, non-interchangeable elements; argument must be iterable.

x = set(['Mandy', 'Robin', 'Moly', 'Mandy']) # list as argument
print(x) # each element must be unique in sets

y = set(('Mandy', 'Robin', 'Moly', 'Mandy')) # tuple as argument
print(y) 

z = set('Mandilona') # string as argument
print(z, type(z)) # characters in an unordered way

w = {'Mandilona'}
print(w, type(w))

q = {} # empty curly braces interpreted as dictionary
print(q, type(q))

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

print(set1.intersection(set2)) # intersection method finds the elements that two sets have in common
print(set1 & set2)

print(set1.union(set2)) # union method finds all elements from both sets
print(set1 | set2)

print(set1.difference(set2)) # difference method shows elements in set one that are not shared with set two
print(set1 - set2)

print(set1.symmetric_difference(set2)) # symmetric difference method shows all the elements that two sets don't share
print(set1 ^ set2)
