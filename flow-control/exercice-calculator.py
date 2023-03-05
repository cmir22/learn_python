# User numbers
firstNumber = 0
secondNumber = 0

# Save the restult
result = 0

# Command typed
command = ""

while True:
    command = input("Ingrese la operacion ")
    print(command)
    if (command == "suma"):
        firstNumber = int(input("Ingrese el primer numero "))
        secondNumber = int(input("Ingrese el segundo numero "))
        result = firstNumber + secondNumber
        print(result)
    elif (command.lower() == "multi"):
        firstNumber = int(input("Ingrese el primer numero "))
        secondNumber = int(input("Ingrese el segundo numero "))
        result = firstNumber * secondNumber
        print(result)
    elif (command.lower() == "div"):
        firstNumber = int(input("Ingrese el primer numero "))
        secondNumber = int(input("Ingrese el segundo numero "))
        result = firstNumber / secondNumber
        print(result)
    elif (command.lower() == "resta"):
        firstNumber = int(input("Ingrese el primer numero "))
        secondNumber = int(input("Ingrese el segundo numero "))
        result = firstNumber - secondNumber
        print(result)
    else:
        print("Operarion no valid")
        break
