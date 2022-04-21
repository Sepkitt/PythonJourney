#The objective of this project is to create an Address book using python in which the user can add a new contact 
# #edit and delete existing contact and view all the contact.

from select import select
from tkinter import *

root = Tk()
root.geometry('400x400')
root.config(bg = 'SlateGray3')
root.resizable(0,0)
root.title('DataFlair = ContactBook')

contactList = [
    ['Parv Maheswari',  '0176738493'],
    ['David Sharma',  '2684430000'],
    ['Mandish Kabra',   '4338354432'],
    ['Prisha Modi','6834552341'],
    ['Rahul kaushik',   '1234852689'],
    ['Johena Shaa' , '2119876543'],
    ]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side - RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)