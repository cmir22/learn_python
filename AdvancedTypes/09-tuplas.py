# Tuples are inmutables
numbers = (1, 2, 3, 4, 3, 2, 2) + (1, 5, 6, 43, 4)

print(numbers)

point = [1, 2]

# But we can create a new list using the tuple
new_list_tuple = numbers[:2]  # this do not affect the real tuple

print(tuple(point))
kklkkkk
