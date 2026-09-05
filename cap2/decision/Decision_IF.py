name = input("Enter the name: ")
age = int(input("Enter the age: "))

if age >= 65:
    print("The patient " + name + " HAS priority care")
else:
    print("The patient " + name + " DOES NOT HAVE priority care")