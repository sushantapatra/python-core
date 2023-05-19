"""
Comments In Python
# this is a single line comment
multiline comment stater (''' ''' or """ """)
"""

"""
Print Statement
In Python, the print() function is commonly used to display output on the console or terminal. It takes one or more arguments and prints them to the standard output, followed by a newline character (\n) by default. Here's the basic syntax of the print() function:

print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Let's go over each parameter:

=> value1, value2, ...: These are the values or expressions that you want to print. You can pass multiple values, separated by commas.

=> sep=' ': This optional parameter specifies the separator between the values. By default, it is a single space ' ', but you can change it to any other string.

=> end='\n': This optional parameter specifies the string appended after all values have been printed. By default, it is a newline character '\n'. You can change it to any other string.

=> file=sys.stdout: This optional parameter specifies the file-like object where the output will be written. By default, it is set to sys.stdout, which represents the standard output. You can redirect the output to a file or another stream by providing a different file object.

=> flush=False: This optional parameter specifies whether the output buffer should be flushed immediately. By default, it is False, meaning the buffer is not flushed.

"""
# print("Hello, world!")
# # Output: Hello, world!

# name = "Alice"
# age = 25
# print("Name:", name, "Age:", age)
# # Output: Name: Alice Age: 25

# print(1, 2, 3, 4, sep=' | ', end='!')
# # Output: 1 | 2 | 3 | 4!


"""
Escape Sequences
In Python, escape sequences are special characters that are used to represent certain actions or characters that cannot be easily entered or printed directly. They are typically represented by a backslash followed by a specific character or combination of characters. Here are some common escape sequences in Python:

"""

# \\: Backslash
# print("This is a backslash: \\")
# \': Single quote
# print('He said, \'Hello!')
# \": Double quote
# print("She said, \"Hi!")
# \n: Newline
# print("Hello\nWorld!")
# \t: Horizontal tab
# print("Name:\tJohn")
# \r: Carriage return
# print("Hello\rWorld!")
# \b: Backspace
# print("Hello\bWorld!")
# \f: Form feed
# print("Hello\fWorld!")
# \v: Vertical tab
# print("Hello\vWorld!")
# \a: ASCII bell
# print("\aBeep!")
# \ooo: Octal value (where "ooo" is an octal number)
# print("\110\145\154\154\157")
# \xhh: Hexadecimal value (where "hh" is a hexadecimal number)
# print("\x48\x65\x6c\x6c\x6f")


"""
Python Datatype and Variable

In Python, variables are used to store data or values. They are created by assigning a value to a name or identifier. Python is a dynamically typed language, meaning that variables can hold values of different types, and their type can change during execution.

Here are some common data types in Python:

1=>Numeric Types:
    int: Integers, e.g., 5, -10, 0.
    float: Floating-point numbers, e.g., 3.14, -2.5, 0.0.
    complex: Complex numbers, e.g., 1 + 2j, -3j.

2=>Text Type:
    str: Strings of characters, enclosed in single quotes ('') or double quotes (""). For example, "Hello, world!".

3=>Sequence Types:
    list: Ordered, mutable collections of elements, enclosed in square brackets ([]). For example, [1, 2, 3].
    tuple: Ordered, immutable collections of elements, enclosed in parentheses (()). For example, (4, 5, 6).

4=>Mapping Type:
    dict: Unordered collections of key-value pairs, enclosed in curly braces ({}). For example, {"name": "John", "age": 25}.

5=>Set Types:
    set: Unordered collections of unique elements, enclosed in curly braces ({}). For example, {1, 2, 3}.

6=>Boolean Type:
    bool: Represents either True or False.

7=>None Type:
    None: Represents the absence of a value or a null value.

In Python, you can determine the data type of a value or variable using the type() function. 
The type() function returns the data type of an object.
"""
# name = "John"
# age = 30
# is_student = True
# x = 10
# y = 3.14
# # print(name, age, is_student, sep="\n")
# print(type(x))         # Output: <class 'int'>
# print(type(y))         # Output: <class 'float'>
# print(type(name))      # Output: <class 'str'>
# print(type(is_student))  # Output: <class 'bool'>

"""
Python Typecasting

Typecasting, also known as type conversion, is the process of converting a value from one data type to another in Python. It allows you to change the interpretation or representation of the data. Here are some commonly used typecasting functions in Python:

=> int(), float(), str(), bool(), list(), tuple(), set(), dict()
"""
# # int(): Converts a value to an integer data type.
# num_str = "10"
# num_int = int(num_str)
# print(num_int)      # Output: 10

# # float(): Converts a value to a floating-point data type.
# num_str = "3.14"
# num_float = float(num_str)
# print(num_float)    # Output: 3.14

# # str(): Converts a value to a string data type.
# num_int = 10
# num_str = str(num_int)
# print(num_str)      # Output: "10"

# # bool(): Converts a value to a boolean data type.
# num_int = 0
# is_valid = bool(num_int)
# print(is_valid)     # Output: False

