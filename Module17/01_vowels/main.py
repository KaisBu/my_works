sentence = input('Введите предложение: ')
sentence_list = list(sentence)
letters_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

new_list = [sym for sym in sentence_list if sym in letters_list]

print('Список гласный букы:', new_list)
print('Длина списка:', len(new_list))
