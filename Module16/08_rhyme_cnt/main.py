total_number = int(input('Enter total number of peoples: '))
number = int(input('Enter counting number: '))
print(f'This mean that every {number} people drop out')
people_list = []
index = 0

for i in range(total_number):
    people_list.append(i + 1)

while len(people_list) != 1:
    print('\nCurrent list:', people_list)
    print('Start counting from number', people_list[index])

    index += number - 1

    while index > len(people_list) - 1:
        index -= (len(people_list))

    print(f'Person number {people_list[index]} drops out')
    people_list.pop(index)

    if index > len(people_list) - 1:
        index -= (len(people_list))

print(f'\nRemaining man number {people_list[0]}')
