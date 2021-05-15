word = input('Enter the word: ')
sym_list = list(word.lower())
reversed_list = list(word.lower())
reversed_list.reverse()

if sym_list == reversed_list:
    print('The word is palindrome')
else:
    print('The word is not palindrome')




