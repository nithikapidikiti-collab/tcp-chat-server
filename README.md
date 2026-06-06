# TCP Multi-Client Chat Server

A real-time terminal chat application built from scratch using raw Python sockets and threading. Multiple clients can connect simultaneously and broadcast messages to each other through a central server.

## How it works

A TCP server binds to port 9999 and listens for incoming connections. Each client that connects is handled in its own thread, allowing multiple users to chat simultaneously. When a client sends a message, the server broadcasts it to all other connected clients.

## How to run

**Start the server:**
