string = input('Enter the string: ')
reverse_string = string[::-1]

print(string[len(string) - reverse_string.index('h') - 2:string.index('h'): -1])
