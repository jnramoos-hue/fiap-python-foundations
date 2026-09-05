multiplication_table = int(input("Enter a number to display its multiplication table: "))
print("Multiplication table for", multiplication_table)

for value in range(1, 11, 1):
    print(str(multiplication_table) + " x " + str(value) + " = " + str(multiplication_table * value))