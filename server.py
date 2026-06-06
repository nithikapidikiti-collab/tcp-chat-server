import socket, threading

clients = []

def handle(conn, addr):
    print(f"[+] {addr} connected")
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: break
            broadcast(msg, conn)
        except: break
    clients.remove(conn)
    conn.close()

def broadcast(msg, sender):
    for c in clients:
        if c != sender:
            try: c.send(msg)
            except: clients.remove(c)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen()
print("[*] Listening on :9999")
while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle, args=(conn, addr)).start()