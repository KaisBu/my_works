import random

number = int(input('Enter the number: '))

numbers_list = [random.randint(0, 5) for _ in range(number)]
numbers_list = [i for i in numbers_list if i != 0] + [0] * numbers_list.count(0)

print(numbers_list)
