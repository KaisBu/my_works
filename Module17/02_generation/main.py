num = int(input('Enter the number: '))

num_list = [i for i in range(num)]
new_list = [(1 if (num_list.index(x) + 1) % 2 != 0 else x % 5)
            for x in num_list]

print('Result:', new_list)
