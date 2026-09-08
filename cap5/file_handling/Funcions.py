def ask():
    return input("What do you want to do?\n" +
              "<I> - To insert a user.\n" +
              "<S> - To search for a user.\n" +
              "<D> - To delete a user.\n" +
              "<L> - To list a user: ").upper()

def insert(dictionary):
    dictionary[input("Enter the login: ").upper()] = [input("Enter your name: ").upper(),
                                                   input("Enter the last access date: "),
                                                   input("Enter the last workstation accessed: ").upper()]

    save(dictionary)

def save(dictionary):
    with open("bs.txt", "a") as file:
        for key, value in dictionary.items():
            file.write(key + ":" + str(value))