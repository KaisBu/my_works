number_friend = int(input('Enter total number of friends: '))
number_iou = int(input('Enter number of IOUs: '))
iou_list = []

for _ in range(number_friend):
    iou_list.append(0)

for i in range(number_iou):
    print('\nIOU  number', i + 1)
    index1 = int(input('To whom: '))
    index2 = int(input('By whom: '))
    summ = int(input('How much: '))
    iou_list[index1 - 1] -= summ
    iou_list[index2 - 1] += summ

print('\nFriends balance:')
for num in iou_list:
    print(iou_list.index(num) + 1, ':', num)




