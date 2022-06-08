'''
Built-in practice: range()
In this exercise, you will practice using Python's built-in function range(). Remember that you can use range() in a few different ways:

1) Create a sequence of numbers from 0 to a stop value (which is exclusive). This is useful when you want to create a simple sequence of numbers starting at zero:

range(stop)

# Example
list(range(11))

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2) Create a sequence of numbers from a start value to a stop value (which is exclusive) with a step size. This is useful when you want to create a sequence of numbers that increments by some value other than one. For example, a list of even numbers:

range(start, stop, step)

# Example
list(range(2,11,2))

[2, 4, 6, 8, 10]
'''

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1, 12, 2)]
print(nums_list2)

'''
Built-in practice: enumerate()
In this exercise, you'll practice using Python's built-in function enumerate(). This function is useful for obtaining an indexed list. For example, suppose you had a list of people that arrived at a party you are hosting. The list is ordered by arrival (Jerry was the first to arrive, followed by Kramer, etc.):

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
If you wanted to attach an index representing a person's arrival order, you could use the following for loop:

indexed_names = []
for i in range(len(names)):
    index_name = (i, names[i])
    indexed_names.append(index_name)

[(0,'Jerry'),(1,'Kramer'),(2,'Elaine'),(3,'George'),(4,'Newman')]
But, that's not the most efficient solution. Let's explore how to use enumerate() to make this more efficient.
'''

# Rewrite the for loop to use enumerate
indexed_names = []
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, start=1)]
print(indexed_names_unpack)

'''
Built-in practice: map()
In this exercise, you'll practice using Python's built-in map() function to apply a function to every element of an object. Let's look at a list of party guests:

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
Suppose you wanted to create a new list (called names_uppercase) that converted all the letters in each name to uppercase. you could accomplish this with the below for loop:

names_uppercase = []

for name in names:
  names_uppercase.append(name.upper())

['JERRY', 'KRAMER', 'ELAINE', 'GEORGE', 'NEWMAN']
Let's explore using the map() function to do this more efficiently in one line of code.

'''

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))


# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)
