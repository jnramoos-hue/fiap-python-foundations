users = {}
print(users)

users = {"chaves": ["Chaves from 8", "24/12/2017", "Reception_01"],
         "quico": ["Quico das Flores", "20/12/2017", "Xray_03"]
        }

print(users)

users["florinda"] = ["Mrs. Florinda das Flores", "24/12/2017", "Xray_01"]

print(users)

print("#########-------##########")
print(users.get("quico"))