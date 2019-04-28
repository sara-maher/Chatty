""" Script for Tkinter GUI chat client. """
from PIL import Image, ImageDraw, ImageTk, ImageFont
import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def receive():
    """ Handles receiving of messages. """
    while True:
        try:
            msg = sock.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break

def send(event=None):
    """ Handles sending of messages. """
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    sock.send(bytes(msg, "utf8"))
    if msg == "#quit":
        sock.close()
        top.quit()

def on_closing(event=None):
    """ This function is to be called when the window is closed. """
    my_msg.set("#quit")
    send()




top = tkinter.Tk()
top.title("Client")
top.geometry("800x600")
image = Image.open("logo.png")
background_image=ImageTk.PhotoImage(image)
background_label =tkinter.Label(top, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = background_image
messages_frame = tkinter.Frame(top)

my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=70, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack(fill=tkinter.X,padx=5)

messages_frame.pack(fill=tkinter.X,padx=5)

button_label = tkinter.Label(top, text="Enter Message:",bg="white")
button_label.pack()
entry_field = tkinter.Entry(top, textvariable=my_msg, foreground="Red")
entry_field.bind("<Return>", send)
entry_field.pack(fill=tkinter.X,padx=5)
send_button = tkinter.Button(top, text="Send", command=send,height="2", width="15", bg ="red",pady="5")
send_button.pack()

quit_button = tkinter.Button(top, text="Quit", command=on_closing,height="2", width="15", bg ="yellow")
quit_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)



HOST = "127.0.0.1"
PORT = 5000
BUFSIZ = 1024
ADDR = (HOST, PORT)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(ADDR)

name = "name"
sock.send(bytes(name, "utf8"))

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.