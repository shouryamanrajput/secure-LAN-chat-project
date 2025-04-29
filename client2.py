# client2.py

import socket
import threading
from encryption import encrypt, decrypt

HOST = '127.0.0.1'  # Replace with your Server's IP Address
PORT = 55555
key = 123  # Same key as server

def receive_messages(client_socket):
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if encrypted_message:
                decrypted_message = decrypt(encrypted_message.decode('utf-8'), key)
                print(f"\nFriend: {decrypted_message}")
        except:
            print("Error receiving message.")
            client_socket.close()
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input("")
        encrypted_message = encrypt(message, key)
        client.send(encrypted_message.encode('utf-8'))

if __name__ == "__main__":
    main()