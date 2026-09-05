inventory = []
answer = "Y"

while answer == "Y":
    inventory.append(input("Equipment: "))
    inventory.append(float(input("Value: ")))
    inventory.append(int(input("Serial number: ")))
    inventory.append(input("Department: "))
    answer = input('Enter "Y" to continue: ').upper()

# for element in inventory:
#     print(element)