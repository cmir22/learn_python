users = [
    ["Chanchito", 4],
    ["Pepe", 5],
    ["Manolo", 9]
]


# Example using for
# new_names_list = []
# for user in users:
#     new_names_list.append(user[0])

# Using conditionals
# names = [user for user in users if user[1] >= 5]

# Using conditionals and fintering
# names = [user[0] for user in users if user[1] >= 5]

# Using map
# names = list(map(lambda user: user[0], users))

# Using Filter
lessUsers = list(filter(lambda user: user[1] >= 5, users))

print(lessUsers)
