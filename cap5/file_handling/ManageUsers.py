from cap5.file_handling.Funcions import *

users = {}
option = ask()
while option == "I" or option == "S" or option == "D" or option == "L":
    if option == "I":
        insert(users)
    option = ask()