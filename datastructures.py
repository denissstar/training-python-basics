# Python data structures exercise
# For syntax highlighting install Python plugin for VSCode, or use PyCharm
# Refer to https://docs.python.org/3/tutorial/datastructures.html for the help with methods

# List
"""Create a list of cloud service providers that you are aware of, and print it out
"""
letters = ["a", "b", "c"]
print(letters)

"""Print second element of the list ["a", "b", "c", "d", "e"]
Print the last element of this list
"""
letters = ["a", "b", "c", "d", "e"]
print(letters[0])

"""Concatenate two lists ["a", "b", "c"] and ["c", "d", "e"] together, so each list element is a letter string
List methods .append() or .extend() will be useful here
"""
list_a = ["a", "b", "c"]

# Tuple
"""Create a tuple of four world oceans (as strings) and print it out.
Some scientists claim that they discovered a new ocean! Try to call .append method on that tuple to add one extra element, e.g. "Antarctic". Why it won't work?
"""
tuple_numbers = (1, 2, 3)

# Dictionary
"""For the following employees dictionary add a new key:pair, where key is your region and values is a list of some names of your local colleagues
Print out a list of your local colleagues from this dictionary
"""
employees = {"UK": ["Pascal", "Deniss"]}
print(employees["UK"])

# Set
"""Create two sets 1,2,3 and 3,4,5 and print them out
Create a set union of those sets 1,2,3 and 3,4,5 using .union method and print it out.
Create a new set out of this list ["a", "b", "b", "c"] using in-built set() function
"""
set_a = {1, 2, 3}