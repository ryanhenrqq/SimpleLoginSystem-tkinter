import webbrowser
import win32ui
from PIL import ImageTk
from tkinter import *

# Open passwords .txt file, for validation
with open('.\\passwords.txt','r') as system_valid:
    password_1= system_valid.readlines()
    password_1= "".join(password_1)
    password_1= password_1.strip()
    password= password_1.split()


# all these 4 functions hide the other names when you click on it
def loginuser1():
    window.geometry('300x350')
    user1field.grid(column=1,row=4)
    user1key.grid(column=1,row=5)
    user1img.grid(column=1,row=3)
    user1btn.destroy()
    user2btn.destroy()
    user3btn.destroy()
    user4btn.destroy()


def loginuser2():
    window.geometry('300x350')
    user2field.grid(column=1,row=3)
    user2key.grid(column=1,row=4)
    user2img.grid(column=1,row=5)
    user1btn.destroy()
    user2btn.destroy()
    user3btn.destroy()
    user4btn.destroy()


def loginuser3():
    window.geometry('300x350')
    user3field.grid(column=1,row=4)
    user3key.grid(column=1,row=5)
    user3img.grid(column=1,row=3)
    user1btn.destroy()
    user2btn.destroy()
    user3btn.destroy()
    user4btn.destroy()


def loginuser4():
    window.geometry('300x350')
    user4field.grid(column=1,row=4)
    user4key.grid(column=1,row=5)
    user4img.grid(column=1,row=3)
    user1btn.destroy()
    user2btn.destroy()
    user3btn.destroy()
    user4btn.destroy()


# these 4 funcions can validade user input and the passwords inside our .txt file, and open an anchor for the next...
def verify1():
    input = user1field.get()
    if input==password[0]:
        correct1()
    else:
        win32ui.MessageBox('Senha errada!','Login')
        quit()


def verify2():
    input = user2field.get()
    if input==password[1]:
        correct2()
    else:
        win32ui.MessageBox('Senha errada!','Login')
        quit()


def verify3():
    input = user3field.get()
    if input==password[2]:
        correct3()
    else:
        win32ui.MessageBox('Senha errada!','Login')
        quit()


def verify4():
    input = user4field.get()
    if input==password[3]:
        correct4()
    else:
        win32ui.MessageBox('Senha errada!','Login')
        quit()


# these functions have the second window informations, and they show itself and the buttons for redirect
def correct1():
    name = 'User 1'
    window2.deiconify()
    window2.geometry('400x300')
    header2['font'] = ('System 20')
    header2['text'] = f'Bem Vindo, {name}'
    header2.grid(column=1,row=1)
    enter1.grid(column=1,row=2)
    logoffbtn.grid(column=1,row=5)
    window.destroy()


def correct2():
    name = 'User 2'
    window2.deiconify()
    window2.geometry('400x300')
    header2['font'] = ('System 20')
    header2['text'] = f'Bem Vindo, {name}'
    header2.grid(column=1,row=1)
    enter2.grid(column=1,row=2)
    logoffbtn.grid(column=1,row=4)
    window.destroy()


def correct3():
    name = 'User 3'
    window2.deiconify()
    window2.geometry('400x300')
    header2['font'] = ('System 20')
    header2['text'] = f'Bem Vindo, {name}'
    header2.grid(column=1,row=1)
    enter3.grid(column=1,row=2)
    logoffbtn.grid(column=1,row=4)
    window.destroy()


def correct4():
    name = 'User 4'
    window2.deiconify()
    window2.geometry('400x300')
    header2['font'] = ('System 20')
    header2['text'] = f'Bem Vindo, {name}'
    header2.grid(column=1,row=1)
    enter4.grid(column=1,row=2)
    logoffbtn.grid(column=1,row=3)
    window.destroy()


# these ones are the web link, for redirect
def redir1():
    webbrowser.open("https://www.google.com/")


def redir2():
    webbrowser.open("https://www.google.com/")


def redir3():
    webbrowser.open("https://www.google.com/")


def redir4():
    webbrowser.open("https://www.google.com/")


# as the window stay open for future call, this button close the window itself
def logoff():
    window2.destroy()
    quit()

# these are tkinter parameters (main window and window 2)

# this window is the login screen, where you choose the user and put it the password
window = Tk()
# and this is the welcome window, which contains the anchors button for website
window2 = Tk()

window.title('Sistema de Login em Redes')
window2.title('Sistema de Login em Redes')
window.geometry('300x300')
window2.geometry('0x0')
window.resizable(0,0)
window2.resizable(0,0)
window2.iconify

# images path setter and converter (PIL library)
user1imgf = ImageTk.PhotoImage(file='.\\user1_profile.png')
user2imgf = ImageTk.PhotoImage(file='.\\user2_profile.png')
user3imgf = ImageTk.PhotoImage(file='.\\user3_profile.png')
user4imgf = ImageTk.PhotoImage(file='.\\user4_profile.png')

# main window header and users
header = Label(window,text='Login Redes',font=('System 28'))
header.grid(column=1,row=1)

user1btn = Button(window,command=loginuser1,text='user1',font=('System 16'),width=38)
user1btn.grid(column=1,row=2)

user2btn = Button(window,command=loginuser2,text='user2',font=('System 16'),width=38)
user2btn.grid(column=1,row=3)

user3btn = Button(window,command=loginuser3,text='user3',font=('System 16'),width=38)
user3btn.grid(column=1,row=4)

user4btn = Button(window,command=loginuser4,text='user4',font=('System 16'),width=38)
user4btn.grid(column=1,row=5)

# main window validation
user1field = Entry(window,width=30,show='*')
user2field = Entry(window,width=30,show='*')
user3field = Entry(window,width=30,show='*')
user4field = Entry(window,width=30,show='*')
user1key = Button(window,command=verify1,text='Entrar',font=('System 16'),width=26)
user2key = Button(window,command=verify2,text='Entrar',font=('System 16'),width=26)
user3key = Button(window,command=verify3,text='Entrar',font=('System 16'),width=26)
user4key = Button(window,command=verify4,text='Entrar',font=('System 16'),width=26)

# main window images to show
user1img = Label(window, image=user1imgf)
user2img = Label(window, image=user2imgf)
user3img = Label(window, image=user3imgf)
user4img = Label(window, image=user4imgf)

# window 2 assets
header2 = Label(window2,text='testing',font=('System 28'))
enter1 = Button(window2,command=redir1,text='Link para o Google',font=('System 16'))
enter2 = Button(window2,command=redir2,text='Link para o Google',font=('System 16'))
enter3 = Button(window2,command=redir3,text='Link para o Google',font=('System 16'))
enter4 = Button(window2,command=redir4,text='Link para o Google',font=('System 16'))
logoffbtn = Button(window2,command=logoff,text='Fechar',font=('System 16'))

window.mainloop()
window2.mainloop()
