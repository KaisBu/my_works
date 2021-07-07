def gen(col_1, col_2):
    generator = (
        (col_1[index], number)
        for index, number in enumerate(col_2[:min(len(col_1), len(col_2))])
    )
    return generator


def output_on_display(some_list):
    print(some_list[0])

    if len(some_list) > 1:
        output_on_display(some_list[1:])


string = 'abcd'
nums_tuple = 10, 20, 30, 40

print('String: {string}\nTuple of numbers: {tup}'.format(
    string=string,
    tup=nums_tuple
))
gen_1 = gen(string, nums_tuple)
print('\nResult:', '\n{el}'.format(el=gen_1))
output_on_display(list(gen_1))
