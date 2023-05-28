"""
OS Module 

The `os` module in Python provides a way to interact with the operating system. It offers a wide range of functions for file and directory operations, process management, and other system-related tasks. Here are some commonly used functions and features of the `os` module:

1. File and Directory Operations:
   - `os.getcwd()`: Returns the current working directory.
   - `os.chdir(path)`: Changes the current working directory to the specified path.
   - `os.listdir(path)`: Returns a list of files and directories in the specified path.
   - `os.mkdir(path)`: Creates a directory at the specified path.
   - `os.remove(path)`: Deletes the file at the specified path.
   - `os.rename(src, dst)`: Renames a file or directory from `src` to `dst`.
   - `os.path.isfile(path)`: Checks if the specified path is a file.
   - `os.path.isdir(path)`: Checks if the specified path is a directory.

2. Environment Variables:
   - `os.getenv(var_name)`: Returns the value of the environment variable `var_name`.
   - `os.environ`: A dictionary-like object that contains the current environment variables.

3. Process Management:
   - `os.system(command)`: Executes the command in the system shell.
   - `os.spawnl(mode, path, ...)`: Spawns a new process using the specified mode and path.
   - `os.kill(pid, signal)`: Sends a signal to the process with the specified process ID (PID).

4. Miscellaneous:
   - `os.path.join(path, *paths)`: Joins one or more path components intelligently.
   - `os.path.exists(path)`: Checks if the specified path exists.
   - `os.path.abspath(path)`: Returns the absolute path of the specified path.
   - `os.path.basename(path)`: Returns the base name of the specified path.
   - `os.path.dirname(path)`: Returns the directory name of the specified path.

These are just a few examples of the functions and features provided by the `os` module. You can refer to the Python documentation for the `os` module for more details and additional functionalities: https://docs.python.org/3/library/os.html
"""

import os

# # Get the current working directory
current_dir = os.getcwd()
# print("Current directory:", current_dir)

# # List all files and directories in the current directory
# file_list = os.listdir(current_dir)
# print("Files and directories in current directory:")
# for item in file_list:
#     print(item)

# # Create a new directory
# new_dir = os.path.join(current_dir, "new_directory")
# os.mkdir(new_dir)
# print("New directory created.")

# # Remove a  directory
# new_dir = os.path.join(current_dir, "new_directory")
# os.rmdir(new_dir)
# print("New directory deleted.")

# # Rename a file
# old_file = os.path.join(current_dir, "old_file.txt")
# new_file = os.path.join(current_dir, "new_file.txt")
# with open(old_file, 'w') as file:
#     file.write("This is the old file.")
# os.rename(old_file, new_file)
# print("File renamed.")

# # Check if a path is a file or directory
# path = os.path.join(current_dir, "new_file.txt")
# if os.path.isfile(path):
#     print(f"{path} is a file.")
# elif os.path.isdir(path):
#     print(f"{path} is a directory.")

# # Execute a system command
# os.system("ls")

# # Get the value of an environment variable
# home_dir = os.getenv("HOME")
# print("Home directory:", home_dir)

# # Check if a path exists
# existing_path = os.path.join(current_dir, "existing_file.txt")
# nonexistent_path = os.path.join(current_dir, "nonexistent_file.txt")
# print("Existing path exists:", os.path.exists(existing_path))
# print("Nonexistent path exists:", os.path.exists(nonexistent_path))
