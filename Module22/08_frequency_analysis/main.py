import os, collections


def read_file():
    dictionary = {}
    text_path = os.path.abspath('text.txt')
    file = open(text_path, 'r')

    for string in file:
        for elem in string:
            if elem.isalpha():
                if elem.lower() in dictionary:
                    dictionary[elem.lower()] += 1
                else:
                    dictionary[elem.lower()] = 1

    file.close()
    return dictionary


def sorting_func(dictionary):
    sum_value = sum(dictionary.values())
    sort_dict = collections.OrderedDict()

    for key, value in dictionary.items():
        value = round(value / sum_value, 3)
        if value in sort_dict:
            sort_dict[value].append(key)
        else:
            sort_dict[value] = [key]

    return sort_dict


def analysis(dictionary):
    analysis_path = os.path.abspath('analysis.txt')
    analysis_file = open(analysis_path, 'a')

    for key in sorted(dictionary.keys(), reverse=True):
        for letter in sorted(dictionary[key]):
            string = '{letter} {key}\n'.format(
                letter=letter,
                key=key
            )
            analysis_file.write(string)

    analysis_file.close()


letters_dict = read_file()
letters_dict = sorting_func(letters_dict)
analysis(letters_dict)
