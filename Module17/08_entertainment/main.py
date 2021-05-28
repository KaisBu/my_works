import random

sticks_number = int(input('Enter number of sticks: '))
throws_number = int(input('Enter number of throws: '))

sticks = ['I' for _ in range(sticks_number)]

for i in range(throws_number):
    a = random.randint(0, sticks_number - 1)
    b = random.randint(a, sticks_number - 1)
    print(f'Trow number {i + 1}: knocked down sticks from number '
          f'{a + 1} to number {b + 1}')
    sticks[a:b + 1] = ['.'] * ((b + 1) - a)

sticks_string = ''.join(sticks)

print('\nResult:', sticks_string)