# list(), tuple(), set(), dict(): Convert values to different collection data types.
# # List
# nums_tuple = (1, 2, 3)
# nums_list = list(nums_tuple)
# print(nums_list)    # Output: [1, 2, 3]

# # Tuple
# nums_list = [1, 2, 3]
# nums_tuple = tuple(nums_list)
# print(nums_tuple)   # Output: (1, 2, 3)

# # Set
# nums_list = [1, 2, 3, 3]
# nums_set = set(nums_list)
# print(nums_set)     # Output: {1, 2, 3}

# # Dictionary
# person_tuple = (("name", "John"), ("age", 25))
# person_dict = dict(person_tuple)
# print(person_dict)  # Output: {'name': 'John', 'age': 25}


"""
String

In Python, strings are sequences of characters enclosed in single quotes ('') or double quotes (""). They are a fundamental data type used to represent text. Here are some important aspects of strings in Python:
"""
# #1=>Creating Strings:

# # Using single quotes
# name = 'John'
# # Using double quotes
# message = "Hello, world!"
# # Escaping special characters
# sentence = "She said, \"Hello!\""
# print(name, message, sentence)

# 2 =>Accessing Characters:
# name = "John"
# print(name[0])       # Output: 'J'
# print(name[-1])      # Output: 'n'

# # 3=> String Slicing:
# name = "John Doe"
# print(name[0:4])     # Output: 'John'
# print(name[5:])      # Output: 'Doe'

# # 4=>String Concatenation:
# name = "John"
# greeting = "Hello, " + name + "!"
# print(greeting)      # Output: 'Hello, John!'

# # 5=>String Length:
# name = "John"
# length = len(name)
# print(length)        # Output: 4

# # 6=>String Methods:
# name = "john doe"
# print(name.upper())          # Output: 'JOHN DOE'
# print(name.capitalize())     # Output: 'John doe'
# print(name.replace('doe', 'smith'))  # Output: 'john smith'
# print(name.title())            # Output:"John Doe"


# # find(), index(): Searches for a substring within a string and returns the index of its first occurrence. The difference is that find() returns -1 if the substring is not found, while index() raises an exception.
# message = "Hello, world!"
# print(message.find("world"))      # Output: 7
# print(message.index("world"))     # Output: 7

# # count(): Counts the number of occurrences of a substring within a string.
# message = "Hello, world!"
# print(message.count("l"))         # Output: 3

# # isdigit(), isalpha(), isalnum(): Checks if a string consists of digits, alphabetic characters, or alphanumeric characters, respectively.
# num = "123"
# word = "Hello"
# mix = "Hello123"
# print(num.isdigit())              # Output: True
# print(word.isalpha())             # Output: True
# print(mix.isalnum())              # Output: True

# # startswith(), endswith(): Checks if a string starts or ends with a specified prefix or suffix.
# message = "Hello, world!"
# print(message.startswith("Hello"))       # Output: True
# print(message.endswith("world!"))        # Output: True

# # splitlines(): Splits a multi-line string into a list of individual lines.
# poem = "Roses are red\nViolets are blue\nSugar is sweet\nAnd so are you"
# lines = poem.splitlines()
# print(lines)
# # Output:
# # ['Roses are red', 'Violets are blue', 'Sugar is sweet', 'And so are you']


# # 7=>String Formatting:
# name = "John"
# age = 25
# print("My name is {} and I am {} years old.".format(name, age))
# print(f"My name is {name} and I am {age} years old.")
# # Output: 'My name is John and I am 25 years old.'

# # 8=>String Operations:
# name = "John"
# print(name + " Doe")         # Output: 'John Doe'
# print(name * 3)              # Output: 'JohnJohnJohn'

# To know all str function list in python
# print(dir(str))
# print(help(str.__doc__))
# Read the function documentation
# print(str.islower.__doc__)


"""
If Else Statement

The Python if else statement is used to execute a block of code if a condition is true, and a different block of code if the condition is false.
if condition:
    # block of code to be executed if condition is true
else:
    # block of code to be executed if condition is false
"""
# # check if the user is older than 18
# age = 18

# if age >= 18:
#     print("You are old enough to vote.")
# else:
#     print("You are not old enough to vote.")

"""
Match Case Statement

In this example, the value of the user_type variable is matched against the patterns "student", "teacher", and "staff". If the value of user_type matches one of the patterns, the block of code associated with that pattern will be executed. Otherwise, the block of code associated with the _ pattern will be executed.

The _ pattern is a special pattern that matches any value. It is often used as a catch-all pattern to execute code if none of the other patterns match.
"""
# # check if the user is a student, teacher, or staff member
# user_type = "student"

# match user_type:
#     case "student":
#         print("You are a student.")
#     case "teacher":
#         print("You are a teacher.")
#     case "staff":
#         print("You are staff.")
#     case _:
#         print("You are not a student, teacher, or staff member.")

