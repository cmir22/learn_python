# Group or conjunt
first = {1, 2, 1, 1, 2, 4}
second = [3, 5, 8, 9, 6, 4, 7, 1, 1, 1, 1, 2, 2, 3, 3]

# Methods to use
first.add(2)
first.remove(4)

# Convert into a set
second = set(second)

print(second)
print(first)

#  We can join sets
print(first | second)
# Intersection operator
print(first & second)
# Diference operator
print(first - second)
# Diference simetric operator
print(first ^ second)
