# what are functions in python?

# Functions are a block of code that only runs when it is called. 
# You can pass data, known as parameters, into a function. A function can return data as a result.
# In Python a function is defined using the def keyword:
# Example
# Create a function named my_function:

def greet():
  print("Hello from a function")

# Call the function:
greet()

# functions can take parameters

def greet(name):
  print(f'Hello {name}')

greet('Alishba')  

# default parameters
def greet(name = 'Guest'):
  print(f'Hello {name}')

greet() # Hello Guest
greet('Alishba')  # Hello Alishba

# functions can return values

def add(a , b):
  return a + b

result = add(2, 3)
print(result)

def make_tea():
  print('Boil water')
  print('Add tea leaves')
  print('Add sugar')
  print('Add milk')
  print('Boil for 5 minutes')
  print('Serve')
  return 'Tea is ready ☕ '

tea = make_tea()
print(tea)  # Tea is ready ☕



# mini project
def call_llm(prompt):
  print(f'User : {prompt}') 
  return 'AI : Hello, How can I help you?'

reposne = call_llm(prompt= 'Hi, My name is Alishba.')  
print(reposne)




# dice roll game
import random

def roll_dice(limit = 6):
  return random.randint(1, limit)


print(roll_dice(40))  
print(roll_dice())