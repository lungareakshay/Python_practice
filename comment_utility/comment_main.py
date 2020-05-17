# Comment Utility

from tkinter import *
from tkinter import messagebox  

##########################################################################################
def headerClicked():
    '''
    get header comment format
    '''
    programmer_name = programmer.get()
    workitem_number = workitem.get()
    print(programmer_name +' '+workitem_number)

def singleClicked():
    '''
    get single line comment format
    '''
    print('test2')

def blockClicked():
    '''
    get block comment format
    '''
    print('test3')

def acceptchar():
    '''
    set comment char
    '''
    user_input = Toplevel()
    user_input.title('Enter comment character:')
    user_input.geometry('300x30')
    user_input.mainloop()

def displayinfo():
    '''
    display information for utility
    '''
    messagebox.showinfo(title='Information', message='This utility has been developed by AkshayL.\n For more info ')
##########################################################################################


window = Tk()

# set title
window.title('Comment Utility')
window.geometry('250x160')

# create menu to set the comment character
menu = Menu(window)
menu.add_command(label='Settings',command =acceptchar)
menu.add_command(label='Info',command =displayinfo)
window.config(menu=menu)

# input for 'Programmer Name' and 'Work Item Number'
lbl = Label(window, text="Pragrammer:", font = ("Arial Bold",10))
lbl.grid(column=0, row=0, sticky='w')

programmer = Entry(window,width=10)
programmer.grid(column=0, row=1, sticky ='we')

lbl2 = Label(window, text="Work Item:", font = ("Arial Bold",10))
lbl2.grid(column=0, row=2, sticky ='w')

workitem = Entry(window,width=10)
workitem.grid(column=0, row=3, sticky ='we')
# default focus on work item number
workitem.focus()

# Button to generate comment
btn_header = Button(window, text="Header",command=headerClicked)
btn_header.grid(column=0, row=4,sticky ='we')
window.grid_columnconfigure(0, weight=1)

btn_header = Button(window, text="Single Line",command=singleClicked)
btn_header.grid(column=0, row=5, sticky ='we')

btn_header = Button(window, text="Block",command=blockClicked)
btn_header.grid(column=0, row=6, sticky ='we')

# wait for user
window.mainloop()

