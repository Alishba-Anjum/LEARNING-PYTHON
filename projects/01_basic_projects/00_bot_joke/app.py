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