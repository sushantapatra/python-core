================= IDENTIFIER ==========================
An identifier is a name having a few letters, numbers and special characters _(underscore).
It should always start with a non-numeric character.
It is used to identify a variable, function, symbolic constant, class etc.

=> Python is a case sensitive programming language.
d is not equal to d
t is not equal to t
rahul is not equal to rahul

=================== CONSTANTS ===================
A constant is an identifier whose value connot be changed thoughout the execution of a program wheras the variable value keeps on changing.
=> There are no constant in Python, the way they exist in C and Java


===========  String Function ============

Python has a set of built-in methods that you can use on strings. These methods are used to perform operations such as finding, replacing, and formatting strings.

Here are some of the most commonly used Python string methods:

capitalize() - Converts the first letter of a string to uppercase.
center() - Returns a centered string of specified size.
count() - Returns the number of occurrences of a substring in a string.
endswith() - Returns True if a string ends with the given suffix.
format() - Creates a formatted string from the template string and the supplied values.
index() - Returns the index of the first occurrence of a substring in a string.
lower() - Converts all the characters in a string to lowercase.
replace() - Replaces all occurrences of a substring in a string with another substring.
split() - Splits a string into a list of strings based on a delimiter.
strip() - Removes whitespace from the beginning and end of a string.
upper() - Converts all the characters in a string to uppercase.

# capitalize()
string = "hello world"
capitalized_string = string.capitalize()
print(capitalized_string)
# Output: Hello world

# center()
string = "hello world"
centered_string = string.center(20)
print(centered_string)
# Output: 
#        hello world

# count()
string = "hello world"
count = string.count("l")
print(count)
# Output: 2

# endswith()
string = "hello world"
endswith = string.endswith("d")
print(endswith)
# Output: False

# format()
string = "The value is {value}"
formatted_string = string.format(value=10)
print(formatted_string)
# Output: The value is 10

# index()
string = "hello world"
index = string.index("l")
print(index)
# Output: 2

# lower()
string = "HELLO WORLD"
lower_string = string.lower()
print(lower_string)
# Output: hello world

# replace()
string = "hello world"
replaced_string = string.replace("world", "universe")
print(replaced_string)
# Output: hello universe

# split()
string = "hello, world"
split_string = string.split(",")
print(split_string)
# Output: ['hello', 'world']

# strip()
string = "  hello world  "
stripped_string = string.strip()
print(stripped_string)
# Output: hello world

# upper()
string = "hello world"
upper_string = string.upper()
print(upper_string)
# Output: HELLO WORLD

============ If Else Statement ==================
If Else Statement

The Python if else statement is used to execute a block of code if a condition is true, and a different block of code if the condition is false.
if condition:
    # block of code to be executed if condition is true
else:
    # block of code to be executed if condition is false

# check if the user is older than 18
age = 18

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")


=========== Match Case Statement ===============
The Python match case statement is a new feature introduced in Python 3.10. It is used to match a value against a set of patterns and execute a block of code for each pattern that matches.

In this example, the value of the user_type variable is matched against the patterns "student", "teacher", and "staff". If the value of user_type matches one of the patterns, the block of code associated with that pattern will be executed. Otherwise, the block of code associated with the _ pattern will be executed.

The _ pattern is a special pattern that matches any value. It is often used as a catch-all pattern to execute code if none of the other patterns match.

# check if the user is a student, teacher, or staff member
user_type = "student"

match user_type:
    case "student":
        print("You are a student.")
    case "teacher":
        print("You are a teacher.")
    case "staff":
        print("You are staff.")
    case _:
        print("You are not a student, teacher, or staff member.")


===== For Loop ========
A Python for loop is a control flow statement that allows us to execute a block of code repeatedly, until a specific condition is met. The syntax for a for loop is as follows:

for item in sequence:
    # Code block to be executed for each item
    # You can access the current item using the 'item' variable
    # Do something with 'item'

