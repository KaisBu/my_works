cell_number = int(input('\nEnter number of cells: '))
values = []

if cell_number <= 0:
    print('Error. Number of cells must be more than zero.')
else:
    for i in range(cell_number):
        efficiency = int(input(f"Efficiency of {i + 1} cell: "))
        if efficiency < i + 1:
            values.append(efficiency)

    print('\nInappropriate values:', end=' ')

    for num in values:
        print(num, end=' ')
