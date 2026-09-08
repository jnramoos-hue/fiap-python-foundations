import socket

HOST = "127.0.0.1"
PORT = 43210

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)
    print("Waiting for a client...")

    connection, client_address = server_socket.accept()

    with connection:
        print("Connected to:", client_address)
        received_message = connection.recv(1024)
        print("Received:", received_message.decode("utf-8"))
        connection.sendall(b"Hello, client")
