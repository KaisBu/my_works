def sum_digit(n):
    summ = 0
    for symbol in str(n):
        summ += int(symbol)
    return summ


def numb_digit(n):
    count_d = 0
    for symbol in str(n):
        count_d += 1
    return count_d


N = int(input('Enter the number: '))

summ = sum_digit(N)
count = numb_digit(N)

print('\nSum digits:', summ)
print('Number of digits:', count)
print('Difference between the sum and the number of digits:', summ - count)

