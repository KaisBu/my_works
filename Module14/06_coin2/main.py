import math

x = float(input('Enter X: '))
y = float(input('Enter Y: '))
r = int(input('Enter radius: '))

if math.sqrt(r ** 2) >= math.sqrt(x ** 2 + y ** 2):
    print('A coin is somewhere nearby')
else:
    print('There are no coins in the area')