# print the numbers from 0 to 9
for i in range(10):
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oddNum = []
evenNum = []
for num in numbers:
    if num % 2 == 0:
        evenNum.append(num)
    else:
        oddNum.append(num)


print(oddNum, evenNum)

========= While Loop ==================
In Python, a while loop is used to repeatedly execute a block of code as long as a certain condition is true. It allows you to keep executing the code block until the condition becomes false. The general syntax of a while loop in Python is as follows:

num = 1

while num <= 5:
    print(num)
    num += 1


========== Function  ==============
In Python, a function is a block of code that performs a specific task and can be called and executed at any point in a program. Functions allow you to organize your code into reusable components, improving code readability and maintainability.

Defining a Function:
A function in Python is defined using the `def` keyword, followed by the function name, parentheses (which may contain parameters), and a colon. The general syntax for defining a function is as follows:


def function_name(parameter1, parameter2, ...):
    # Code block defining the function
    # Perform some actions
    # Optionally, return a value


Here's an example of a simple function that greets a person by name:


def greet(name):
    print("Hello, " + name + "!")

# Calling the function
greet("Alice")


Output:

Hello, Alice!


In the above example, the `greet` function takes one parameter `name` and prints a greeting message using that name.

Function Parameters:
Functions can have parameters, which are variables that receive values when the function is called. Parameters are defined inside the parentheses during the function definition. They allow you to pass values to the function to work with.

Returning Values:
Functions can also return values using the `return` statement. The `return` statement allows the function to send a value back to the caller. Here's an example:


def add(a, b):
    return a + b

result = add(3, 5)
print(result)


Output:

8


In the above example, the `add` function takes two parameters `a` and `b` and returns their sum using the `return` statement. The returned value is then stored in the `result` variable and printed.

Function Call:
To execute a function, you simply call it by using its name followed by parentheses. You can pass arguments (values) to the function inside the parentheses if the function expects parameters.


function_name(argument1, argument2, ...)


Function call example:


greet("Bob")


Output:

Hello, Bob!


In the example above, the `greet` function is called with the argument `"Bob"`. The function is executed, and the greeting message is printed.

Functions are fundamental building blocks in Python programming that help you write modular, reusable, and efficient code. They allow you to break down complex tasks into smaller, manageable pieces, and make your code more organized and readable.


==== Function with *args and **kwargs ===========
Python functions have several advanced features that enhance their flexibility and capabilities. Here are some of the advanced features commonly used in Python functions:

1. Default Parameters:
   You can assign default values to function parameters. If no argument is provided for a parameter, the default value is used. Here's an example:

   
   def greet(name, greeting="Hello"):
       print(greeting + ", " + name + "!")

   greet("Alice")
   greet("Bob", "Hi")
   

   Output:
   
   Hello, Alice!
   Hi, Bob!
   

   In the above example, the `greet` function has a default parameter `greeting` with the value `"Hello"`. If no value is provided for `greeting`, the default value is used.

2. Variable-Length Arguments:
   Functions can accept a variable number of arguments using special syntax. The `*args` parameter allows you to pass multiple positional arguments, and the `**kwargs` parameter allows you to pass multiple keyword arguments. Here's an example:

   
   def print_arguments(*args, **kwargs):
       for arg in args:
           print(arg)

       for key, value in kwargs.items():
           print(key + ": " + str(value))

   print_arguments("apple", "banana", name="Alice", age=25)
   

   Output:
   
   apple
   banana
   name: Alice
   age: 25
   

   In the above example, the `print_arguments` function accepts multiple positional arguments using `*args` and multiple keyword arguments using `**kwargs`. It then prints the arguments.

3. Lambda Functions (Anonymous Functions):
   Lambda functions are small, anonymous functions that are defined without a name. They are typically used for short, one-line functions. Here's an example:

   
   add = lambda x, y: x + y
   result = add(3, 5)
   print(result)
   

   Output:
   
   8
   

   In the above example, a lambda function is defined and assigned to the `add` variable. The lambda function takes two arguments `x` and `y` and returns their sum.

