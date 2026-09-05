def fill_inventory(inventory):
    answer = "Y"

    while answer == "Y":
        equipment = [
            input("Equipment: "),
            float(input("Value: ")),
            int(input("Serial Number: ")),
            input("Department: ")
        ]

        inventory.append(equipment)
        answer = input('Enter "Y" to continue: ').upper()


def display_inventory(inventory):
    for element in inventory:
        print("Name.........: ", element[0])
        print("Value........: ", element[1])
        print("Serial.......: ", element[2])
        print("Department...: ", element[3])


def find_by_name(inventory):
    search = input("\nEnter the name of the equipment you want to search for: ")

    for element in inventory:
        if search == element:
            print("Value..: ", element[1])
            print("Serial.: ", element[2])


def depreciate_by_name(inventory, percentage):
    depreciation = input(
        "\nEnter the name of the equipment to be depreciated: "
    )

    for element in inventory:
        if depreciation == element:
            print("Previous value: ", element[1])
            element[1] = element[1] * (1 - percentage / 100)
            print("New value.....: ", element[1])


def delete_by_serial(inventory):
    serial_number = int(input("\nEnter the serial number of the equipment to be deleted: "))

    for element in inventory:
        if element[2] == serial_number:
            inventory.remove(element)
    return "Items deleted."


def summarize_values(inventory):
    values = []

    for element in inventory:
        values.append(element[1])

    if len(values) > 0:
        print("The most expensive equipment costs: ", max(values))
        print("The least expensive equipment costs: ", min(values))
        print("The total value of the equipment is: ", sum(values))