"""
For Loop
In Python, a for loop is used to iterate over a sequence of elements. It allows you to perform a certain block of code repeatedly for each item in the sequence. The general syntax of a for loop in Python is as follows:

for item in sequence:
    # Code block to be executed for each item
    # You can access the current item using the 'item' variable
    # Do something with 'item'
"""
# string = "Remember"
# for c in string:
#     print(c)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# oddNum = []
# evenNum = []
# for num in numbers:
#     if num % 2 == 0:
#         evenNum.append(num)
#     else:
#         oddNum.append(num)


# print(oddNum, evenNum)

"""
While Loop

In Python, a while loop is used to repeatedly execute a block of code as long as a certain condition is true. It allows you to keep executing the code block until the condition becomes false. The general syntax of a while loop in Python is as follows:
"""

# num = 1

# while num <= 5:
#     print(num)
#     num += 1

"""
Function

In Python, a function is a block of code that performs a specific task and can be called and executed at any point in a program. Functions allow you to organize your code into reusable components, improving code readability and maintainability.

Defining a Function:
A function in Python is defined using the def keyword, followed by the function name, parentheses (which may contain parameters), and a colon. The general syntax for defining a function is as follows:

Functions can accept a variable number of arguments using special syntax. The *args parameter allows you to pass multiple positional arguments, and the **kwargs parameter allows you to pass multiple keyword arguments. Here's an example:
"""


# def greet(name):
#     print("Hello, " + name + "!")


# # Calling the function
# greet("Alice")


# def add(a, b):
#     return a + b


# result = add(3, 5)
# print(result)

# # Default Parameters:
# def greet(name, greeting="Hello"):
#     print(greeting + ", " + name + "!")


# greet("Alice")
# greet("Bob", "Hi")

# Variable-Length Arguments:
'''
In the above example, the print_arguments function accepts multiple positional arguments using *args and multiple keyword arguments using **kwargs. It then prints the arguments.
'''

# def print_arguments(*args, **kwargs):
#     for arg in args:
#         print(arg)

#     for key, value in kwargs.items():
#         print(key + ": " + str(value))


# print_arguments("apple", "banana", name="Alice", age=25)

# def avarage(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n

#     return sum/len(numbers)


# avg = avarage(10, 2, 23, 4, 5)
# print(avg)

# Lambda Functions (Anonymous Functions):
# Lambda functions are small, anonymous functions that are defined without a name. They are typically used for short, one-line functions. Here's an example:


# def add(x, y): return x + y


# result = add(3, 5)
# print(result)

# Decorators:
'''Decorators are functions that wrap other functions to enhance their functionality. They allow you to modify the behavior of a function without changing its source code. Decorators are denoted by the @ symbol followed by the decorator name, placed above the function definition. Here's an example:
In the above example, the uppercase_decorator function is a decorator that converts the result of the decorated function to uppercase. The greet function is decorated with @uppercase_decorator, so the output is in uppercase.
'''


# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         return result.upper()

#     return wrapper


# @uppercase_decorator
# def greet():
#     return "hello, world"


# print(greet())

"""
List

In Python, a list is a built-in data type that represents an ordered collection of items. Lists are mutable, meaning they can be modified after they are created. They can contain elements of different data types, such as integers, floats, strings, or even other lists. Lists are defined using square brackets [ ], and the elements are separated by commas. Here's an example of creating a list:

"""
# my_list = [1, 2, 3, 4, 5]

# # print(type(my_list)) #<List>
# print(my_list)
# # Accessing Elements:
# # You can access individual elements of a list using indexing. The first element is at index 0, the second element at index 1, and so on. Negative indices can be used to access elements from the end of the list. Here's an example:
# print(my_list[0])    # Output: 1
# print(my_list[2])    # Output: 3
# print(my_list[-1])   # Output: 5 (last element)

# # Modifying Elements:
# # Since lists are mutable, you can modify individual elements by assigning new values to specific indices. Here's an example:
# my_list = [1, 2, 3, 4, 5]
# print(my_list)    # Output: [1, 2, 3, 4, 5]
# my_list[2] = 7
# print(my_list)    # Output: [1, 2, 7, 4, 5]

# # List Methods:
# # Lists come with several built-in methods that allow you to manipulate and perform operations on them. Some commonly used methods include append(), extend(), insert(), remove(), pop(), sort(), and reverse(). Here's an example:
# my_list = [1, 2, 3]
# my_list.append(4)         # Add an element at the end
# my_list.extend([5, 6])    # Extend the list with another list
# my_list.insert(0, 0)      # Insert an element at a specific index
# my_list.remove(3)         # Remove the first occurrence of an element
# popped_element = my_list.pop()     # Remove and return the last element
# my_list.sort()            # Sort the list in ascending order
# my_list.reverse()         # Reverse the order of elements
# print(my_list)            # Output: [6, 5, 4, 2, 1, 0]


# List Slicing:
# You can extract a portion of a list using slicing, which allows you to create a new list containing a subset of the original elements. Here's an example:
my_list = [1, 2, 3, 4, 5]
subset = my_list[1:4]    # Extract elements from index 1 to 3 (exclusive)
print(subset)            # Output: [2, 3, 4]
