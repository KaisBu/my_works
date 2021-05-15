word = input('Enter the word: ')
sym_list = list(word)
unique_letters = []


for symbol in sym_list:
    count = -1
    for sym in sym_list:
        if sym == symbol:
            count += 1
    if count == 0:
        unique_letters.append(symbol)

print('Number of unique letters:', len(unique_letters))

