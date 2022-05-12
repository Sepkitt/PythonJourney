import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

email = input('What is your email ').strip()

# Without : operator the code will only show that specific characters index value
# The : operator is like a while card so for example :email.index('@') will display all the characters that comes  before @

username = email[:email.index('@' )]
domain = email[email.index('@' ) + 1:]

print(f'Your username is {Fore.CYAN}{username}{Fore.RESET} and your domain is {Fore.CYAN}{domain}{Fore.RESET}')