import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

play = input('Do you want to play? Y or N ').lower()
print ('Lets begin!')
    
    

def start_game():
    healthPoints = 10

    print(f' {Fore.GREEN}your starting with {healthPoints} health points')

    choice = input(f'your in a room that has two doors, do you go to the blue door or  yellow door? Ans {Fore.YELLOW}Y {Fore.RESET} or  {Fore.BLUE}B ').lower()
    
    while True:
        if(choice == 'Y'):
            print(f'you chose to through the Yellow door')
        elif(choice == 'B'):
            print(f'you chose to go through the Blue door')
    
        else:
            print('Please choose Y or B')
            start_game()   
        
    
    
    
    
if(play == 'y'):
    
    start_game()
    
else: print('you chose not to play')