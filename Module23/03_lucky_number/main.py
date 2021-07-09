import random


num_sum = 0

try:
    while True:
        if num_sum >= 777:
            print('Sum of numbers is more than 777')
            break

        try:
            number = int(input('Enter the number: '))
            if random.randint(1, 13) != 1:
                with open('results.txt', 'a') as results:
                    results.write('{number}\n'.format(number=number))
                num_sum += number
            else:
                raise random

        except ValueError:
            print('The number is entered incorrectly, use only numbers')

except:
    print('Random error')

