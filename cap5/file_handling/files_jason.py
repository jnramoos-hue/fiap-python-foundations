import json

with open("bd.json", "r") as arq_json:
    dic = json.load(arq_json)
    for key, data in dic.items():
        print(key + " | " + str(data))