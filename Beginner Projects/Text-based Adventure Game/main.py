import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

answer = input('Do you want to play? (yes / no) ').lower().strip()
print ('Lets begin!')
    
    

def start_game():
    healthPoints = 10

    print(f'You are an elite soldier tasked with saving the princess, your starting with {Fore.GREEN}{healthPoints}{Fore.RESET} health points')

    answer = input(f'You are standing on a platform, and a monster is chasing you from the left side, do you go left or right? ({Fore.YELLOW}left{Fore.RESET}/{Fore.GREEN}right{Fore.RESET})').lower().strip()
    
    while healthPoints > 1:
        if(answer == 'left'):
            healthPoints = 0
            print(f'you chose to left and the monster eats you')
            
        elif(answer == 'right'):
            print(f'{Fore.CYAN}You go right and you see a pipe that leads down to the sewers')
            answer = input(f'Do you go down the pipe or go forward ({Fore.YELLOW}forward{Fore.RESET}/{Fore.GREEN}down{Fore.RESET})').lower().strip()
            
            if(answer == 'forward'):
              print(f'{Fore.CYAN}You Chose to go forward and you see three different Items{Fore.RESET}. A red glowing {Fore.RED}Apple{Fore.RESET} a green vibrating {Fore.GREEN}Flower{Fore.RESET} and a bright Yellow star shaped {Fore.YELLOW}Cookie{Fore.RESET}')
              answer = input(f'Which item do you choose? ({Fore.CYAN}Apple{Fore.RESET}, {Fore.YELLOW}Flower{Fore.RESET}, {Fore.GREEN}Cookie{Fore.RESET})').lower().strip()
              
              if(answer == 'flower'):
                  print(f'')
                  
              elif(answer == 'cookie'):
                  print(f'')
                  
              elif(answer == 'apple'): 
                  healthPoints = 0
                  print(f'The apple was extremely poisonous and it causes you to collapse, the monster that was chasing you at the beginning caught up to you and you were eaten')
              else: 
                  print(f'Please Choose ({Fore.CYAN}Apple{Fore.RESET}, {Fore.YELLOW}Flower{Fore.RESET}, {Fore.GREEN}Cookie{Fore.RESET})')
                  continue
                  
            elif(answer == down):
               print(f'{Fore.CYAN}You went down the pipe through the sewers and come across a small monster')
               answer = input('Do you ATTACK or RUN')

                
        else:
            print('Please choose left or right')
            start_game()   
            
    print(' You have run out of health and has sadly passed away, rest in peace soldier')   
    
    
    
    
if(answer == 'yes'):
    
    start_game()
    
else: print('you chose not to play')