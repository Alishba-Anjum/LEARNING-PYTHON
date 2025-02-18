# file handling in python
# open() function
# open() function is used to open a file and return a file object
# file object is used to read, write, and close the file
# file object is created using the open() function
# open() function takes two arguments: file name and mode
# mode is used to specify the purpose of opening the file
# mode can be read, write, append, etc.

# Example
# In this example, we are opening a file called Alishba.txt in write mode and writing some text to it.

file = open('Alishba.txt', 'w') # w is used to write in the file
file = open('Alishba.txt', 'r') # r is used to read the file
file = open('Alishba.txt', 'a') # a is used to append the file
file.write("\nHello, Alishba")
file.close()

# Example 2

with open('Alishba.txt', 'a+') as newfile:
    newfile.write("\nHello, Alishba")
    newfile.seek(0)                 
    print(newfile.read())

