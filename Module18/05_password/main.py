def password_check():
    password = input('Enter new password: ')
    is1 = is2 = is3 = False
    count = 0

    if len(password) < 8:
        print('The password is unreliable, try again')
        password_check()

    if password.isalnum():
        is1 = True

    for sym in password:
        if sym.isdigit():
            count += 1
        elif sym.islower():
            is2 = True
        elif sym.isupper():
            is3 = True

    if count >= 3 and is1*is2*is3:
        print('This is strong password!')
    else:
        print('The password is unreliable, try again')
        password_check()


password_check()
