# # How to create a list
# # Method 1: Creating an empty list when you don't have an element yet, but plan to add later. Using square brackets

# empty_list = []
# print(empty_list)

# # Method 2: Using the list()

# empty_list2 = list()
# print(empty_list2)

# # Creating a List with Initial Elements. Lists can store multiple items separated by commas inside square brackets []
# # List of Integers

# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# # List of strings

# fruits = ["apple", "banana", "cherry"]
# print(fruits)  # Output: ['apple', 'banana', 'cherry']

# # Mixed data types
# mixed_list = ["Alice", 25, 5.8, True]
# print(mixed_list)  # Output: ['Alice', 25, 5.8, True]

# # Creating a List from Another Sequence. you can convert strings, tuples or other iterables into a list

# # From a string (each character becomes an element)
# chars = list("hello")
# print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']

# # From a Tuple 
# my_tuple = (10, 20, 30)
# list_from_tuple = list(my_tuple)
# print(list_from_tuple)

# #From a range
# # Squares of numbers 0–4
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Even numbers between 0–10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8, 10]

# Creating a Nested List. A list can contain other lists. It is useful for matrices or grouped data.

# Matrix - 


