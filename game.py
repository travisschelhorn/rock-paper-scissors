# this is the "game.py" file...

from ast import If, NotIn


print("Rock, Paper, Scissors")

print("Welcome to the Rock Paper Scissors Game")

# User Inputs

user_selection = input("Please make a selction ('rock', 'paper', 'scissors'):")

# Standardization

user_selection = user_selection.lower() 

print("your choice: ",(user_selection))


# Options 
options = ["rock", "paper", "scissors"]

if user_selection not in options:
    print("Sorry. Your choice is invalid")
    exit()


# Computer Selection

import random
random.random()

computer = (random.choice(options))

print("Computer chose", (computer))

# Determining the Winner



# End of Game
print("This is the end of the game. Thank you for playing")
