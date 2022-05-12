import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string

def emailSlicer(email):
    username, _,domain = email.strip().partition('@')
    return f'Your username is {Fore.CYAN}{username}{Fore.RESET} and your domain is {Fore.CYAN}{domain}{Fore.RESET}'

user_input = input("What is your Email: ")

print(emailSlicer(user_input))