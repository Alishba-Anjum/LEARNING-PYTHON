# Boolean
# True 0r False

is_logged_in = True
is_logged_out = False

print(is_logged_in) # true
print(is_logged_out) # false
print(type(is_logged_in)) # < class 'bool'>

# comparison operators

# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

num = 10
num2 = 20
print(num == num2) # False
print(num != num2) # True
print(num > num2) # False
print(num < num2) # True
print(num >= num2) # False
print(num <= num2) # True


# Conditions

# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

age = int(input("Enter your age: "))

if ( age < 18 ):
    print( 'you are a minor')
elif ( age == 18):
    print('you are young')
elif ( age >= 70):
    print('you are old')
else:
    print('you are adult')


# Logical Operators
# logical operators are used to combine conditional statements
# there are three logical operators.

# and
# or
# not

# and "both conditions must be true"
# True and True = True
# True and False = False
# False and False = False

percentage = 90

if (percentage >= 90 and percentage <= 100 ):
    print( "your grade is A+" )

elif( percentage >= 80 and percentage <= 90 ):
    print( "your grade is A" ) 

elif( percentage >= 70 and percentage <= 80 ):
    print( "your grade is B" )

elif( percentage >= 60 and percentage <= 70 ):
    print( "your grade is C" )

elif( percentage >= 50 and percentage <= 60 ):
    print( "your grade is D" )

else:
    print( "Failed" )


# or "at least one condition must be true"
# True or True = True
# True or False = True
# False or False = False

people_age  = int(input("Enter your age: "))
people_weight = int(input("Enter your weight: "))

if (people_age >= 18 or people_weight >= 50):
    print("You are eligible to donate blood")
else:
    print("You are not eligible to donate blood")    

# not "reverse the result"
# not True = False
# not False = True

# not

is_logged_in = True
is_logged_out = False

if (not is_logged_in):
    print("Please login to continue")
else:
    print("You are already logged in")        



# assignment

is_hungry = False
burger_lover = True
pizza_lover = False

if (is_hungry and burger_lover or pizza_lover):
    print("You can order food")
elif (not is_hungry):
    print("You are not hungry")
else:
    print("You can't order food")    