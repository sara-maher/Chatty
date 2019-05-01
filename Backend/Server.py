import socket
import select #multiple connection run the same on different OS

HEADER_LENGTH = 10
IP = socket.gethostname() 
PORT=1234


#socket type: address family internet
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#SOL->socket option level

server_socket.bind((IP, PORT))
server_socket.listen()

#have list of clients(sockets)
sockets_list = [server_socket]
#Dictionary : client socket is the key and user data is the value
clients = {}

#receive messages
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header): # nothing is received CLIENT CLOSE THE CONNECTION
            return False

    #get message length and then receive the message & return dictionary of header and data    
        message_length = int(message_header.decode("utf-8").strip()) #strip() removes the spaces from the string
        return {"header":message_header, "data":client_socket.recv(message_length)} #we here receive the data however long it is 
    
    #client closed aggrisively
    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)        #read list(read in/get data from),write list,sockets error on

    for notified_socket in read_sockets:
        if notified_socket == server_socket: #accept connection
            client_socket, client_address = server_socket.accept() #accept? accept connection and return socket number and IP address
            
            #header and data
            user = receive_message(client_socket)
            if user is False: #disconnected
                continue

            #  clients list[socket,dictionary{header,data}] 
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(f"Accepted new connection from {client_address[0]} : {client_address[1]} username: {user['data'].decode('utf-8')}")
        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")   
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print(f"Received message from {user ['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")
            
            #share message with everyone
            for client_socket in clients: 
                if client_socket != notified_socket:  #NOT to send myself      #username and data
                    client_socket.send(user['header'] + user['data'] + message['header'] + message ['data'])

    #exception raised
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]