# Standard Library Imports
import random
import datetime 
import os # Importing the os module to use its functions
import math # Importing the math module to use its functions

#1. Generate a random number between 0 and 10
random_number = random.randint(0, 10)
print(f"Random number between 0 and 10: {random_number}")

#2. Get and format the current date/time
now = datetime.datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current time: {formatted_time}")

#3. Print the currnet working directory and PATH variable
cwd = os.getcwd()
path_environment = os.environ.get('PATH')
print(f"Current working directory: {cwd}")
print(f"PATH environment variable: {path_environment}")

#4. Print the value of pi and a square root
print(f"Value of pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

