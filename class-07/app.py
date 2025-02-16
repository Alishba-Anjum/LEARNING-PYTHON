# what are functions in python?

# Functions are a block of code that only runs when it is called. 
# You can pass data, known as parameters, into a function. A function can return data as a result.
# In Python a function is defined using the def keyword:
# Example
# Create a function named my_function:

def my_function():
  print("Hello from a function")

# Call the function:
my_function()

# functions can take parameters

def my_function(name):
  print(f'Hello {name}')

my_function('Alishba')  

# functions can return values

def add(a , b):
  return a + b

result = add(2, 3)
print(result)