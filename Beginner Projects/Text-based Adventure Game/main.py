import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def start_game():
    healthPoints = 10
    equipped = 'nothing'

    print(
        f'You are an elite soldier tasked with saving the princess, your starting with {Fore.GREEN}{healthPoints}{Fore.RESET} health points')

    answer = input(f'{Fore.CYAN}You are standing on a platform, and a monster is chasing you from the left side, do you go left or right?{Fore.RESET} ({Fore.YELLOW}left{Fore.RESET}/{Fore.GREEN}right{Fore.RESET})').lower().strip()

    while healthPoints > 1:
        if(answer == 'left'):
            healthPoints = 0
            print(f'you chose to left and the monster eats you')

        elif(answer == 'right'):
            print(
                f'{Fore.CYAN}You go right and you see a pipe that leads down to the sewers')
            answer = input(
                f'Do you go down the pipe or go forward ({Fore.YELLOW}forward{Fore.RESET}/{Fore.GREEN}down{Fore.RESET})').lower().strip()

            if(answer == 'forward'):
                print(f'{Fore.CYAN}You Chose to go forward and you see three different Items{Fore.RESET}. A red glowing {Fore.RED}Apple{Fore.RESET} a green vibrating {Fore.GREEN}Flower{Fore.RESET} and a bright Yellow star shaped {Fore.YELLOW}Cookie{Fore.RESET}')
                answer = input(
                    f'Which item do you choose? ({Fore.CYAN}Apple{Fore.RESET}, {Fore.YELLOW}Flower{Fore.RESET}, {Fore.GREEN}Cookie{Fore.RESET})').lower().strip()

                if(answer == 'flower'):
                    print(
                        f'{Fore.CYAN}You equipped the flower and you start glowing gold but you lost{ Fore.RESET}{ Fore.RED}3 health')
                    healthPoints -= 3
                    equipped = 'flower'
                    print(f'Your total health points is {healthPoints}')
                    answer = input(
                        f'You have to choose if you want to go back to the sewers or go continue going forward. ({Fore.YELLOW}forward{Fore.RESET}/{Fore.GREEN}down{Fore.RESET})').lower().strip()

                    if(answer == 'forward'):
                        print('You go forward and you encounter')
                        
                    # Go back to Sewers
                    elif(answer == 'down'):
                        sewers(equipped)
                    else:
                        undecided()

                elif(answer == 'cookie'):
                    print(
                        f'{Fore.CYAN}You Eat the cookie and you start glowing, The cookie allowed you to gain immunity to all damage')
                    answer = input(
                        f'Do you go back to the pipe down to the sewers or do you continue to move forward?  ({Fore.YELLOW}forward{Fore.RESET}/{Fore.GREEN}down{Fore.RESET})').lower().strip()
                    # Go back down the sewers
                    equipped = 'cookie'
                    if(answer == 'down'):
                        sewers(equipped)
                    elif(answer == 'forward'):
                        forward()
                        
                elif(answer == 'apple'):
                    healthPoints = 0
                    print(f'The apple was extremely poisonous and it causes you to collapse, the monster that was chasing you at the beginning caught up to you and you were eaten')
                else:
                    undecided()

            elif(answer == 'down'):
                print(
                    f'{Fore.CYAN}You went down the pipe through the sewers and come across a small monster')
                answer = input('Do you ATTACK or RUN (attack or run)')

        else:
            print('Please choose left or right')
            start_game()

    print(' You have run out of health and has sadly passed away, rest in peace soldier')


# sewer room
def sewers(equipped):
    print(f' you have the {equipped} equipped')
    print(f'{Fore.CYAN}You went down the pipe through the sewers and come across a small monster')
    answer = input(f'Do you ATTACK or RUN (attack or run)')
    
    if equipped == '' and answer == 'attack':
        print('You tried to attack the monster but you have no weapon and died a miserable death')
        
    #   if(equipped == 'Flower')
    if(answer == 'attack'):
        print('')
        
#forward
def forward():
    print(f'{Fore.CYAN} You went forward and come across two paths') 
    answer = input(f'Do you go left or right? (Left/Right')

    

# undecided
def undecided():
    healthPoints = 0
    print(f'You were unable to decide a proper item. The monster that was chasing you at the beginning caught up to you and you were eaten')

while True:
    answer = input(
        f'Do you want to play? ({Fore.GREEN}yes{Fore.RESET}/{Fore.RED}no{Fore.RESET}) ').lower().strip()

    if(answer == 'yes'):

        start_game()
    elif(answer == 'no'):
        print('you chose not to play')
        break
    else:
        print('Please choose (Yes/No)')
        continue
