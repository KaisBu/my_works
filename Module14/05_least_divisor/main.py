n = int(input('Enter the number: '))

if n < 0:
    n = - n

for i in range(2, n + 1):
    if n % i == 0:
        print('Smallest divisor other than one:', i)
        break
