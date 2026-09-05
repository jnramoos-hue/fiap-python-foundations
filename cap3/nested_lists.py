inventory=[]
answer = "Y"
while answer == "Y":
  equipment=[input("Equipment: "),
            float(input("Value: ")),
            int(input("Serial Number: ")),
            input("Department: ")]
  inventory.append(equipment)
  answer = input("Enter \"Y\" to continue: ").upper()

for element in inventory:
  print("Name.........: ", element[0])
  print("Value........: ", element[1])
  print("Serial.......: ", element[2])
  print("Department...: ", element[3])

search=input("Enter the name of the equipment you want to search for: ")
for element in inventory:
  if search == element[0]:
    print("Value..: ", element[1])
    print("Serial.:", element[2])

depreciation=input("Enter the name of the equipment to be depreciated: ")
for element in inventory:
  if depreciation == element[0]:
    print("Value..: ", element[1])
    print("Serial.:", element[2])
    element[1] = element[1] * 0.9
    print("New value: ", element[1])

serial=int(input("Enter the serial number of the equipment to be deleted: "))
for element in inventory:
  if element[2] == serial:
    inventory.remove(element)

for element in inventory:
  print("Name.........: ", element[0])
  print("Value........: ", element[1])
  print("Serial.......: ", element[2])
  print("Department...: ", element[3])