import os


text_path = os.path.abspath('text.txt')
text_file = open(text_path, 'r')
i = 0
cipher_text = ''

for string in text_file:
    i += 1
    for letter in string:
        if letter.isalpha():
            cipher_text += chr(ord(letter) + i)
    cipher_text += '\n'

text_file.close()

cipher_file = open(os.path.abspath('cipher_text.txt'), 'w')
cipher_file.write(cipher_text)
cipher_file.close()


