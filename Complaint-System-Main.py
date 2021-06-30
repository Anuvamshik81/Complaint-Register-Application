from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import tkinter.messagebox as tkMessageBox
import time

from complaintListing import ComplaintListing
from configdb import ConnectionDatabase

from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Tkinter Login Form - Server Host')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()
print("Account Logged in Sucessfully")

# Config
conn = ConnectionDatabase()
root = Tk()
root.geometry('550x350')
root.title('Complaint Tracker')
root.configure(bg='blue')

# Style


style = Style()
style.theme_use('classic')
for styles in ['TLabel', 'TButton', 'TRadioButton']:
    style.configure(styles, bg='blue')

labels = ['First Name:', 'Last Name:', 'Address:', 'Gender:', 'Comment:']
for i in range(4):
    Label(root, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

ButtonList = Button(root, text='View Complain')
ButtonList.grid(row=5, column=1)

ButtonSubmit = Button(root, text='Submit Now')
ButtonSubmit.grid(row=5, column=2)

# Entries
firstname = Entry(root, width=40, font=('Arial', 14))
firstname.grid(row=0, column=1, columnspan=2)

lastname = Entry(root, width=40, font=('Arial', 14))
lastname.grid(row=1, column=1, columnspan=2)

address = Entry(root, width=40, font=('Arial', 14))
address.grid(row=2, column=1, columnspan=2)

GenderGroup = StringVar()
Radiobutton(root, text='Male', value='male', variable=GenderGroup).grid(row=3, column=1)
Radiobutton(root, text='Female', value='female', variable=GenderGroup).grid(row=3, column=2)

comment = Text(root, width=40, height=5, font=('Arial', 14))
comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)



def SaveData():
    message = conn.Add(firstname.get(), lastname.get(), address.get(), GenderGroup.get(), comment.get(1.0, 'end'))


firstname.delete(0, 'end')
lastname.delete(0, 'end')
address.delete(0, 'end')
comment.delete(1.0, 'end')

#showinfo(title='Add Information', message='Status')


def ShowComplainList():


 listrequest = ComplaintListing()

ButtonSubmit.config(command=SaveData)
ButtonList.config(command=ShowComplainList)

root.mainloop()
print("All complaints are registered succesfully")
showinfo(title='Status of the complaint', message='In the process of authencity')
for i in range(1, 16):
    time.sleep(1)
    print(str(i) + " Complaint will be resloved in " + str(i) + " days")
showinfo(title='Complaint approval', message='All complaints are resolved')