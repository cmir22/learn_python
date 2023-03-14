point = {"x": 25,
         "y": 50
         }

print(point)
print(point["x"])
print(point["y"])

#  We can add more keys
point["z"] = 45

print(point)

# Access to no existed
if "lala" in point:
    print('Lala is here', point["lala"])

print(point.get("x"))
#  97 is a default value when not exist
print(point.get("simona", 97))
del point["x"]
del (point["y"])
