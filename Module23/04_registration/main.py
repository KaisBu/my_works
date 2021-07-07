with open('registrations.txt', 'r', encoding='utf-8') as registrations:

    for line in registrations:
        line_list = line.split()

        try:
            if len(line_list) != 3:
                raise IndexError
            elif not line_list[0].isalpha():
                raise NameError
            elif '@' not in line_list[1] or '.' not in line_list[1]:
                raise SyntaxError
            elif line_list[2].isdigit():
                if int(line_list[2]) < 10 or int(line_list[2]) > 99:
                    raise ValueError
            elif not line_list[2].isdigit():
                raise ValueError

            with open('registrations_good.log', 'a', encoding='utf-8') as reg_good:
                reg_good.write(line)

        except IndexError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as reg_bad:
                reg_bad.write('IndexError\t{line}'.format(line=line))
        except NameError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as reg_bad:
                reg_bad.write('NameError\t{line}'.format(line=line))
        except SyntaxError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as reg_bad:
                reg_bad.write('SyntaxError\t{line}'.format(line=line))
        except ValueError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as reg_bad:
                reg_bad.write('ValueError\t{line}'.format(line=line))

