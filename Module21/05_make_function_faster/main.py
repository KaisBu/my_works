def calculating_math_func(data, factorials_dict={0: 1}):

    if data in factorials_dict:
        result = factorials_dict[data]
    else:
        result = max(factorials_dict.values())
        for index in range(max(factorials_dict.keys()) + 1, data + 1):
            result *= index
            factorials_dict[index] = result

    print(factorials_dict)
    result /= data ** 3
    result = result ** 10
    return result


while True:
    number = int(input('\nEnter the number: '))
    if number == -1:
        break
    print(calculating_math_func(number))
