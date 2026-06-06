import socket, threading, sys

s = socket.socket()
s.connect(("127.0.0.1", 9999))
name = input("Name: ")

def receive():
    while True:
        try: print(s.recv(1024).decode())
        except: sys.exit()

threading.Thread(target=receive, daemon=True).start()
while True:
    msg = input()
    s.send(f"{name}: {msg}".encode())