4. Decorators:
   Decorators are functions that wrap other functions to enhance their functionality. They allow you to modify the behavior of a function without changing its source code. Decorators are denoted by the `@` symbol followed by the decorator name, placed above the function definition. Here's an example:

   
   def uppercase_decorator(func):
       def wrapper():
           result = func()
           return result.upper()

       return wrapper

   @uppercase_decorator
   def greet():
       return "hello, world"

   print(greet())
   

   Output:
   
   HELLO, WORLD
   

   In the above example, the `uppercase_decorator` function is a decorator that converts the result of the decorated function to uppercase. The `greet` function is decorated with `@uppercase_decorator`, so the output is in uppercase.

These are just a few examples of the advanced features available in Python functions. Understanding and utilizing these features can greatly enhance your ability to write powerful and flexible code.


====== List ================
In Python, a list is a built-in data type that represents an ordered collection of items. Lists are mutable, meaning they can be modified after they are created. They can contain elements of different data types, such as integers, floats, strings, or even other lists. Lists are defined using square brackets `[ ]`, and the elements are separated by commas. Here's an example of creating a list:


my_list = [1, 2, 3, 4, 5]


In the above example, `my_list` is a list that contains integers from 1 to 5.

Lists are versatile and offer several useful methods and operations. Here are some common operations you can perform with lists:

Accessing Elements:
You can access individual elements of a list using indexing. The first element is at index 0, the second element at index 1, and so on. Negative indices can be used to access elements from the end of the list. Here's an example:


my_list = [1, 2, 3, 4, 5]
print(my_list[0])    # Output: 1
print(my_list[2])    # Output: 3
print(my_list[-1])   # Output: 5 (last element)


Modifying Elements:
Since lists are mutable, you can modify individual elements by assigning new values to specific indices. Here's an example:

my_list = [1, 2, 3, 4, 5]
my_list[2] = 7
print(my_list)    # Output: [1, 2, 7, 4, 5]


