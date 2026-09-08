import socket

services = ["domain", "http", "ftp"]

for service in services:
    try:
        print(service.upper(), "port:", socket.getservbyname(service))
    except OSError:
        print(service.upper(), "service was not found on this system.")
