def composition_check(dictionary, synonym):
    for key in dictionary.keys():
        if synonym.lower() == key.lower():
            print('Synonym:', dictionary.get(key))
            return True


num_words = int(input('Enter number of words: '))
synonym_dict = dict()
inverted_synonym_dict = dict()
is_synonym = False

for i in range(num_words):
    pare = input(f'Pare {i + 1}: ').split()
    synonym_dict[pare[0]] = pare[2]
    inverted_synonym_dict[pare[2]] = pare[0]

while not is_synonym:
    word = input('Enter the word: ')
    is_synonym = composition_check(synonym_dict, word)

    if not is_synonym:
        is_synonym = composition_check(inverted_synonym_dict, word)

    if not is_synonym:
        print('There is no such word in dictionary')
