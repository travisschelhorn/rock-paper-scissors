# this is the "game.py" file...

from ast import If, NotIn

print("Rock, Paper, Scissors")

print("Welcome to the Rock Paper Scissors Game")

# User Inputs

username = input("Please enter your username:")

print("It's great to meet you",username)

user_selection = input("Please make a selection ('rock', 'paper', 'scissors'):")

# Standardization

user_selection = user_selection.lower() 

print("Your choice: ",(user_selection))

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
# Rock Options
if user_selection == "rock" and computer == "rock":
    print ("It's a tie!")
elif user_selection == "rock" and computer == "paper":
    print ("The computer won. Better luck next time")
elif user_selection == "rock" and computer == "scissors":
    print ("Congratulations! You win!")
# Paper Options
elif user_selection == "paper" and computer == "rock":
    print ("Congratulations! You win!!")
elif user_selection == "paper" and computer == "paper":
    print ("It's a tie!")
elif user_selection == "paper" and computer == "scissors":
    print ("The computer won. Better luck next time")
# Scissor Options
elif user_selection == "scissors" and computer == "rock":
    print ("The computer won. Better luck next time")
elif user_selection == "scissors" and computer == "paper":
    print ("Congratulations! You win!")
elif user_selection == "scissors" and computer == "scissors":
    print ("It's a tie!")

# End of Game
print("This is the end of the game. Thank you for playing.")
