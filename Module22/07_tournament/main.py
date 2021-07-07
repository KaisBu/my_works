import os


def read_file():
    first_path = os.path.abspath('first_tour.txt')
    first_tour = open(first_path, 'r')
    min_score = int(first_tour.read(2))
    first_tour.seek(4)

    for string in first_tour:
        string_list = string.split()
        if int(string_list[2]) > min_score:
            second_dict[string_list[2]] = [string_list[1][0] + '.', string_list[0]]

    first_tour.close()


def save_result():
    second_path = os.path.abspath('second_tour.txt')
    second_file = open(second_path, 'a')
    second_file.write(str(len(second_dict)))
    i = 0

    for keys in sorted(second_dict.keys(), reverse=True):
        i += 1
        second_file.write(' '.join([f'\n{i})', ' '.join(second_dict[keys]), str(keys)]))

    second_file.close()


second_dict = {}

read_file()
save_result()



