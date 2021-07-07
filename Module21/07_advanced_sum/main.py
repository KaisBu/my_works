def advanced_sum(some_exp, summ=0):
    if isinstance(some_exp, int):
        summ = some_exp
        return summ

    for element in some_exp:
        summ += advanced_sum(element)

    return summ


expression_1 = [[1, 2, [3]], [1], 3]
print('The answer:', advanced_sum(expression_1))
expression_2 = (1, 2, 3, 4, 5)
print('\nThe answer:', advanced_sum(expression_2))

