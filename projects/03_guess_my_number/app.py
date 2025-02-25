# guess my number game
import random


    
my_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10")
print("Can you guess it?")
print("Enter a number between 1 and 10")

user_guess = int(input("Enter a number between 1 and 10: "))
chances = 5

while chances > 0:
    if user_guess > my_number:
        print("your guess is too high")
    elif user_guess < my_number:
        print("your guess is too low")
    else:
        print("Congratulations! You win the number was", my_number)    
        break
    chances -= 1
    print("You have", chances, "chances left")
    user_guess = int(input("Enter a number between 1 and 10: "))

