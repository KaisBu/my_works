word = input('Enter the word: ')
sym_list = list(word.lower())
count_list = []

for i in range(len(sym_list)):
    count = 0
    for sym in sym_list:
        if sym == sym_list[i]:
            count += 1
    count_list.append(count)

count = 0

for number in count_list:
    if number % 2 != 0:
        count += 1

if count > 1:
    print('The word is not palindrome')
else:
    print('The word is palindrome')

