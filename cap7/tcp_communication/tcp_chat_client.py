import socket

HOST = "127.0.0.1"
PORT = 43210

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    while True:
        message = input("Your message: ")
        client_socket.sendall(message.encode("utf-8"))

        response = client_socket.recv(1024).decode("utf-8")
        print("Server response:", response)

        if message.upper() == "END" or response.upper() == "END":
            break
