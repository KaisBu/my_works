def arithmetic_operations(some_list, res=0):
    if some_list[1] == '+':
        res = int(some_list[0]) + int(some_list[2])
    elif some_list[1] == '-':
        res = int(some_list[0]) - int(some_list[2])
    elif some_list[1] == '*':
        res = int(some_list[0]) * int(some_list[2])
    elif some_list[1] == '/' or some_list[1] == '//':
        if int(some_list[2]) != 0:
            if some_list[1] == '/':
                res = int(some_list[0]) / int(some_list[2])
            else:
                res = int(some_list[0]) // int(some_list[2])
        else:
            raise ZeroDivisionError
    elif some_list[1] == '**':
        res = int(some_list[0]) ** int(some_list[2])
    elif some_list[1] == '%':
        res = int(some_list[0]) % int(some_list[2])

    return res


def check_func(some_list):
    if len(some_list) != 3:
        raise IndexError
    elif not some_list[0].isdigit() or not some_list[2].isdigit():
        raise ValueError
    elif some_list[1] not in arithmetic_list:
        raise SyntaxError
    else:
        return arithmetic_operations(some_list)


def action_fun():
    action = input('Do you want to fix it? (y/n): ').lower()
    if action == 'y':
        new_line = input('Enter the string: ').split()
        return check_func(new_line)
    else:
        return 0


result_sum = 0
arithmetic_list = ['+', '-', '*', '/', '**', '%', '//']

with open('calc.txt', 'r') as calc_file:
    for line in calc_file:
        line_list = line.split()

        try:
            result_sum += check_func(line_list)

        except IndexError:
            print('IndexError in line:', line, end='')
            result_sum += action_fun()
        except ValueError:
            print('ValueError in line:', line, end='')
            result_sum += action_fun()
        except SyntaxError:
            print('SyntaxError in line:', line, end='')
            result_sum += action_fun()
        except ZeroDivisionError:
            print('ZeroDivisionError in line:', line, end='')
            result_sum += action_fun()

print('\nResult:', result_sum)

