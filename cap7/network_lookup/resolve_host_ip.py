import socket

answer = "Y"

while answer == "Y":
    host = input("Enter a hostname, for example example.com: ")

    try:
        ip_address = socket.gethostbyname(host)
        print("The IP address for the hostname is: ", ip_address)
    except socket.gaierror:
        print("The hostname could not be resolved.")

    answer = input('Enter "Y" to continue: ').upper()
