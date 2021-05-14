num_video_cards = int(input('\nEnter number of video cards: '))
old_list = []
new_list = []

if num_video_cards <= 0:
    print('Error. Number of video cards must be more than zero.')
else:
    for i in range(num_video_cards):
        number = int(input(f'{i + 1} graphics card: '))
        old_list.append(number)

    for element in old_list:
        if element != max(old_list):
            new_list.append(element)

    print('\nOld video cards list:', old_list)
    print('New video cards list:', new_list)


