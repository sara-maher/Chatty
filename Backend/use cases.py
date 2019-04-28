
def getUsernameAndPassword(my_username, my_password):
    pass

def check_validity(my_username, my_password): #send to database
    pass

def signup_recv(mail,password):
    pass

def signup_send(mail,password):
    pass

def add_chatroom(): #create new server شnd send it's port no to database
    #get last port number from database
    port=port+1
    Server(port)
    #send new server port and IP to database
    pass

def choose_chatroom(PORT): #get the port no from the GUI and run the server with that port no.
    #get chatroom port number
    Client(port)
    pass

def request_listof_chatrooms(): #get list from database and send it to the GUI
    pass


