import socket
import select
import errno     # match error codes
import sys
import threading
import time
# 1.tells serever username
# 2.infinite loop if client has message
# receive msg from server
def sendMsg (my_username,client_socket,HEADER_LENGTH,):
    while True:
        try:
            message = input(f"{my_username}>")

            if message:
                #send message
                msg=message
                message = message.encode("utf-8")
                message_header = f"{len(message) :<{HEADER_LENGTH}}".encode("utf-8")
                client_socket.send(message_header + message)

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error',str(e))
                sys.exit()
    

        except Exception as e:
            print('General error',str(e))
            sys.exit()
            #send messages #waits the user to enter message



def recvMsg(username_header,client_socket,HEADER_LENGTH,):
    while True:
        try:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("connection closed by the server")
                sys.exit()
            #get user name
            username_length= int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            #get message
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")

            
        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error',str(e))
                sys.exit()
    

        except Exception as e:
            print('General error',str(e))
            sys.exit()
            #send messages #waits the user to enter message
   

HEADER_LENGTH = 10
IP =socket.gethostname()

PORT=1234

my_username=input("Username: ") #get username
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(True) #receive won't be blocking #non blocking mode(false)

#send user name to server
username= my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

t1 = threading.Thread(target=sendMsg, args=(my_username,client_socket,HEADER_LENGTH))
t2 = threading.Thread(target= recvMsg,args=(username_header,client_socket,HEADER_LENGTH))
t1.start()

#try:
t2.start()

t1.join()
t2.join()  

# except IOError as e:
#     if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#         print('Reading error',str(e))
#         print("bla")
#         sys.exit()
    

# except Exception as e:
#     print('General error',str(e))
#     print("I'm here")
#     sys.exit()
#     #send messages #waits the user to enter message

