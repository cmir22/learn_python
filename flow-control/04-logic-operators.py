# and, or , not

gas = True
on = True
age = 18


if gas and on:
    print('Able to turn on')

if gas or on:
    print('Able to turn on')

if not gas and on and age > 17:
    print('Able to turn on and age required')

if gas and (on or age > 17):
    print('Able to turn on and age required')
