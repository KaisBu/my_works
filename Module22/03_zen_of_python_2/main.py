import os


def zen_of_python_2(path, letters_dict={}):
    path_text = open(path, 'r')
    letters_count, words_count, string_count = 0, 0, 0

    for line in path_text:
        string_count += 1

        for word in line.split():
            words_count += 1

            for element in word:
                if element.isalpha():
                    letters_count += 1
                    if element.lower() in letters_dict:
                        letters_dict[element.lower()] += 1
                    else:
                        letters_dict[element.lower()] = 1

    path_text.close()
    print('Number of letters: {letters}\nNumber of words: {words}\nNumber of strings: {strings}'.format(
        letters=letters_count,
        words=words_count,
        strings=string_count
    ))
    print('The letter with lowest count:', ', '.join([
        key
        for key, value in letters_dict.items()
        if value == min(letters_dict.values())
    ]))


zen_of_python_2(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')))


