import random


original_list = [random.randint(0, 9) for _ in range(10)]

new_list = [
    tuple([original_list[t + i] for i in range(2)])
    for t in range(0, 10, 2)
]

print('Original list:\t\t', original_list)
print('First solution:\t\t', new_list)

list_1 = [original_list[i] for i in range(0, 10, 2)]
list_2 = [original_list[i] for i in range(1, 10, 2)]
new_list2 = list(zip(list_1, list_2))
print('Second solution:\t', new_list2)

new_list3 = list(zip([
    number
    for i, number in enumerate(original_list)
    if i % 2 == 0
], [
    number
    for i, number in enumerate(original_list)
    if i % 2 != 0
]))
print('Third solution:\t\t', new_list3)


