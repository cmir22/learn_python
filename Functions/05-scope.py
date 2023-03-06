saludo = 25


def saludar():
    #  this is the way to use  global variables
    #  But should not be used global variables
    global saludo
    saludo = 24


print(saludo)
