# python script
# October'22
# Himanshu Tripathi

# tested on ubuntu 22.04.01 LTS
# tested on local system 

# client for echo server app

import socket 
import sys

# server credentials 
IP = socket.gethostbyname(socket.gethostname())
PORT = 54321

# global variables 
BUFFER = 1024
FORMAT = "utf-8"

# create socket for client (TCP socket)
try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((IP,PORT))
    print("connection established with server")
except Exception as e:
    print(f"Error in socket creation >> {str(e)}")
    sys.exit()

# start communication with server 
while True:
    try:
        sock.send(input(">> ").encode(FORMAT))
        msg = sock.recv(BUFFER).decode(FORMAT)
        if not msg:
            print("No message received")
            break
        print(msg)
    except Exception as e:
        print(f"Error in client communication >> {str(e)}")
        break
    except KeyboardInterrupt:
        print("client closed using keyboard interrupt")
        break
sock.close()
sys.exit()
