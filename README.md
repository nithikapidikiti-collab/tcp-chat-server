
# TCP Multi-Client Chat Server

A real-time terminal chat application built from scratch using raw Python sockets and threading. Multiple clients can connect simultaneously and broadcast messages to each other through a central server.

## How it works

A TCP server binds to port 9999 and listens for incoming connections. Each client that connects is handled in its own thread, allowing multiple users to chat simultaneously. When a client sends a message, the server broadcasts it to all other connected clients.

## How to run

**Start the server:**
```
python3 server.py
```

**Connect as a client (open a new terminal for each user):**
```
python3 client.py
```

Type your name when prompted, then start chatting!

## Demo

- Terminal 1: server running, logs each connection
- Terminal 2: client "nithika" connected
- Terminal 3: client "gagana" connected
- Messages sent by one client appear instantly on all others

## Concepts demonstrated

- TCP socket programming (bind, listen, accept, connect)
- Multi-threading to handle concurrent clients
- Network broadcasting
- Client-server architecture

## What I'd add next

- SSL/TLS encryption
- Username colours
- /kick and /whisper commands
- GUI with Tkinter
```

Save with `Cmd + S`, then push:

```
git add .
git commit -m "docs: add README"
git push origin main
```
