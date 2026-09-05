equipment = []
values = []
serial_numbers = []
departments = []
answer = 'Y'

while answer == 'Y':
    equipment.append(input("Equipment: "))
    values.append(float(input("Value: ")))
    serial_numbers.append(int(input("Serial number: ")))
    departments.append(input("Department: "))
    answer = input('Enter "Y" to continue: ').upper()

search = input('\nInsert the name of equipment you wish to search for: ')
for index in range (0, len(equipment)):
    if search == equipment[index]:
        print("Value..: ", values[index])
        print("Serial.: ", serial_numbers[index])