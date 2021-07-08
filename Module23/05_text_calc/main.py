result_sum = 0
arithmetic_operations = ['+', '-', '*', '/', '**', '%', '//']

with open('calc.txt', 'r') as calc_file:
    for line in calc_file:
        line_list = line.split()

        try:
            if len(line_list) != 3:
                raise IndexError
            elif not line_list[0].isdigit() or not line_list[2].isdigit():
                raise ValueError
            elif line_list[1] not in arithmetic_operations:
                raise SyntaxError
            else:
                if line_list[1] == '+':
                    result_sum += int(line_list[0]) + int(line_list[2])
                elif line_list[1] == '-':
                    result_sum += int(line_list[0]) - int(line_list[2])
                elif line_list[1] == '*':
                    result_sum += int(line_list[0]) * int(line_list[2])
                elif line_list[1] == '/' or line_list[1] == '//':
                    if int(line_list[2]) != 0:
                        if line_list[1] == '/':
                            result_sum += int(line_list[0]) / int(line_list[2])
                        else:
                            result_sum += int(line_list[0]) // int(line_list[2])
                    else:
                        raise ZeroDivisionError
                elif line_list[1] == '**':
                    result_sum += int(line_list[0]) ** int(line_list[2])
                elif line_list[1] == '%':
                    result_sum += int(line_list[0]) % int(line_list[2])

        except IndexError:
            print('IndexError', line, end='')
        except ValueError:
            print('ValueError', line, end='')
        except SyntaxError:
            print('SyntaxError', line, end='')
        except ZeroDivisionError:
            print('ZeroDivisionError', line, end='')

print('\nResult:', result_sum)



