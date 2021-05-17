initial_list = [1, 4, -3, 0, 10]

print('\nInitial list:', initial_list)

for i in range(len(initial_list)):
    min_num = initial_list[i]
    for ind in range(i, len(initial_list)):
        if initial_list[ind] < min_num:
            min_num = initial_list[ind]
    index = initial_list.index(min_num)
    initial_list.pop(index)
    initial_list.insert(i, min_num)

print('Sorted list:', initial_list)


