initial_list = [1, 4, -3, 0, 10]
min_num = initial_list[0]
max_num = initial_list[0]
index = 0

for _ in range(len(initial_list)):
    num = initial_list[index]
    if num <= min_num:
        initial_list.pop(index)
        min_num = num
        initial_list.insert(0, num)
        index += 1
    elif num >= max_num:
        initial_list.pop(index)
        max_num = num
        initial_list.append(num)
    elif min_num < num < max_num and num <= initial_list[index - 1]:
        initial_list.pop(index)
        for number in initial_list:
            if number >= num:
                number_index = initial_list.index(number)
                initial_list.insert(number_index, num)
                index += 1
                break
    else:
        initial_list.pop(index)
        reversed_index = 0
        for number in reversed(initial_list):
            if number <= num:
                initial_list.insert(- 1 - reversed_index, num)
                break
            reversed_index += 1

print(initial_list)


