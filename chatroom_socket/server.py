# python script 
# October'22
# Himanshu Tripathi

# tested on ubuntu 22.04.01 LTS
# tested on local system 

# multi-threaded server (TCP Socket)
# used as chat room server 

import socket
import threading
import sys

# server credentials (IP and PORT of server machine)
IP = socket.gethostbyname(socket.gethostname())
PORT = 54321

# global variables 
BUFFER = 1024
FORMAT = "utf-8"
# list to store client socket 
client_list = []
# list to store client username 
name_list = []

# create socket for server and bind with server IP and PORT
try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((IP,PORT))
    # start listening for clients 
    sock.listen()
    print(f"Server is ready to listen clients at {IP}:{PORT}")
except Exception as e:
    print(f"Error in socket creation\n{str(e)}")
    sys.exit()

# function for broadcasting message to all connected clients 
def broadcast(msg):
    for client in client_list:
        client.send(msg.encode(FORMAT))

# thread for client handling 
def client_handle(conn):
    while True:
        try:
            # receive message from client 
            msg = conn.recv(BUFFER).decode(FORMAT)
            # broadcast message to all clients 
            broadcast(msg)
        except:
            # get the index value of client 
            index = client_list.index(conn)
            # remove client from client_list abd from name_list
            client_list.remove(conn)
            user_name = name_list[index]
            broadcast(f"{user_name} has left the chat")
            name_list.remove(user_name)
            # terminate the client handle
            break

# main script, run forever 
while True:
    try:
        # accept client connection 
        conn,addr = sock.accept()
        print(f"{addr} connected with server")
        # ask for user name 
        conn.send("uname".encode(FORMAT))
        uname = conn.recv(BUFFER).decode(FORMAT)
        # update lists 
        client_list.append(conn)
        name_list.append(uname)
        broadcast(f"{uname} joined the chat")
        # create and start thread for client 
        threading.Thread(target=client_handle,args=(conn,)).start()
        active_connection = threading.active_count()-1
    except Exception as e:
        print(f"Error in threading \n{str(e)}")
        break
    except KeyboardInterrupt:
        print("Server closed using keyboard interrupt")
        break
    