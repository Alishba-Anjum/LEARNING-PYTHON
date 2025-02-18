# Dictionary in python
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Dictionary is a collection of key-value pairs.
# In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value.
# Key and value can be of any type.
# Key must be unique and immutable. Value is mutable.

# Creating a dictionary

student : dict = {
    'name' : "Rohaan",
    'age' : 20,
    'city' : "karachi",
    'roll_no' : 83408
}

print(student['name'])
print(student['age'])   
print(student['city'])
print(student['roll_no'])

# nested dictionary

students = [
    {
        'name' : "Rohaan",
        'age' : 20,
        'city' : "karachi",
        'roll_no' : 83408
    },
    {
        'name' : "Ali",
        'age' : 22,
        'city' : "lahore",
        'roll_no' : 83409
    },
    {
        'name' : "Ahmed",
        'age' : 21,
        'city' : "islamabad",
        'roll_no' : 83410
    },
    {
        'name' : "Asad",
        'age' : 23,
        'city' : "quetta",
        'roll_no' : 83411
    }
]

print(students[0]['name'])
print(students[1]['name'])
print(students[2]['name'])
print(students[3]['name'])


# why we use loops in python?
# Loops are used to repeat a block of code.
# For example, if we want to print the numbers from 1 to 10, we can use a loop.
# There are two types of loops in Python, for loop and while loop.

# for loop
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.

# Syntax of for Loop

for i in range(10):
    print(i)


# loop in list
# We can loop through the list elements using the for loop.

students = ['Rohaan', 'Ali', 'Ahmed', 'Asad']

for student in students:
    print(student)

# while loop
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

# Syntax of while Loop

countdown = 10

while countdown >= 1:
    print(countdown)
    countdown -= 1
 
print('Happy New Year!') 


# guessing game
import random

correct_number = 3
guess = 0

while guess != correct_number:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess == correct_number:
        print("You guessed correctly!")
    else:
        print("Try again!")    

# assignment
# prints numbers in exponential form

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number ** 2)


# uses of while loop and for loop
# while loop is used when we don't know the number of iterations beforehand.
# for loop is used when we know the number of iterations beforehand.
