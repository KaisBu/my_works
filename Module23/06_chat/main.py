user_name = input('Enter your name: ')

while True:
    action = input('Enter action (to display the chat on the screen - 1, to write the message - 2): ')
    try:
        if action == '1':
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                lines = chat.readlines()
                print(''.join(lines))
        elif action == '2':
            with open('chat.txt', 'a', encoding='utf-8') as chat:
                message = input('{user}: '.format(user=user_name))
                chat.write('{user}: {message}\n'.format(user=user_name, message=message))
        else:
            print('Wrong action')
    except FileNotFoundError:
        print('FileNotFoundError')

