import socket

name_prompt = "please enter a name"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 55555))#machine did not allow use of port 12345
server_socket.listen(1)

print("TCP server is listening...")

conn, addr = server_socket.accept()

print(f"Connected by {addr}")

#setting name

name = conn.recv(1024).decode()

print ("Client " + name + " has entered the chatroom.")

#messaging starts here
while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    if data.lower() == "quit":
        print(name + " has disconnected.")
        conn.send("Goodbye!".encode())
        conn.close()
        break

    print("Recieved from " + name + ":", data)
    conn.send(data.encode())
