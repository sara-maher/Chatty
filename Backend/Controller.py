from Backend.Model import *
chatroom_name = ""
port_no = 1000

#signup
def add(username, password):
    result = DB_add(username, password)
    return result   # true if success, false if failed

#login
def check(username, password):
    check, result = DB_check(username, password)
    print(username)
    if (check and result == username):
        print("YAY!")
        return True
    return False

def add_chatroom(name): #create new server and send it's port no to database
    result = DB_add_chatroom(name)  #port no should be id+2000
    return result #true if success, false if failed

def delete_chatroom(): #create new server and send it's port no to database
    result = DB_delete_chatroom(chatroom_name)
    return result
def choose_chatroom(name): #get the port no from the GUI and run the server with that port no.
    chatroom_name, port_no = DB_choose_chatroom(mail,password)
    return result

def request_list_of_chatrooms(): #get list from database and send it to the GUI
    result = DB_show_chatrooms()
    return result


