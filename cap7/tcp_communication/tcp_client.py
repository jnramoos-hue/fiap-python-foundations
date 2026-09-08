import socket

HOST = "127.0.0.1"
PORT = 43210

message = input("Enter a message: ").encode("utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(message)
    response = client_socket.recv(1024)
    print("Received:", response.decode("utf-8"))
