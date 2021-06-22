def print_num(num):
    if num == 0:
        return 0

    print_num(num - 1)
    print(num)
    return num + 1


number = 100
print_num(number)