List Methods:
Lists come with several built-in methods that allow you to manipulate and perform operations on them. Some commonly used methods include `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, and `reverse()`. Here's an example:


my_list = [1, 2, 3]
my_list.append(4)         # Add an element at the end
my_list.extend([5, 6])    # Extend the list with another list
my_list.insert(0, 0)      # Insert an element at a specific index
my_list.remove(3)         # Remove the first occurrence of an element
popped_element = my_list.pop()     # Remove and return the last element
my_list.sort()            # Sort the list in ascending order
my_list.reverse()         # Reverse the order of elements
print(my_list)            # Output: [6, 5, 4, 2, 1, 0]


List Slicing:
You can extract a portion of a list using slicing, which allows you to create a new list containing a subset of the original elements. Here's an example:


my_list = [1, 2, 3, 4, 5]
subset = my_list[1:4]    # Extract elements from index 1 to 3 (exclusive)
print(subset)            # Output: [2, 3, 4]


Lists are a fundamental data structure in Python, widely used for storing and manipulating collections of items. They offer flexibility, simplicity, and a rich set of operations that make them suitable for a wide range of programming tasks.



=============== Tuple ==============
In Python, tuples are similar to lists, but they are immutable, meaning their elements cannot be modified once created. Here are some commonly used functions and methods for working with tuples:

1. `len(tuple)`: Returns the number of elements in the tuple.

2. `tuple.count(value)`: Returns the number of occurrences of a value in the tuple.

3. `tuple.index(value, start=0, end=len(tuple))`: Returns the index of the first occurrence of a value in the tuple. You can also specify a start and end index for the search.

4. `tuple + other_tuple`: Concatenates two tuples, creating a new tuple that contains all the elements from both tuples.

5. `tuple * n`: Creates a new tuple by repeating the original tuple n times.

6. `tuple[i]`: Accesses the element at index i in the tuple.

7. `tuple[start:end]`: Returns a new tuple containing elements from start index up to, but not including, the end index.

8. `tuple[:end]`: Returns a new tuple containing elements from the beginning up to, but not including, the end index.

9. `tuple[start:]`: Returns a new tuple containing elements from the start index to the end of the tuple.

10. `tuple[::-1]`: Reverses the order of the elements in the tuple, creating a new tuple.

11. `sorted(tuple)`: Returns a new tuple with the elements sorted in ascending order.

12. `tuple.index(value)`: Returns the index of the first occurrence of a value in the tuple.

These functions and methods provide basic operations for working with tuples in Python. Remember that since tuples are immutable, you cannot modify their elements directly. If you need to modify or manipulate the elements, you may need to convert the tuple to a list, perform the desired operations, and then convert it back to a tuple if necessary.



=========== Sets =============
In Python, a set is an unordered collection of unique elements. Sets are defined using curly braces {} or the set() function. Here are some common operations and methods that you can perform with sets in Python:

my_set = {'sushanta', 1, 2, 'Hello', 3, True}  # Using curly braces
another_set = set([4, 5, 6])  # Using set() function
print(my_set, another_set)
empty_set_wrongway = {}  # you cant't declare empty set. wrong way , OUTPUT : Dict
empty_set = set()  # right way to declare empty set
print(type(empty_set))

Python provides a variety of methods for working with sets, which are unordered collections of unique elements. Here are some commonly used set methods:

#1. `add(element)`: Adds an element to the set if it is not already present.

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

#2. `remove(element)`: Removes the specified element from the set. Raises a `KeyError` if the element is not found.

my_set = {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

#3. `discard(element)`: Removes the specified element from the set if it is present. Unlike `remove()`, it does not raise an error if the element is not found.

my_set = {1, 2, 3, 4}
my_set.discard(2)
my_set.discard(5)  # No error raised
print(my_set)  # Output: {1, 3, 4}


#4. `pop()`: Removes and returns an arbitrary element from the set. Raises a `KeyError` if the set is empty.


my_set = {1, 2, 3, 4}
element = my_set.pop()
print(element)  # Output: 1
print(my_set)  # Output: {2, 3, 4}


#5. `clear()`: Removes all elements from the set, making it an empty set.

my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set)  # Output: set()

#6. `union(other_set)`: Returns a new set that contains all elements from both the set and the `other_set`.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

#7. `intersection(other_set)`: Returns a new set that contains only the elements that are common to both the set and the `other_set`.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

#8. `difference(other_set)`: Returns a new set that contains the elements from the set that are not in the `other_set`.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

#9. `symmetric_difference(other_set)`: Returns a new set that contains the elements that are in either the set or the `other_set`, but not both.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}


These are some of the commonly used set methods in Python. You can refer to the official Python documentation for more information on sets and their methods.

=========== Dictionaries ===================
In Python, a dictionary is a collection of key-value pairs enclosed in curly braces `{}`. It is also known as an associative array or a hash map. Dictionaries are mutable, unordered, and allow duplicate values for keys. Here's an overview of working with dictionaries in Python:

1. Creating a Dictionary:
You can create a dictionary by enclosing comma-separated key-value pairs within curly braces `{}` or by using the `dict()` constructor.


# Using curly braces
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Using dict() constructor
my_dict = dict(key1='value1', key2='value2', key3='value3')


2. Accessing Values:
You can access values in a dictionary using square brackets `[]` and providing the key of the desired value.


my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # Output: John
print(my_dict['age'])  # Output: 25


3. Modifying Values:
To modify the value associated with a key in a dictionary, simply assign a new value to that key.


my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict['age'] = 30
print(my_dict['age'])  # Output: 30


4. Adding a New Key-Value Pair:
To add a new key-value pair to a dictionary, assign a value to a new key.

my_dict = {'name': 'John', 'age': 25}
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}


5. Removing Key-Value Pairs:
There are several methods to remove key-value pairs from a dictionary:

#`del` statement: Deletes a key-value pair from the dictionary.

  my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
  del my_dict['age']
  print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}

# `pop(key)`: Removes the key-value pair specified by the key and returns the corresponding value. Raises a `KeyError` if the key is not found.
  
  my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
  age = my_dict.pop('age')
  print(age)  # Output: 25
  print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}
  
# `popitem()`: Removes and returns an arbitrary key-value pair from the dictionary as a tuple. Raises a `KeyError` if the dictionary is empty.
  
  my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
  item = my_dict.popitem()
  print(item)  # Output: ('city', 'New York')
  print(my_dict)  # Output: {'name': 'John', 'age': 25}
  
# `clear()`: Removes all key-value pairs from the dictionary, making it an empty dictionary.

  my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
  my_dict.clear()
  print(my_dict)  # Output: {}

  
# Accessing Values:
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # Output: John
print(my_dict['age'])  # Output: 25
# Output:  if not found any key to return none
print(my_dict.get('hello'))
# Output: if not found any key to return error
print(my_dict['hello'])

print(my_dict.items())
for key, value in my_dict.items():
    print(key, value, sep=" => ")



# 1. **len()**: Returns the number of key-value pairs in a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))  # Output: 3

# 2. **keys()**: Returns a list containing all the keys in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])

# 3. **values()**: Returns a list containing all the values in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.values())  # Output: dict_values([1, 2, 3])

# 4 . **items()**: Returns a list of tuples containing key-value pairs.

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 5. **get()**: Returns the value associated with a specified key. If the key does not exist, it returns a default value (None by default).

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.get('a'))  # Output: 1
print(my_dict.get('d'))  # Output: None
print(my_dict.get('d', 'Key not found'))  # Output: Key not found

# 6. **pop()**: Removes and returns the value associated with a specified key. If the key does not exist, it returns a default value (if provided) or raises a KeyError.

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.pop('b'))  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}

# 7. **popitem()**: Removes and returns the last inserted key-value pair as a tuple. Raises a KeyError if the dictionary is empty.

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.popitem())  # Output: ('c', 3)
print(my_dict)  # Output: {'a': 1, 'b': 2}

# 8. **clear()**: Removes all key-value pairs from the dictionary, making it empty.

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # Output: {}



"""
For Loop With else condition
Python's `for` loop is a versatile construct that allows you to iterate over elements in a sequence or any iterable object. Here are some advanced features and techniques you can use with `for` loops in Python:

"""
# 1. **Iterating over a range of numbers**: You can use the `range()` function to generate a sequence of numbers and iterate over them.

for i in range(5):
    print(i)  # Output: 0 1 2 3 4
else:
    print('not in i')

# 2. **Iterating over a list or other iterable**: You can iterate over elements in a list, string, tuple, or any other iterable object.

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)  # Output: apple banana cherry

name = "John Doe"
for char in name:
    print(char)  # Output: J o h n   D o e

# 3. **Enumerating elements**: You can use the `enumerate()` function to iterate over elements along with their indices.

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)  # Output: 0 apple   1 banana   2 cherry

# 4. **Iterating over dictionaries**: You can iterate over the keys, values, or key-value pairs of a dictionary using the `items()`, `keys()`, or `values()` methods.

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)  # Output: a b c

for value in my_dict.values():
    print(value)  # Output: 1 2 3

for key, value in my_dict.items():
    print(key, value)  # Output: a 1   b 2   c 3

# 5. **Skipping iterations with `continue`**: You can use the `continue` statement to skip the rest of the code in the current iteration and move to the next iteration.

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Output: 1 3 5 7 9

# 6. **Breaking out of the loop with `break`**: You can use the `break` statement to exit the loop prematurely.

for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0 1 2 3 4

# 7. **Nested loops**: You can have one or more loops inside another loop, allowing you to iterate over multiple dimensions or nested structures.

for i in range(3):
    for j in range(2):
        print(i, j)  # Output: (0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1)



========================
"""
Exception Handling
In Python, errors and exceptions are used to indicate that something unexpected or erroneous has occurred during the execution of a program. Python provides several types of errors, and you can handle them using exception handling mechanisms. Here are some common types of errors and exception handling techniques in Python:
"""
================================
#1. **SyntaxError**: Occurs when there is a mistake in the syntax of the code. It is raised by the Python interpreter during the parsing phase.

# SyntaxError: invalid syntax
print "Hello, World!"


#2. **IndentationError**: Occurs when there is an incorrect indentation in the code. It typically happens when the indentation level is inconsistent.

# IndentationError: unexpected indent
if True:
print("Indentation is important in Python!")


#3. **NameError**: Occurs when a variable or name is not found in the current scope or namespace.

# NameError: name 'x' is not defined
print(x)


#4. **TypeError**: Occurs when an operation is performed on an object of an inappropriate type.

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
x = 5 + "hello"


#5. **ValueError**: Occurs when a function receives an argument of the correct type but an inappropriate value.

# ValueError: invalid literal for int() with base 10: 'abc'
x = int("abc")


#6. **IndexError**: Occurs when you try to access an index that is out of range for a sequence (list, string, tuple).

# IndexError: list index out of range
my_list = [1, 2, 3]
print(my_list[3])


#7. **KeyError**: Occurs when you try to access a dictionary key that doesn't exist.

# KeyError: 'c'
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])


======================
"""
Exception handling allows you to catch and handle these errors gracefully, preventing the program from crashing. The `try-except` statement is used for exception handling in Python.
"""
====================
try:
  # code that might raise an exception
except Exception as e:
  # code to handle the exception

try:
    # Code that may raise an exception
    x = 5 / 0  # ZeroDivisionError: division by zero
except ZeroDivisionError:
    # Handling the specific exception
    print("Cannot divide by zero!")


#You can also use the `else` block to execute code if no exceptions occur, and the `finally` block to specify code that should be executed regardless of whether an exception occurred or not.

try:
    # Code that may raise an exception
    x = 5 / 2
except ZeroDivisionError:
    # Handling the specific exception
    print("Cannot divide by zero!")
else:
    # Code that executes if no exceptions occur
    print("Division successful!")
finally:
    # Code that always executes
    print("Execution complete!")




"""
Raising custom Error using raise keyword : ValueError,Exception, KeyError
To create an error in Python, you can raise an exception explicitly using the `raise` statement. Here's an example of how to create and raise a custom error:

"""


"""In this example, we have a function called `my_function()`. Inside the function, we check for a certain condition using an `if` statement. If the condition is met, we raise a `ValueError` exception using the `raise` statement. The `ValueError` class is a built-in exception class in Python that represents a generic value-related error.

Outside the function, we wrap the call to `my_function()` inside a `try-except` block to catch the `ValueError` exception specifically. If the `ValueError` is raised, the code inside the `except` block will be executed. In this example, we print the error message using `str(e)`, which displays the error message associated with the exception.

You can replace `ValueError` with any other built-in exception class like `TypeError`, `NameError`, or create your own custom exception class by subclassing `Exception`. By raising and catching exceptions, you can effectively handle and communicate errors within your Python code."""


# def my_function(age):
#     # Check for a condition
#     if age < 21:
#         # Raise a custom error
#         raise ValueError("A custom error occurred: you are not a adult")


# # Call the function and catch the error
# try:
#     my_function(20)
# except ValueError as e:
#     print("Custom error occurred:", str(e))



===========================================================
short hand if else statement in python
value_if_true if condition else value_if_false
======================================================
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)


==================== Enumerate Function  =======================
The enumerate() function in Python is a built-in function that allows you to iterate over an iterable (such as a list, tuple, or string) while also providing an index for each item in the iterable. It returns an enumerate object, which can be used in a loop or converted to other data structures.
enumerate(iterable, start=0)

fruits = ['apple', 'banana', 'mango', 'orange']

for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")

