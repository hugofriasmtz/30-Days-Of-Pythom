# 1. List Comprehension
# List comprehension in Python is a compact way to create lists from a sequence.
# It is faster and more readable than using a traditional for loop.

# syntax
# [i for i in iterable if expression]

# 1.1 Convert a string to a list of characters

# Method 1 - using list()
language = 'Python'
lst = list(language)             # converts string to list
print(type(lst))                 # <class 'list'>
print(lst)                       # ['P', 'y', 't', 'h', 'o', 'n']

# Method 2 - using list comprehension
lst = [i for i in language]
print(type(lst))                 # <class 'list'>
print(lst)                       # ['P', 'y', 't', 'h', 'o', 'n']

# 1.2 Generate lists of numbers

# Generate numbers from 0 to 10
numbers = [i for i in range(11)]
print(numbers)                   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Math operations inside the comprehension
squares = [i * i for i in range(11)]
print(squares)                   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create list of tuples (number, square)
numbers = [(i, i * i) for i in range(11)]
print(numbers)                   # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), ...]

# 1.3 Use conditions inside comprehension

# Even numbers between 0 and 20
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)              # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Odd numbers between 0 and 20
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)               # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 1.4 Filter data with multiple conditions
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)     # [4, 6, 8, 10]

# 1.5 Flatten nested lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)            # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 2. Lambda Function
# A Lambda function is an anonymous function (without a name). It can have multiple parameters
# but only one expression. It's used to create short functions in a single line.

# syntax
# lambda parameters: expression

# Basic example
x = lambda a, b: a + b
print(x(2, 3))                   # 5

# 2.1 Convert a normal function to lambda

# Traditional function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))        # 5

# Equivalent lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))        # 5

# 2.2 Self-invoking lambda
print((lambda a, b: a + b)(2, 3))  # 5

# 2.3 Lambda with a single variable
square = lambda x: x ** 2
print(square(3))                 # 9

cube = lambda x: x ** 3
print(cube(3))                   # 27

# 2.4 Lambda with multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))  # 22

# 2.5 Lambda inside another function
def power(x):
    return lambda n: x ** n

# power(2)(3) computes 2 ** 3
cube = power(2)(3)
print(cube)                      # 8

two_power_of_five = power(2)(5)
print(two_power_of_five)         # 32
