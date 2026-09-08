dataBase = []

with open("iris.data", "r") as ex_bid_data:
    for register in ex_bid_data.readlines():
        dataBase.append(register.split(","))

print(dataBase)

print(float(dataBase[0] [0]))