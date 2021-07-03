import os


def zen_print(path):
    zen_text = open(path, 'r')

    for line in zen_text:
        print(line[-1::-1], end='')

    zen_text.close()


zen_print(os.path.abspath('zen.txt'))

