import socket
import threading
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321

BUFFER = 1024
FORMAT = "utf-8"

username = input("Enter your username: ")

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((IP,PORT))
    print("Connected with server")
except Exception as e:
    print(f"Error in socket creation\n{str(e)}")
    sys.exit()

def recv_data():
    while True:
        try:
            msg = sock.recv(BUFFER).decode(FORMAT)
            if msg == "uname":
                sock.send(username.encode(FORMAT))
            else:
                print(msg)
        except Exception as e:
            print(f"Error in recv data\n{str(e)}")
            sock.close()
            break
    sys.exit()

def send_data():
    while True:
        try:
            msg = f"{username} >> {input('')}"
            sock.send(msg.encode(FORMAT))
        except Exception as e:
            print(f"Error in send message\n{str(e)}")
            sock.close()
            break
    sys.exit()

threading.Thread(target=send_data).start()
threading.Thread(target=recv_data).start()
    