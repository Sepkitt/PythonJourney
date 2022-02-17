import random
from words import words



# this project are variables, random, integer, strings, char, input and output, and boolean. 
# In the game, users have to enter letter guesses, and each user will have a limited number of guesses
# (a counter variable is needed for limiting the guesses). 

# You can create a pre-organized list of words that users can grab words from. 
# Also, you must include specific functions to check whether or not a user has entered a single 
# letter or if the input letter is in the hidden word, to if the user has actually 
# inputted a single letter, and to print the correct outcomes (letters).



def hangman():
    # get a random word
    hidden_word = random.choice(words).lower()
    #ask the user to either enter a letter or guess the secrate word
    guesses = 0
    max_guesses = 10
    
    while guesses < max_guesses:
        guess = input('Guess the word ').lower()
        hint = hidden_word.len()
        print(f'the hidden word has {hint} letters')
        if guess in hidden_word:
            guesses = guesses +1
            print (f'the letter {guess} is in the hidden word')
            print(f'you have used {guesses} guesses ')
            #tell the user the amount of guesses left
            guesses_left = max_guesses - guesses
            print(f'You have {guesses_left} guesses left')
            
            #Ask user if they want to guess the hidden word
            guess_hidden_word = input('Do you want to guess the hidden word? Y/N ').lower()
            if(guess_hidden_word == 'y'):
                # Ask user what they think the hidden word is
                guess_word = input('What is the hidden word? ').lower()
                if guess_word == hidden_word:
                    print('you guessed the hidden word hooray!!')
                    break
                else:
                    guesses = guesses +1 
                    print(f'{guess_word} is not the hidden word')
                    guesses_left = max_guesses - guesses
                    print(f'You have {guesses_left} guesses left') 
            elif(guess_hidden_word == 'n'):
                print(f'you still have {guesses_left} guesses left')
                continue
        
        else:
            guesses = guesses +1
            print(f'hidden word does not contain {guess}')
            print(f'you have used {guesses} guesses ')
            #tell the user the amount of guesses left
            guesses_left = max_guesses - guesses
            print(f'You have {guesses_left} guesses left')
            
    print(f'you dont have anymore guesses, the hidden word was {hidden_word}')
    
hangman()
