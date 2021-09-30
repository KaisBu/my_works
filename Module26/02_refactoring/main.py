def my_gen(limit: int) -> tuple:
    for x in list_1:
        for y in list_2:
            result = x * y
            yield x, y, result

            if result == limit:
                print('Found!!!')
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for num1, num2, res in my_gen(to_find):
    print(num1, num2, res)

# зачтено
