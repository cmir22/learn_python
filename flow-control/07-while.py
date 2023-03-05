# number = 1

# while number < 100:
#     print(number)
#     number *= 2
while True:
    command = input("$ ")
    print(command)
    if command.lower() == "exit":
        break
