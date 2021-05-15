word = input('Enter the word: ')
sym_list = list(word.lower())
reversed_list = list(word.lower())
reversed_list.reverse()

if sym_list == reversed_list:
    print('The word is palindrome')
else:
    print('The word is not palindrome')



# TODO Можно реализовать иначе, но, в принципе не обязательно. Опишу вам тем не менее этот способ.
#  Итерируем по строке, считая сколько раз встречается каждый элемент в этой строке. Затем смотрим на эти кол-ва.
#  Если нечетных количеств больше 1: строка не палиндром. Если нечетное количество одно или ноль - палиндром.
