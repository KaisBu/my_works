string = input('Enter the string: ')
count = 1
new_list = []

for i in range(len(string)):
    if string.find(string[i], i + 1, len(string)) - i == 1:
        count += 1
    else:
        new_list.append(string[i])
        new_list.append(str(count))
        count = 1

print('New string:', ''.join(new_list))
