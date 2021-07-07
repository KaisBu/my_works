def series(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return series(num - 2) + series(num - 1)


position = int(input('Enter the position of number in Fibonacci series: '))
print(series(position))

