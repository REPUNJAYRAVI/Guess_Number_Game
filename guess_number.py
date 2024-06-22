#importing game logo from art page
from art import guess_game
#importing randint module for generating random numbers
from random import randint

#generating random int number which will be fixed throughout the game
original_number = randint(1, 100)

#defining function for number comparison
def userguess(guess_number):
    if guess_number > original_number:
        print("You are away from Original Number")
    elif guess_number < original_number:
        print("You are near to Original Number")
    elif guess_number == original_number:
        print(f"You Won! The original number is {original_number}")

def game_mode():
    global user_chance
    game_level = input("Choose the level of game, Easy or Hard?:\n")
    if game_level.lower() == "easy":
        # You will get total 10 chances to guess the number
        user_chance = 10  
    elif game_level.lower() == "hard":
        # You will get total 5 chances to guess the number
        user_chance = 5
    else:
        print("Please enter a valid input for the level of the game")
        game_mode()  # Recursively call to prompt again if input is invalid

#printing game logo
print(guess_game)
#printing declaration of game
print("""Welcome to the Number Guessing Game.
The computer is thinking of a number between 1 and 100.
It has generated a random number that you need to guess!""")

# Initializing user_chance variable
user_chance = 0

# Setting the game mode to determine user_chance
game_mode()

# Starting the guessing loop
for i in range(user_chance):
    print(f"You have {user_chance - i} chances left")
    guess_number = int(input("Enter your number: "))
    userguess(guess_number)
    if guess_number == original_number:
        break
else:
    print(f"Game over! You Lost The original number was {original_number}.")
