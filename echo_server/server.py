# python script 
# October'22
# Himanshu Tripathi

# tested on ubuntu 22.04.01 LTS

# echo server (TCP socket)

import socket 
import sys

# server credentials 
IP = socket.gethostbyname(socket.gethostname())
PORT = 54321

# global variables 
BUFFER = 1024
FORMAT = "utf-8"

# create socket for server (TCP socket)
try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((IP,PORT))
    sock.listen()
    print(f"Server is ready to listen clients at {IP}:{PORT}")
except Exception as e:
    print(f"Error in socket creation >> {str(e)}")
    sys.exit()

# communicate with client 
while True:
    try:
        conn,addr = sock.accept()
        print(f"Client connected from {addr[0]}:{addr[1]}")
        while True:
            try:
                msg = conn.recv(BUFFER).decode(FORMAT)
                if not msg:
                    print("No message received\nclient connection is closed")
                    conn.close()
                    break
                print(f"[{addr}] >> {msg}")
                # send acknowledgement message 
                conn.send("message received".encode(FORMAT))
            except Exception as e:
                print(f"Error in client connection >> {str(e)}")
                break
            except KeyboardInterrupt:
                print("Client connection closed using keyboard interrupt")
                if conn:
                    conn.close()
                break
    except Exception as e:
        print(f"Error in communicate function >> {str(e)}")
        break
    except KeyboardInterrupt:
        print("Server closed using keyboard interrupt")
        break
sock.close()
sys.exit()