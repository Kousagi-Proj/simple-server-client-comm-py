import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("localhost", 55555))#machine did not allow use of port 12345

#setting name

name = input ("Please enter your display name: ")

client_socket.send(name.encode())

#name set, start chatting

print("Welcome " + name + "! You may start chatting. Type 'quit' to leave.")

while True:
    message = input(name + ": ")

    client_socket.send(message.encode())

    if message.lower() == "quit":
        print("You disconnected.")
        client_socket.close()
        break

    # Receive echoed message
    data = client_socket.recv(1024).decode()
    print("server:", data)
