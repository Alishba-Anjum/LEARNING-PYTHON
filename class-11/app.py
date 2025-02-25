#  What is object oriented programming in Python?

# Object-oriented programming (OOP) is a programming paradigm that uses objects and their interactions to model real-world entities.
# It is a way of structuring code to make it easier to understand and maintain.
# It is a way of organizing code to make it easier to reuse and scale.
# It is a way of organizing code to make it easier to debug, test and maintain.    
    
# What is class in Python?
# A class is a blueprint for creating objects.

# What is object in Python?
# An object is an instance of a class.

# What is constructor in Python?
# A constructor is a special method that is called when an object is created.

# What is self in Python?/
# The self parameter is a reference to the current instance of the class.

class Student: # class
    name: str
    fname: str
    age: int
    roll_no: int

    def __init__(self, name, fname, age, roll_no): # constructor method
        self.name = name
        self.fname = fname
        self.age = age
        self.roll_no = roll_no
   
student1 = Student("Rohaan", "Umair", 20, 83408) # object
print(student1.name)
print(student1.fname)
print(student1.age)
print(student1.roll_no)

student2 = Student("Ali", "Khan", 20, 83411)
print(student2.name)
print(student2.fname)
print(student2.age)
print(student2.roll_no)

print(student1)


class Student: # class
    name: str
    fname: str
    age: int
    roll_no: int

    def __init__(self, name, fname, age, roll_no): # constructor method
        self.name = name
        self.fname = fname
        self.age = age
        self.roll_no = roll_no

    def ring_bell(self):
        print("Ring ring")    
   
student1 = Student("Rohaan", "Umair", 20, 83408) # object
print(student1.name)
student1.ring_bell()