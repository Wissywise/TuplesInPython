"""
A tuple in Python is a built-in data type used to store an ordered, unchangeable (immutable) collection of items.
Tuples are written by placing elements inside parentheses (), separated by commas. Unlike lists, once a tuple is
created, you cannot add, remove, or alter its elements.
Ordered: Elements have a defined order that will never change.
Immutable: Cannot be altered or modified after creation, protecting data integrity.
Heterogeneous: Can store multiple data types simultaneously (strings, integers, floats, booleans).
Indexed: Elements are accessed using standard integer indices (e.g., my_tuple[1]).
"""
# 1. Creating a tuple with mixed data types
coordinates = (4, 10, "North")

# 2. Accessing elements (indexing starts at 0)
print(coordinates[0])  # Output: 4
print(coordinates[2])  # Output: North

# 3. Tuples allow duplicate values
numbers = (1, 2, 2, 3)
print(numbers)         # Output: (1, 2, 2, 3)

# 4. Immutability (This will cause an error!)
# coordinates[0] = 5   # TypeError: 'tuple' object does not support item assignment

person = ("John Wick", "July 10, 2000", "CA1467")

print("Name:", person[0])
print("Date of Birth:", person[1])
print("ID:", person[2])

not_a_tuple = ("apple")   # Python treats this as a standard string (str)
is_a_tuple = ("apple",)   # Python recognizes this as a tuple

# Create a tuple representing a user profile
user = ("Alice", 28, "Engineer")

"""
Unpacking allows you to extract the values inside a tuple and assign them directly to distinct variables in a 
single line of code. Note: The number of variables on the left must exactly match the number of elements inside the 
tuple, otherwise Python will throw a ValueError
"""
# Unpack the tuple into individual variables
name, age, job = user

print(name)  # Output: Alice
print(age)   # Output: 28
print(job)   # Output: Engineer
