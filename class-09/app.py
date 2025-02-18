#  what is Error Handling in Python?

# Error handling in Python is a way of handling errors that may occur during the execution of a program. 
# It allows you to continue running the program even if there is an error.
# You can use try and except blocks to handle errors.

# Example
# In this example, we are trying to divide a number by zero.   

try:
    num  = int(input("Enter a number: "))
    print(num / 0)
except ZeroDivisionError:
    print("You can't divide by zero")

except ValueError:
    print("Please enter a number")
except Exception as e:
    print(e)    


# Module in Python

# A module is a file containing Python code. A module can define functions, classes, and variables.
# A module can also include runnable code.
# You can use a module by importing it into your program.
# You can also import specific functions or variables from a module.
# You can also create your own modules and import them into your program.

# Example
# In this example, we are importing the math module and using the sqrt function to calculate the square root of a number.

import math

num = 25

print(int(math.sqrt(num)))

# Example
# In this example, we are importing the random module and using the randint function to generate a random number between 1 and 10.

import random

print(random.randint(1, 10))

# Example
# In this example, we are importing the math module and using the pi variable to calculate the area of a circle.

import math

radius = 7 
area = math.pi * radius ** 2
print(area)

# Example
# In this example, we are creating our own module called mymodule.py and importing it into our program.

# mymodule.py

import mymodule
from mymodule import greet

print(mymodule.greet("Rohaan"))


# projects
# Create a Python program that tells a joke when the user asks for it.

JOKE = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs.'"
SORRY = "Sorry, I only tell jokes."
PROMPT = "WHAT YOU WANT?"

def bot():
    try:
        user_input = input(PROMPT)
        if 'joke' in user_input.lower():
            print(JOKE)
        else:
            print(SORRY)    
       
    except ValueError:
        print("Enter a valid input.")

bot()