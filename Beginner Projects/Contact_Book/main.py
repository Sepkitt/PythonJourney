#The objective of this project is to create an Address book using python in which the user can add a new contact 
# Edit and delete existing contact and view all the contact.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

contact = {}
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

options =  f"""
{Fore.CYAN} Contact Book Application{Fore.RESET}
    1. Add new contact
    2. Search contact
    3. Display contact
    4. Edit contact
    5. Delete contact
    6. Exit
"""
while True:
    # Display contact Details
    def contactDetails():
        print(f"{Fore.GREEN}Contact Details{Fore.RESET}")
        display_contact()

    # user prompt
    choice = int(input(options))

    # Add Contact
    if choice == 1:
        name = input("Enter the contact name ").capitalize()
        phone = input("Enter the mobile number ")
        contact[name] = phone

    # Search Contact   
    elif choice == 2:
        search_name = input("Enter the contact name ").capitalize()
        if search_name in contact:
            print(f"""{Fore.GREEN}{search_name}'s contact number is { contact[search_name]}{Fore.RESET}""")

        else:
            print("Name is not found in contact book")   
    
    # Display Contact
    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            contactDetails()
          

    # Edit Contact
    elif choice == 4:
        edit_contact = input("Enter the contact name to be edited ")
        if edit_contact in contact:
            phone = input("enter mobile number ")
            contact[edit_contact] = phone
            print("Contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")   
            
    # Delete Contact
    elif choice == 5:
        del_contact = input("Enter the contact you want to delete ").capitalize()
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n ").lower()
            if confirm == 'y':
                contact.pop(del_contact)
                contactDetails()
            else:
                continue
        else:
                print("Name is not found in contact book")    

    # Exit
    elif choice == 6:
         break
    else: 
        print("Please select options options from 1-6")










