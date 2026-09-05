name = input("Enter the patient's name: ")
age = int(input("Enter the patient's age: "))
infectious_disease = input("Is there a suspected infectious disease? ").upper()

if age >= 65:
    print("The patient " + name + " has priority care")
elif infectious_disease == "YES":
    print("The patient " + name + " must be directed to a separate waiting room.")
else:
    print("The patient " + name + " does not have priority care and may wait in the general waiting room!")