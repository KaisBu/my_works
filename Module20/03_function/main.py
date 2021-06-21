import random


def func_slice(variable, element):
    if variable.count(element) >= 2:
        count, i_1, i_2 = 0, 0, 0
        for index, value in enumerate(variable):
            if count == 0 and value == element:
                i_1 = index
                count += 1
            elif count == 1 and value == element:
                i_2 = index
                break
        return variable[i_1:i_2 + 1]

    elif variable.count(element) == 1:
        return variable[variable.index(element):]
    else:
        return ()


first_tuple = tuple([random.randint(0, 10) for _ in range(20)])
number = int(input('Enter a number from 0 to 10: '))

second_tuple = func_slice(first_tuple, number)
print('Result:', second_tuple)
