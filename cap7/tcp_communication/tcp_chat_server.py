import socket

HOST = "127.0.0.1"
PORT = 43210

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("Waiting for a chat client...")

    connection, client_address = server_socket.accept()

    with connection:
        print("Connected to:", client_address)

        while True:
            received_data = connection.recv(1024)

            if not received_data:
                break

            received_message = received_data.decode("utf-8")
            print("Client:", received_message)

            response = input("Your response: ")
            connection.sendall(response.encode("utf-8"))

            if received_message.upper() == "END" or response.upper() == "END":
                break
