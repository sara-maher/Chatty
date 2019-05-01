from Backend.Model import *
chatroom_name = ""
port_no = 1000
user_name = ""

# signup
def add(username, password):
    result = DB_add(username, password)
    return result   # true if success, false if failed


# login
def check(username, password):
    global user_name
    check, result = DB_check(username, password)
    # print(username)
    # print(result
    if (result is None):
        return False
    user_name = result[0]
    if (check and result[0] == username):
        print("YAY!")
        return True
    return False


def add_chatroom(name):     # create new server and send it's port no to database
    global user_name
    result = DB_add_chatroom(name)  # port no should be id+2000
    print(name)
    DB_AddAdmin(user_name, name)
    return result   # true if success, false if failed


def delete_chatroom(name):  # create new server and send it's port no to database
    result = DB_delete_chatroom(name, user_name)
    return result


# view all chatrooms
def view_chatrooms():
    return DB_view_chatrooms()


# select a chatroom to enter
def choose_chatroom(name):  # get the name from the GUI and port no. from db
    global chatroom_name
    global port_no
    chatroom_name = name
    check, port_no = DB_choose_chatroom(name)
    port_no += 5000
    return check, port_no
