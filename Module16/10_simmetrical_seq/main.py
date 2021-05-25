def chek(lst):
    reversed_lst = []
    for sym in lst:
        reversed_lst.insert(0, sym)
    if reversed_lst == lst:
        return True
    else:
        return False


total_number = int(input('Enter total number of  numbers: '))
list_number, new_list = [], []

for _ in range(total_number):
    number = int(input('Enter the number: '))
    list_number.append(number)

print('\nThe sequence:', list_number)

for _ in range(len(list_number) - 1):
    if chek(list_number):
        break
    num = list_number[0]
    list_number.pop(0)
    new_list.insert(0, num)

print('Number of missing numbers:', len(new_list))
print('Missing numbers:', new_list)

