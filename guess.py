# ------------------------------------------------------------------------------
# Guess The Number Lab
# User need to enter an integer number between 1 and 10.
# After they input the data, the program will show them the correct answer and
# guess entered by the user.
# ------------------------------------------------------------------------------

import random

# Tell the user they need to think a number between 1 and 10.Randomly generated 
# an integer between 1 and 10.
print("I am thinking of a number between 1 and 10.")
number = random.randint(1, 10)  # Random integer number generator

# Prompt and collect what does the user guess.
guess = input("What is the number?") 

# Show the user correct answer and what does they guessed.
print("The number was", str(number) + ".")
print("You guessed", str(guess) + ".")
