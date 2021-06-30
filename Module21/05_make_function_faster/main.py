def calculating_math_func(data):

    if data in factorials_dict:
        result = factorials_dict[data]
    else:
        result = max(factorials_dict.values())
        for index in range(max(factorials_dict.keys()) + 1, data + 1):
            result *= index
            factorials_dict[index] = result

    result /= data ** 3
    result = result ** 10
    return result


factorials_dict = {0: 1}
number = int(input('Enter the number: '))
print(calculating_math_func(number))
