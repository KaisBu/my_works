sym_sum, count = 0, 0

try:
    with open('people.txt', 'r') as people_file:
        for line in people_file:
            length = len(line)
            count += 1

            if line.endswith('\n'):
                length -= 1
                if not line[:-1].isalpha():
                    raise ValueError

            try:
                if length < 3:
                    raise BaseException
                else:
                    sym_sum += length

            except BaseException:
                print('Error on line {count}'.format(count=count))
                with open('errors.log', 'a') as logs:
                    logs.write('Error on line {count}\n'.format(count=count))

except FileNotFoundError:
    print('File not found')
except ValueError:
    print('Names should only be letters')
finally:
    print('\nSum of symbols:', sym_sum)
