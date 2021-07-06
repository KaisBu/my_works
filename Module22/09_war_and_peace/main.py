import os, zipfile, collections


def read_file(text_path):
    dictionary = {}
    file = open(text_path, 'r', encoding='utf-8')

    for string in file:
        for elem in string:
            if elem.isalpha():
                if elem in dictionary:
                    dictionary[elem] += 1
                else:
                    dictionary[elem] = 1

    file.close()
    dictionary = sorting_dict(dictionary)
    return dictionary


def sorting_dict(dictionary):
    sort_dict = collections.OrderedDict()

    for key in sorted(dictionary, key=dictionary.get, reverse=True):
        sort_dict[key] = dictionary[key]

    return sort_dict


def save_file(dictionary):
    file_path = os.path.abspath('stat_result.txt')
    file = open(file_path, 'w', encoding='utf-8')

    for key, value in dictionary.items():
        print(key, value)
        file.write(' '.join([str(key), str(value), '\n']))

    file.close()


z = zipfile.ZipFile('voyna-i-mir.zip', 'r')
z.extract('voyna-i-mir.txt')
z.close()

creation_path = os.path.abspath('voyna-i-mir.txt')
letters_dict = read_file(creation_path)
save_file(letters_dict)

