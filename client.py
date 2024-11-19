import socket
import threading

# Client Configuration
HOST = '127.0.0.1'  # Server's IP
PORT = 12345        # Server's Port

def receive_messages(client):
    while True:
        try:
            # Receive and print messages
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def send_messages(client):
    while True:
        # Send user input to the server
        message = f"{nickname}: {input('')}"
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    nickname = input("Enter your nickname: ")

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()
