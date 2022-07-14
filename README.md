# rock-paper-scissors

This command line Python application will allow a human user to participate in a game of Rock-Paper-Scissors with a computer opponent that will make random selections.

# Setup

In order to set up the game, either cloan or download this [remote repository](https://github.com/travisschelhorn/rock-paper-scissors) onto your computer.  Remember the location of where it is saved.  After cloning the repo, navigate there from the command-line:

```
cd ~/Desktop/rock-paper-scissors
```

Create a virtual environment

```
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```
conda activate rpos-env
```

Install package dependencies within the virtual environment

```
pip install -r requirements.txt
```

# Game Play
Play a game

```
python game.py
```

Choose a username for your player (e.g. 'John Doe')

```
Username="John Doe" python game.py
```

Make your selection

```
user_selection = input("Please make a selction ('rock', 'paper', 'scissors'):")
```

Simulate Computer Selection

The application should select one of the options (i.e. "rock", "paper", or "scissors") at random, and assign that as the computer player's choice.


```
computer = (random.choice(options))
```
# Determining the Winner
The application should compare the user's selection to the computer player's selection, and determine which selection is the winner. The following logic should govern that determination:


+ Rock beats Scissors
+ Paper beats Rock
+ Scissors beats Paper
+ Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"


# Displaying Results
An example of a dsired output after one game:

```
Rock, Paper, Scissors
Welcome to the Rock Paper Scissors Game
Please enter your username: Travis
It's great to meet you  Travis
Please make a selection ('rock', 'paper', 'scissors'):rock
Your choice:  rock
Computer chose scissors
Congratulations! You win!
This is the end of the game. Thank you for playing.
```

