import socket

HOST = "127.0.0.1"
PORT = 43210
exit_option = ""

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    while exit_option != "X":
        message = input("Your message: ")
        client_socket.sendto(message.encode("utf-8"), (HOST, PORT))

        data, origin = client_socket.recvfrom(65535)
        print("Server response:", data.decode("utf-8"))
        print("Response origin:", origin)

        exit_option = input('Enter "X" to exit: ').upper()
