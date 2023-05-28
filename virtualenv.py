"""
Create a virtual environment in python :

A virtual environment in Python is a self-contained directory that encapsulates a specific Python environment, including its own Python interpreter, packages, and dependencies. It allows you to create isolated environments for different projects, each with its own set of packages and versions, without interfering with the system-wide Python installation or other projects.
"""

#Here are the basic steps to create and use a virtual environment in Python:

#1. **Create a virtual environment:** Open a terminal or command prompt and navigate to the desired location where you want to create the virtual environment. Then, run the following command:

python -m venv myenv


#This command creates a virtual environment named `myenv` in the current directory.

#2. **Activate the virtual environment:** Depending on your operating system, you need to activate the virtual environment. The activation process sets up the environment variables so that the Python interpreter and packages within the virtual environment are used.

#- **On Windows:**
myenv\Scripts\activate


#- **On macOS and Linux:**
source myenv/bin/activate

#Once activated, your command prompt or terminal should show the name of the virtual environment at the beginning of the prompt (e.g., `(myenv) C:\path\to\project>`).

#3. **Install packages:** Now that you have activated the virtual environment, you can install packages using `pip`. For example:

pip install package_name


#This command installs the specified package into the virtual environment.

#4. **Deactivate the virtual environment:** When you're done working in the virtual environment, you can deactivate it using the following command:

deactivate



#To generate a requirements.txt 
pip freeze > requirements.txt
pip install -r requirements.txt