import os


def int_sum(path, path_2):
    numbers_text = open(path, 'r', encoding='utf-8')
    answer_text = open(path_2, 'w')
    summ = 0

    for line in numbers_text:
        for elem in line.split():
            if elem.isdigit():
                summ += int(elem)

    answer_text.write(str(summ))

    numbers_text.close()
    answer_text.close()


int_sum(os.path.abspath('numbers.txt'), os.path.abspath('answer.txt'))

