"""
Comments In Python
# this is a single line comment
multiline comment stater (''' ''' or """ """)
"""

"""
Escape Sequences
In Python, escape sequences are special characters that are used to represent certain actions or characters that cannot be easily entered or printed directly. They are typically represented by a backslash followed by a specific character or combination of characters. Here are some common escape sequences in Python:

"""
# \\: Backslash
print("This is a backslash: \\")
# \': Single quote
print('He said, \'Hello!')
# \": Double quote
print("She said, \"Hi!")
# \n: Newline
print("Hello\nWorld!")
# \t: Horizontal tab
print("Name:\tJohn")
# \r: Carriage return
print("Hello\rWorld!")
# \b: Backspace
print("Hello\bWorld!")
# \f: Form feed
print("Hello\fWorld!")
# \v: Vertical tab
print("Hello\vWorld!")
# \a: ASCII bell
print("\aBeep!")
# \ooo: Octal value (where "ooo" is an octal number)
print("\110\145\154\154\157")
# \xhh: Hexadecimal value (where "hh" is a hexadecimal number)
print("\x48\x65\x6c\x6c\x6f")


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
print("Hello, world!")
# Output: Hello, world!

name = "Alice"
age = 25
print("Name:", name, "Age:", age)
# Output: Name: Alice Age: 25

print(1, 2, 3, 4, sep=' | ', end='!')
# Output: 1 | 2 | 3 | 4!

file = open('readme.txt', 'w')
print("Hello, file!", file=file)
file.close()
