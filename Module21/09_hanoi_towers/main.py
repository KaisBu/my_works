def move(number, start, end):
    if number > 0:
        move(number-1, start, 6 - start - end)

        print('Transfer disk {number} from rod number {start} to rod number {end}'.format(
            number=number,
            start=start,
            end=end
        ))

        move(number-1, 6 - start - end, end)


disks_num = int(input('Enter number of disks: '))
move(disks_num, 1, 3)
