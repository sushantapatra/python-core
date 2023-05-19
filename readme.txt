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

```python
def function_name(parameter1, parameter2, ...):
    # Code block defining the function
    # Perform some actions
    # Optionally, return a value
```

Here's an example of a simple function that greets a person by name:

```python
def greet(name):
    print("Hello, " + name + "!")

# Calling the function
greet("Alice")
```

Output:
```
Hello, Alice!
```

In the above example, the `greet` function takes one parameter `name` and prints a greeting message using that name.

Function Parameters:
Functions can have parameters, which are variables that receive values when the function is called. Parameters are defined inside the parentheses during the function definition. They allow you to pass values to the function to work with.

Returning Values:
Functions can also return values using the `return` statement. The `return` statement allows the function to send a value back to the caller. Here's an example:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

Output:
```
8
```

In the above example, the `add` function takes two parameters `a` and `b` and returns their sum using the `return` statement. The returned value is then stored in the `result` variable and printed.

Function Call:
To execute a function, you simply call it by using its name followed by parentheses. You can pass arguments (values) to the function inside the parentheses if the function expects parameters.

```python
function_name(argument1, argument2, ...)
```

Function call example:

```python
greet("Bob")
```

Output:
```
Hello, Bob!
```

In the example above, the `greet` function is called with the argument `"Bob"`. The function is executed, and the greeting message is printed.

Functions are fundamental building blocks in Python programming that help you write modular, reusable, and efficient code. They allow you to break down complex tasks into smaller, manageable pieces, and make your code more organized and readable.


==== Function with *args and **kwargs ===========
Python functions have several advanced features that enhance their flexibility and capabilities. Here are some of the advanced features commonly used in Python functions:

1. Default Parameters:
   You can assign default values to function parameters. If no argument is provided for a parameter, the default value is used. Here's an example:

   ```python
   def greet(name, greeting="Hello"):
       print(greeting + ", " + name + "!")

   greet("Alice")
   greet("Bob", "Hi")
   ```

   Output:
   ```
   Hello, Alice!
   Hi, Bob!
   ```

   In the above example, the `greet` function has a default parameter `greeting` with the value `"Hello"`. If no value is provided for `greeting`, the default value is used.

2. Variable-Length Arguments:
   Functions can accept a variable number of arguments using special syntax. The `*args` parameter allows you to pass multiple positional arguments, and the `**kwargs` parameter allows you to pass multiple keyword arguments. Here's an example:

   ```python
   def print_arguments(*args, **kwargs):
       for arg in args:
           print(arg)

       for key, value in kwargs.items():
           print(key + ": " + str(value))

   print_arguments("apple", "banana", name="Alice", age=25)
   ```

   Output:
   ```
   apple
   banana
   name: Alice
   age: 25
   ```

   In the above example, the `print_arguments` function accepts multiple positional arguments using `*args` and multiple keyword arguments using `**kwargs`. It then prints the arguments.

3. Lambda Functions (Anonymous Functions):
   Lambda functions are small, anonymous functions that are defined without a name. They are typically used for short, one-line functions. Here's an example:

   ```python
   add = lambda x, y: x + y
   result = add(3, 5)
   print(result)
   ```

   Output:
   ```
   8
   ```

   In the above example, a lambda function is defined and assigned to the `add` variable. The lambda function takes two arguments `x` and `y` and returns their sum.

4. Decorators:
   Decorators are functions that wrap other functions to enhance their functionality. They allow you to modify the behavior of a function without changing its source code. Decorators are denoted by the `@` symbol followed by the decorator name, placed above the function definition. Here's an example:

   ```python
   def uppercase_decorator(func):
       def wrapper():
           result = func()
           return result.upper()

       return wrapper

   @uppercase_decorator
   def greet():
       return "hello, world"

   print(greet())
   ```

   Output:
   ```
   HELLO, WORLD
   ```

   In the above example, the `uppercase_decorator` function is a decorator that converts the result of the decorated function to uppercase. The `greet` function is decorated with `@uppercase_decorator`, so the output is in uppercase.

These are just a few examples of the advanced features available in Python functions. Understanding and utilizing these features can greatly enhance your ability to write powerful and flexible code.


====== List ================
In Python, a list is a built-in data type that represents an ordered collection of items. Lists are mutable, meaning they can be modified after they are created. They can contain elements of different data types, such as integers, floats, strings, or even other lists. Lists are defined using square brackets `[ ]`, and the elements are separated by commas. Here's an example of creating a list:

```python
my_list = [1, 2, 3, 4, 5]
```

In the above example, `my_list` is a list that contains integers from 1 to 5.

Lists are versatile and offer several useful methods and operations. Here are some common operations you can perform with lists:

Accessing Elements:
You can access individual elements of a list using indexing. The first element is at index 0, the second element at index 1, and so on. Negative indices can be used to access elements from the end of the list. Here's an example:

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[0])    # Output: 1
print(my_list[2])    # Output: 3
print(my_list[-1])   # Output: 5 (last element)
```

Modifying Elements:
Since lists are mutable, you can modify individual elements by assigning new values to specific indices. Here's an example:

```python
my_list = [1, 2, 3, 4, 5]
my_list[2] = 7
print(my_list)    # Output: [1, 2, 7, 4, 5]
```

List Methods:
Lists come with several built-in methods that allow you to manipulate and perform operations on them. Some commonly used methods include `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, and `reverse()`. Here's an example:

```python
my_list = [1, 2, 3]
my_list.append(4)         # Add an element at the end
my_list.extend([5, 6])    # Extend the list with another list
my_list.insert(0, 0)      # Insert an element at a specific index
my_list.remove(3)         # Remove the first occurrence of an element
popped_element = my_list.pop()     # Remove and return the last element
my_list.sort()            # Sort the list in ascending order
my_list.reverse()         # Reverse the order of elements
print(my_list)            # Output: [6, 5, 4, 2, 1, 0]
```

List Slicing:
You can extract a portion of a list using slicing, which allows you to create a new list containing a subset of the original elements. Here's an example:

```python
my_list = [1, 2, 3, 4, 5]
subset = my_list[1:4]    # Extract elements from index 1 to 3 (exclusive)
print(subset)            # Output: [2, 3, 4]
```

Lists are a fundamental data structure in Python, widely used for storing and manipulating collections of items. They offer flexibility, simplicity, and a rich set of operations that make them suitable for a wide range of programming tasks.