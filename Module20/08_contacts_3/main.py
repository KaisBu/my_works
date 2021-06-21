phone_book = {
    ('Sidorov', 'Nikita'): 89252542143,
    ('Sidorova', 'Alina'): 89283662514,
    ('Sidorov', 'Pavel'): 89682211017,
    ('Sidorovski', 'Igor'): 89361024780,
    ('Sidoroj', 'Pchemeck'): 89651224571
}


def add(book):
    surname = input('Enter the last name of the new contact: ')
    name = input('Enter the name of the new contact: ')
    phone_number = int(input('Enter the phone number: '))

    if (surname, name) not in book:
        book[(surname, name)] = phone_number

        print('\nPhone book: ')
        for key, value in book.items():
            print(key[0], key[1], '-', value)
    else:
        print('This contact is already exists.')


def search(book):
    surname = input('Enter the last name of the searching contact: ').lower()
    is_in = False

    for names, phone_number in book.items():
        if (names[0].lower()[:len(surname)] == surname.lower()[:len(surname)] and
                abs(len(names[0]) - len(surname)) <= 1):
            print(names[0], names[1], '-', phone_number)
            is_in = True

    if not is_in:
        print('There are no contacts with such a surname in the phone book.')


while True:
    action = input('\nEnter the action (add or search phone number): ').lower()
    if action == 'add':
        add(phone_book)
    elif action == 'search':
        search(phone_book)
    else:
        print('Wrong action. It is impossible perform the action.')




