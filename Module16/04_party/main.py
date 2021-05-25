guests = ['Peter', 'Vania', 'Sasha', 'Lisa', 'Kate']

while True:
    print(f'\nThe are {len(guests)} people on the party:', guests)
    action = input('Guest has come or gone? ')

    if action.lower() == 'end':
        print('The party is over, everyone went to bed.')
        break

    guest_name = input('Enter quest name: ')

    if action.lower() == 'come':
        if len(guests) < 6:
            guests.append(guest_name)
            print('Hello,', guest_name)
        else:
            print(f'Sorry, {guest_name}, There is no places.')
    elif action.lower() == 'gone':
        if guest_name in guests:
            guests.remove(guest_name)
            print(f'Bye, {guest_name}!')
        else:
            print('There are no people whit that name')
    else:
        print("Error, let's try again")




