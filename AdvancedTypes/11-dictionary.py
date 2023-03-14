point = {"x": 25, "y": 50}


point["z"] = 45


if "lala" in point:
    print("I found lala", point["lala"])


print(point.get("x"))
print(point.get("lala", 97))

del point["x"]

print(point)


for valor in point.items():
    print(valor)


users = [
    {"id": 1, "name": "chanchito"},
    {"id": 2, "name": "pancho"},
    {"id": 3, "name": "manolo"}
]

for user in users:
    print(user.get("name"))
