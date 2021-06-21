def gen(col_1, col_2):
    col_1 = [sym for sym in col_1]
    col_2 = [sym for sym in col_2]

    if len(col_1) > len(col_2):
        num = len(col_2)
    else:
        num = len(col_1)

    generator = (
        (col_1[index], number)
        for index, number in enumerate(col_2[:num])
    )
    return generator


def output_on_display(archive):
    for element in archive:
        print(element)


string = "abcd"
nums_tuple = 10, 20, 30, 40

print('String: {string}\nTuple of numbers: {tup}'.format(
    string=string,
    tup=nums_tuple
))
gen_1 = gen(string, nums_tuple)
print('\nResult:', '\n{el}'.format(el=gen_1))
output_on_display(gen_1)

lst = [20, 58, 96, 95, 63, 125]
new_set = {1, 2, 3}

print('\nList: {lst}\nTuple of numbers: {new_set}'.format(
    lst=lst,
    new_set=new_set
))
gen_2 = gen(lst, new_set)
print('\nResult:', '\n{el}'.format(el=gen_2))
output_on_display(gen_2)



