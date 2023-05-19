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
