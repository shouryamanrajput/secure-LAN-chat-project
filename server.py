# server.py

import socket
import threading
from encryption import decrypt, encrypt

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 55555
clients = []
key = 123  # Shared secret key

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if encrypted_message:
                print(f"Encrypted message received: {encrypted_message}")
                broadcast(encrypted_message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()