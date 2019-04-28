import tkinter
from tkinter import *
import time
import os
from functools import partial
from Backend.Controller import *
# import client
from PIL import Image, ImageDraw, ImageTk, ImageFont
register_screen = main_screen = username = password = username_entry = None
login_screen = username_verify = password_verify = username_login_entry = None
login_success_screen = password_not_recog_screen = user_not_found_screen = None
password_entry = password_login_entry = None


# signup form
def sign_up():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Sign Up")
    register_screen.geometry("800x600")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    image = Image.open("logo.png")
    background_image = ImageTk.PhotoImage(image)
    background_label = Label(register_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    Label(register_screen, text="Please enter details below to join us", width="300", height="2", bg="white", font=("Helvetica", 20, "bold")).pack()
    Label(text="", bg="white").pack()
    Label(register_screen, text="", bg="white").pack()
    username_lable = Label(register_screen, text="Username ", bg="white")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ", bg="white")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="", bg="white").pack()
    Button(register_screen, text="Sign Up", width=15, height=2, bg="yellow", command=register_user).pack()


# login form
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("800x600")
    image = Image.open("logo.png")
    background_image = ImageTk.PhotoImage(image)
    background_label = Label(login_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    Label(login_screen, text="Please enter details below to login", width="300", height="2", bg="white", font=("Helvetica", 20, "bold")).pack()
    Label(login_screen, text="", bg="white").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ", bg="white").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg="white").pack()
    Label(login_screen, text="Password * ", bg="white").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="", bg="white").pack()
    Button(login_screen, text="Login", bg="yellow", width=15, height=2, command=login_verify).pack()


# Implementing event on register button
def register_user():

    username_info = username.get()
    password_info = password.get()
    # Write The code to save User data in DB
    """
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    """
    result = add(username_info, password_info)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    if (result):
        Label(register_screen, text="Registration Success", fg="green", font=("Helvetica", 11), bg="white").pack()
    else:
        Label(register_screen, text="Registration Failed", fg="red", font=("Helvetica", 11), bg="white").pack()


# Implementing event on login button
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    result = check(username1, password1)
    if (result):
        login_sucess(username1)
    else:  # to do add, check for password and username to know which of them is wrong
        user_not_found()
    """
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess(username1)

        else:
            password_not_recognised()

    else:
        user_not_found()
    """


# Designing popup for login success
def login_sucess(user_name):
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    image = Image.open("logo.png")
    background_image = ImageTk.PhotoImage(image)
    background_label = Label(login_success_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image
    login_success_screen.geometry("800x600")
    # -------Open chat room page----------
    Label(login_success_screen, text="Choose the chat room", width="300", height="2", bg="white", font=("Helvetica", 20, "bold")).pack()
    check, chatrooms = view_chatrooms()
    if (check):
        i = 0
        for chatroom in chatrooms:
            print(chatroom)
            Button(login_success_screen, text=chatroom, height="2", width="15", command=partial(enter_chat, chatroom[0]), bg="Red", fg="white").place(x=100+i, y=500)
            i = i+150
        # Button(login_success_screen, text="Chat Room 2", height="2", width="15", command=enter_chat, bg="green", fg="yellow").place(x=350, y=500)
        Button(login_success_screen, text="Add Chat Room", height="2", width="15", command=add_chat, bg="orange", fg="blue").place(x=600, y=500)
    else:
        Label(login_success_screen, text="Error Viewing Chatrooms", fg="red", font=("Helvetica", 11), bg="white").pack()


def enter_chat(x):
    # print(x)
    check, port = choose_chatroom(str(x))
    print(check)
    print(port)
    if (check):
        string = 'python Chatroom/client_view.py ' + str(port)
        # time.sleep(1)
        os.system(string)
    else:
        Label(login_success_screen, text="Error Entering Chatroom", fg="red", font=("Helvetica", 11), bg="white").pack()
    return


def add_chat():
    return
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    image = Image.open("logo.png")
    background_image = ImageTk.PhotoImage(image)
    background_label = Label(password_not_recog_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image
    password_not_recog_screen.geometry("800x600")
    Label(password_not_recog_screen, text="Invalid Password ", bg="white").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    image = Image.open("logo.png")
    background_image = ImageTk.PhotoImage(image)
    background_label = Label(user_not_found_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image
    user_not_found_screen.geometry("800x600")
    Label(user_not_found_screen, text="User Not Found", bg="white").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups
def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def delete_login_screen():
    login_screen.destroy()


def opening(main_screen2):
    global main_screen
    main_screen = main_screen2
    main_screen.geometry("800x600")
    main_screen.title("Chatty App")
    image = Image.open("logo.png")
    background_image = ImageTk.PhotoImage(image)
    background_label = Label(main_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image
    Button(text="Login", height="2", width="15", command=login, bg="green").place(x=100, y=500)
    Label(text="", bg="white").pack()
    Button(text="Sign Up", height="2", width="15", command=sign_up, bg="yellow").place(x=580, y=500) 
