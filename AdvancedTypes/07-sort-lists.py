numbers = [5, 8, 9, 7, 5, 6, 2, 1, 17, 78, 5, 1, 32, 4, 8, 4]

# default sort
numbers.sort()
# reverse sort
numbers.sort(reverse=True)
# Sorted return a new list without remove the previus list
new_sorted = sorted(numbers, reverse=True)

print(numbers, new_sorted)

users = [["Chanchito", 4], ["Pepe", 5], ["Manolo", 9]]

# ----------------------------------------------
# Example without lambda:

# def ordenate(element):
#     return element[1]
# users.sort(key=ordenate, reverse=True)
# ----------------------------------------------


# ----------------------------------------------
# Example with lambda:

users.sort(key=lambda el: el[1], reverse=False)
# ----------------------------------------------

print(users)
