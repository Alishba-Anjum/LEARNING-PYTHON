# What is 4 pillars of OOP?
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism

# What is Encapsulation 🛡️

# The practice of bundling data (variables) and methods (functions) that operate on the data into a single unit (a class).
# It restricts direct access to some of an object's components, which helps prevent accidental modifications.
# Example:

class Car:
    __make : str # Private variable (cannot be accessed directly)
    model : str
    year : int

    def __init__(self, make, model, year):
        self.__make = make
        self.model = model
        self.year = year


car = Car("Toyota", "Camry", 2022)
# print(car.__make) # This will raise an AttributeError

# What is Abstraction 🎭

# Hides complex implementation details and exposes only essential features.
# Achieved using abstract classes and methods (via the abc module).
# Example:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

dog = Dog()
print(dog.make_sound())

# What is Inheritance 🔄

# Allows a class (child) to inherit attributes and methods from another class (parent).
# Enables code reuse and hierarchy creation.
# Example:

class Student:
    name: str
    age: int
    roll_no: int

    def __init__(self, name, age, roll_no): # constructor method
        self.name = name
        self.age = age
        self.roll_no = roll_no

class Teacher(Student):
    subject: str

    def __init__(self, name, age, roll_no, subject): # constructor method
        super().__init__(name, age, roll_no)
        self.subject = subject  

teacher = Teacher("Rohaan", 20, 83408, "Computer Science")
print(teacher.name)
print(teacher.age)  
print(teacher.roll_no)
print(teacher.subject)            

# What is Polymorphism 🔄➡️🔄

# Allows objects of different classes to be treated as objects of a common superclass.
# The same function or method name can have different implementations.
# Example:

class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Bark!"
    
# The Cat class has a method speak() that returns "Meow!".
# The Dog class has a method speak() that returns "Bark!".
# Both classes have the same method name (speak), but they return different values.
# This is an example of Polymorphism, where different classes share the same method name but behave differently.    

def animal_sound(animal):
    return animal.speak()

# This function takes an object (animal) as an argument.
# It calls the speak() method of the passed object.
# Since both Cat and Dog have a speak() method, this function can work with both.

print(animal_sound(Cat()))  # Meow!
print(animal_sound(Dog()))  # Bark!

