string = input('Enter the string: ')
letters = dict()
count = 0

for sym in string:
    letters[sym] = letters.get(sym, 0) + 1

for value in letters.values():
    if value % 2 == 1:
        count += 1

if count <= 1:
    print('Can be palindrome')
else:
    print('Can not be palindrome')


