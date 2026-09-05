equipment = []
values = []
serial_numbers = []
departments = []
answer = "Y"

while answer == "Y":
    equipment.append(input("Equipment: "))
    values.append(float(input("Value: ")))
    serial_numbers.append(int(input("Serial number: ")))
    departments.append(input("Department: "))
    answer = input('Enter "Y" to continue: ').upper()

for index in range(0, len(equipment)):
    print("\nEquipment..: ", index + 1)
    print("Name.........: ", equipment[index])
    print("Value........: ", values[index])
    print("Serial number: ", serial_numbers[index])
    print("Department...: ", departments[index])