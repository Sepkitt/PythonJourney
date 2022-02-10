# Generate a random number each dice the program runs, and the users can use the dice repeatedly for as long as he wants. 
# When the user rolls the dice, the program will generate a random number between 1 and 6 (as on a standard dice).
#The number will then be displayed to the user. It will also ask users if they would like to roll the dice again. 
# The program should also include a function that can randomly grab a number within 1 to 6 and print it. 
# This beginner-level python projects will help build a strong foundation for fundamental programming concepts.

import random

# set a variable to true (this will be used to run the while loop)
play = True

# Create a function that will select a random number within 1 to 6 and print it
def dice_simulator():
        random_number = random.randint(1, 6)
        print (random_number)
   
# add a while loop that will ask the user if they want to play.

while play:
    answer = input('Would you like to roll the dice? ').lower()
    # If the user answer is 'y' the dice simulator will run

    if answer == 'y':
        dice_simulator()
        
    # If the user answer is 'n' End the function

    elif answer == 'n':
        print('Thanks for playing')
        break
    
    # If the user answer is 'not y or n' Tell the user they can only use y or n

    else:
        print('Please enter y or n')




