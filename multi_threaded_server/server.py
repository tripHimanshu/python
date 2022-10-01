# python script
# october'22
# Himanshu Tripathi

# tested on ubuntu 22.04.01 LTS

# multi-threaded server (TCP Socket)

import socket 
import sys
import threading

# server credentials 
IP = socket.gethostbyname(socket.gethostname())
PORT = 54321

# global variables 
BUFFER = 1024
FORMAT = "utf-8"

# function for creating socket for server (TCP Socket)
def server_socket():
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind((IP,PORT))
        sock.listen()
        print(f"server is ready to listen clients at {IP}:{PORT}")
        return sock
    except Exception as e:
        print(f"Error in server_socket >> {str(e)}")
        sys.exit()

# function for client handler (thread)
def client_handle(conn,addr):
    while True:
        try:
            msg = conn.recv(BUFFER).decode(FORMAT)
            if not msg:
                print("No message received")
                break
            print(f"[{addr[0]}:{addr[1]}] >> {msg}")
            conn.send("message received".encode(FORMAT))
        except Exception as e:
            print(f"Error in client_handle >> {addr}")
            print(str(e))
            break

# function to accept client connection and start thread for client 
def connect_client(server):
    while True:
        try:
            conn, addr = server.accept()
            print(f"[Connected] >> {addr[0]}:{addr[1]}")
            client_thread = threading.Thread(target=client_handle, args=(conn,addr))
            client_thread.start()
            print(f"[Active Clients] >> {threading.active_count()-1}")
        except Exception as e:
            print(f"Error in connect_client >> {str(e)}")
            break

if __name__ == "__main__":
    try:
        server = server_socket()
        connect_client(server)
    except Exception as e:
        print(f"Error in main function >> {str(e)}")
    except KeyboardInterrupt:
        print("server closed using keyboard interrupt")
        server.close()
    sys.exit()
    