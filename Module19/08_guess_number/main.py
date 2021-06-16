max_number = int(input('Enter maximum number: '))
number_set = set(list(i for i in range(max_number + 1)))

while True:
    amount = input('\nIs the required number among these numbers: ').split()

    if ''.join(amount).lower() == 'help!':
        print('Artyom could think of the following numbers',
              ' '.join([str(i) for i in number_set]))
        break

    check_number_set = set([int(i) for i in amount if 0 <= int(i) <= max_number])
    answer = input("Artem's answer: ").lower()

    if answer == 'yes':
        if len(check_number_set) == 1:
            print('Correct!')
            break
        else:
            number_set.intersection_update(check_number_set)
    elif answer == 'no':
        number_set.difference_update(check_number_set)
