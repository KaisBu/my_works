num_orders = int(input('Enter number of orders: '))
orders = dict()

print('\nEnter the order as follows: last_name pizza_name quantity')

for i in range(num_orders):
    order = input(f'Order {i + 1}: ').split()
    if len(order) == 3:
        if order[0] in orders.keys():
            if order[1] in orders[order[0]].keys():
                orders[order[0]][order[1]] += int(order[2])
            else:
                orders[order[0]][order[1]] = int(order[2])
        else:
            orders[order[0]] = dict.fromkeys([order[1]], int(order[2]))
    else:
        print('Incorrect filling form!')

print()

for name in sorted(orders.keys()):
    print('{key}:'.format(key=name))
    for pizza in sorted(orders[name].keys()):
        print('\t{pizza}: {amount}'.format(pizza=pizza, amount=orders[name][pizza]))


