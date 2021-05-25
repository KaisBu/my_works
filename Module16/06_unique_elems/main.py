first_list = []
second_list = []

for i in range(3):
    num = int(input(f'Enter {i + 1} number into first list: '))
    first_list.append(num)

for i in range(7):
    num = int(input(f'Enter {i + 1} number into second list: '))
    second_list.append(num)

first_list.extend(second_list)
first_list = list(set(first_list))

print('New list:', first_list)
