import socket
import select
import errno     # match error codes
import sys
# 1.tells serever username
# 2.infinite loop if client has message
# receive msg from server
def Client(PORT):
    HEADER_LENGTH = 10
    IP =socket.gethostname()

    #PORT=1234

    my_username=input("Username: ") #get username
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    client_socket.setblocking(False) #receive won't be blocking

    #send user name to server
    username= my_username.encode("utf-8")
    username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
    client_socket.send(username_header + username)

    while True:
        message = input(f"{my_username}>")

        if message:
            #send message
            message = message.encode("utf-8")
            message_header = f"{len(message) :<{HEADER_LENGTH}}".encode("utf-8")
            client_socket.send(message_header + message)
        try:
            while True:
                #receive things
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
            continue

        except Exception as e:
            print('General error',str(e))
            sys.exit()
            #send messages #waits the user to enter message

