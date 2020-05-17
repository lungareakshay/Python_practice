# Comment Utility

from tkinter import *
from tkinter import messagebox  
from datetime import date
import winreg
import clipboard

##########################################################################################


REG_PATH = r"HKEY_CURRENT_USER\Software\Akshay Lungare Inc.\CommentUtility"

def initialize():
    #Example MouseSensitivity
    #Read value 
    ls_prog = get_reg('ProgrammerName')
    ls_workitem = get_reg('WorkItem')
    ls_desc = get_reg('Description')

    programmer.insert(0,ls_prog)
    workitem.insert(0,ls_workitem)
    description.insert(0,ls_desc)

def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        print(WindowsError)
        return False

def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        print(WindowsError)
        return None

def setClipboard(ls_comment):
    '''
    set clipboard text and set the variable in registry
    '''
    programmer_name = programmer.get()
    workitem_number = workitem.get()
    description_text = description.get()

    set_reg('ProgrammerName', programmer_name)
    set_reg('WorkItem', workitem_number)
    set_reg('Description', description_text)

    clipboard.copy(ls_comment)
    #minimize window
    window.iconify()

def getInput(fun):
    def inner(*args, **kwargs):
        ld_date = date.today()
        workitem_number = workitem.get()
        programmer_name = programmer.get()
        description_text = description.get()
        return fun(ld_date,workitem_number,programmer_name,description_text)
    return inner
    
@getInput
def headerClicked(ld_date,workitem_number,programmer_name,description_text):
    '''
    get header comment format
    '''
    ls_header = "####################################################################"
    ls_header += "\n#Function\\Module:"
    ls_header += "\n#                "
    ls_header += "\n#Return Arg:"
    ls_header += "\n#           "
    ls_header += "\n#Description:"
    ls_header += "\n#           "
    ls_header += "\n# Date         Work Item        Programmer      Description"
    ls_header += "\n# "+ str(ld_date) +"   WI#"+ workitem_number +"          "+ programmer_name +"        "+description_text
    ls_header += "\n####################################################################"
    
    setClipboard(ls_header)

@getInput
def singleClicked(ld_date,workitem_number,programmer_name,description_text):
    '''
    get single line comment format
    '''
    ls_single_line = "# Date:"+ str(ld_date) +"   Work Item: WI#"+ workitem_number +"       Programmer: "+ programmer_name +"    Description: "+ description_text
    setClipboard(ls_single_line)

@getInput
def blockClicked(ld_date,workitem_number,programmer_name,description_text):
    '''
    get block comment format
    '''
    ls_block_comment = "# START Date: "+ str(ld_date) +"   Work Item: WI#"+ workitem_number +"       Programmer: "+ programmer_name +"   Description:"+description_text
    ls_block_comment += "\n# END Date: "+ str(ld_date) +"   Work Item: WI#"+ workitem_number +"       Programmer: "+ programmer_name 
    setClipboard(ls_block_comment)

def displayinfo():
    '''
    display information for utility
    '''
    messagebox.showinfo(title='Information', message='This utility has been developed by AkshayL.\nFor more info: https://github.com/lungareakshay/Python_practice/tree/master/comment_utility')
##########################################################################################

window = Tk()

# set title
window.title('Comment Utility')
window.geometry('250x230')
window.iconbitmap('./hash.ico')
window.maxsize(250,230) 

# create menu to set the comment character
menu = Menu(window)
menu.add_command(label='Info',command =displayinfo)
window.config(menu=menu)

##########################################################################################

# input for 'Programmer Name' and 'Work Item Number'
lbl = Label(window, text="Pragrammer:", font = ("Arial Bold",10), fg='blue')
lbl.grid(column=0, row=0, sticky='w')

programmer = Entry(window,width=10)
programmer.grid(column=0, row=1, sticky ='we')

lbl2 = Label(window, text="Work Item:", font = ("Arial Bold",10), fg='blue')
lbl2.grid(column=0, row=2, sticky ='w')

workitem = Entry(window,width=10)
workitem.grid(column=0, row=3, sticky ='we')
# default focus on work item number
workitem.focus()

lbl3 = Label(window, text="Description:", font = ("Arial Bold",10), fg='blue')
lbl3.grid(column=0, row=4, sticky ='w')

description = Entry(window,width=10)
description.grid(column=0, row=5, sticky ='we')

##########################################################################################

# Button to generate comment
btn_header = Button(window, text="Header",command=headerClicked, font = ("Arial Bold",10))
btn_header.grid(column=0, row=6,sticky ='we')

btn_header = Button(window, text="Single Line",command=singleClicked, font = ("Arial Bold",10))
btn_header.grid(column=0, row=7, sticky ='we')

btn_header = Button(window, text="Block",command=blockClicked, font = ("Arial Bold",10))
btn_header.grid(column=0, row=8, sticky ='we')

##########################################################################################
window.grid_columnconfigure(0, weight=1)

initialize()

# wait for user
window.mainloop()

