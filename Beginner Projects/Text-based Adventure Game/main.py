import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

answer = input('Do you want to play? (yes / no) ').lower().strip()
print ('Lets begin!')
    
    

def start_game():
    healthPoints = 10

    print(f'You are an elite soldier tasked with saving the princess, your starting with {Fore.GREEN} {healthPoints}{Fore.RESET} health points')

    answer = input(f'you are standing on a platform, and a monster is chasing you from the left side, do you go left or right? ( {Fore.YELLOW}left {Fore.RESET} or  {Fore.BLUE} right )').lower().strip()
    
    while healthPoints > 1:
        if(answer == 'left'):
            healthPoints = 0
            print(f'you chose to left and the monster eats you')
        elif(answer == 'right'):
            print(f'you chose to go through the Blue door')
    
        else:
            print('Please choose left or right')
            start_game()   
            
    print(' You have run out of health and has sadly passed away, rest in peace soldier')   
    
    
    
    
if(answer == 'yes'):
    
    start_game()
    
else: print('you chose not to play')