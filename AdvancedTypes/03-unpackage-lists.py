numbers = [1, 2, 3]

# Ugly
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# Right way
first, second, third = numbers

numbers = [1, 2, 3, 6, 5, 8, 9, 7, 6, 3]

first, *others, last = numbers

print(first, last, others)
