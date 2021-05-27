alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_list = list(alphabet)

sentence = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
sentence_list = list(sentence.lower())

cipher = [(alphabet_list[(alphabet_list.index(x) + shift) % len(alphabet_list)]
          if x != ' ' else ' ') for x in sentence_list]

cipher_string = ''.join(cipher)
print('Зашифрованное сообщение:', cipher_string)


