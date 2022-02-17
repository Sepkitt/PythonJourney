from doctest import SKIP
import random
from unittest import skip
import colorama
from colorama import Fore, Back, Style
from words import words

# use autoreset=True to reset color style
colorama.init(autoreset=True)
#Colorama colors

'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''


def hangman():
    # get a random word
    hidden_word = random.choice(words).lower()
    #ask the user to either enter a letter or guess the secrate word
    guesses = 0
    max_guesses = 10
    guesses_left = 0
    while guesses < max_guesses:
        #show the user the length of the hidden word as a hint
        hint = len(hidden_word)
        print(f'the hidden word has {Fore.YELLOW}{hint}{Fore.RESET} letters')

        
        #Show the user the total guesses they start with
        if guesses_left == 0:
            print( f'You start with {Fore.GREEN}{max_guesses}{Fore.RESET} guesses')
        else :
            # Use guess instead of guesses when the guesses variable == 1
            if guesses == 1:
                print(f'you have used {Fore.RED}{guesses}{Fore.RESET} guess ')
            else:
                print(f'you have used {Fore.RED}{guesses}{Fore.RESET} guesses ')


        # Convert User input to lower case
        guess = input('Guess the word ').lower()
        # Check if user just submitted an answer without entering a letter
        if not(guess):
            print(f'{Fore.RED} No white spaces Allowed{Fore.RESET}:\n Please enter valid text only')
            continue
         #By using str. isalpha() you can check if it is a letter

        elif not(guess.isalpha()):
            print(f'{Fore.RED} Please enter valid text only')
            continue
        
        #USE str.isspace() to check if a string is empty
    
        elif(guess.isspace()):
            print(f'{Fore.RED} Please enter valid text only')
            continue

            

        if guess in hidden_word:
            guesses = guesses +1
            print (f'the letter {Fore.GREEN}{guess}{Fore.RESET} is in the hidden word')
            
            #tell the user the amount of guesses left
            guesses_left = max_guesses - guesses
            print(f'You have {guesses_left} guesses left')
            
            # Ask user if they want to guess the hidden word
            guess_hidden_word = input(f'Do you want to guess the hidden word? {Fore.YELLOW}Y/N{Fore.RESET} ').lower()
            
            if(guess_hidden_word == 'y'):
                # Ask user what they think the hidden word is
                guess_word = input('What is the hidden word? ').lower()
                if guess_word == hidden_word:
                    print(f'{Fore.GREEN} you guessed the hidden word {Style.BRIGHT}hooray!!')
                    break
                else:
                    # if the user guessed the hidden word incorectly, keep track of the amount of guesses used
                    guesses = guesses +1 
                    print(f'{Fore.RED}{guess_word}{Fore.RESET} is not the hidden word')
                    # Subtract the max_guesses with the current value of guesses to show the amount of guesses left
                    guesses_left = max_guesses - guesses
                    print(f'You have {Fore.GREEN}{guesses_left}{Fore.RESET} guesses left') 
                    
            elif(guess_hidden_word == 'n'):
                # Continue the game if the user does not want to guess the hidden word
                print(f'{Fore.GREEN}You have selected to continue without guessing the hidden word')
                continue
        
        else:
            guesses = guesses +1
            print(f'hidden word does not contain the letter {Fore.GREEN}{guess}{Fore.RESET}')

            #tell the user the amount of guesses left
            guesses_left = max_guesses - guesses
            print(f'You have {Fore.GREEN}{guesses_left}{Fore.RESET} guesses left')
            
    # When the user runs out of guesses, show the hidden word        
    print(f'you dont have anymore guesses, the hidden word was {Fore.CYAN}{hidden_word}{Fore.RESET}')
    
hangman()
