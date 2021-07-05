import os


def read_file():
    text_path = os.path.abspath('text.txt')
    file = open(text_path, 'r')

    for string in file:
        for elem in string:
            if elem.isalpha():
                if elem.lower() in letters_dict:
                    letters_dict[elem.lower()] += 1
                else:
                    letters_dict[elem.lower()] = 1

    file.close()


def sorting_func(dictionary):
    sum_value = sum(dictionary.values())
    sort_keys, sort_values = [], []

    for key in sorted(dictionary, key=dictionary.get, reverse=True):
        sort_keys.append(key)
        sort_values.append(round(dictionary[key] / sum_value, 3))

    print(sort_keys, sort_values)



letters_dict = {}

read_file()
print(letters_dict)
sorting_func(letters_dict)
