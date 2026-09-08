import getpass

username = input("Enter the username: ")
password = getpass.getpass("Enter the password: ")

if username == "admin" and password == "1234":
    print("Access granted.")
else:
    print("Access denied.")
