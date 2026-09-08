import socket

HOST = "127.0.0.1"
PORT = 43210

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print("UDP server is ready...")

    while True:
        data, origin = server_socket.recvfrom(65535)
        message = data.decode("utf-8")
        print("Origin........: ", origin)
        print("Received data.: ", message)

        response = input("Enter the response: ")
        server_socket.sendto(response.encode("utf-8"), origin)

        if message.upper() == "END" or response.upper() == "END":
            break
