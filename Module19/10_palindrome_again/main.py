string = input('Enter the string: ')

sym_set = set(list(string))

if (len(string) == (2 * len(sym_set) - 1)) or (len(string) == 2 * len(sym_set)):
    print('Can be made a palindrome')
else:
    print("Can't be made a palindrome")

