#The objective of this project is to create an Address book using python in which the user can add a new contact 
#edit and delete existing contact and view all the contact.

# with open('contact.txt', 'a') as f:
#     name = input('Name: ')
#     phone = input('Phone: ')
#     f.writelines(f'Name: {name} \nPhone: {phone} \n\n')

contact = {}
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

options =  "1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete contact \n 6. Exit"
while True:
    # user prompt
    choice = int(input(options))

    # Add Contact
    if choice == 1:
        name = input("Enter the contact name ")
        phone = input("Enter the mobile number ")
        contact[name] = phone

    # Search Contact   
    elif choice == 2:
        search_name = input("Enter the contact name ")
        if search_name in contact:
            print(search_name,"'s contact number is ", contact[search_name])

        else:
            print("Name is not found in contact book")   
    
    # Display Contact
    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()

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
        del_contact = input("Enter the contact you want to delete")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n ").lower()
            if confirm == 'y':
                contact.pop(del_contact)
                display_contact()
            else:
                print("Name is not found in contact book")     

    # Exit
    elif choice == 6:
         break
    else: 
        print("Please select options options from 1-6")










