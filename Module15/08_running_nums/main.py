initial_list = []

for i in range(5):
    list_item = int(input(f'Enter {i + 1} list item: '))
    initial_list.append(list_item)

shift = int(input('\nEnter the shift: '))

print('Initial list:', initial_list)

for _ in range(shift):
    element = initial_list.pop()
    initial_list.insert(0, element)

print('Shifted list:', initial_list)
