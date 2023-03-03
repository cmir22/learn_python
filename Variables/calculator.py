n1 = input("Type first number")
n2 = input("Type second number")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
rest = n1 - n2
mult = n1 * n2
div = n1 / n2

msg = f"""
For this numbers {n1} and {n2},
result is {suma}
result is {rest}
result is {mult}
result is {div}
"""

print(msg)
