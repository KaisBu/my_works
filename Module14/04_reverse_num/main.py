def invert_symbol(numb):
    digits = ''
    for symbol in reversed(numb):
        if symbol == '.':
            break
        digits += symbol
    return digits


def whole_part(numb):
    digits = ''
    for symbol in numb:
        if symbol == '.':
            break
        digits += symbol
    return float(invert_symbol(digits))


def after_point(numb):
    count = 0
    digit = invert_symbol(numb)
    for symbol in digit:
        count += 1
    return float(digit) / 10 ** count


numb1 = float(input('\nEnter first number: '))
numb2 = float(input('Enter second number: '))

numb1 = whole_part(str(numb1)) + after_point(str(numb1))
numb2 = whole_part(str(numb2)) + after_point(str(numb2))

print('\nFirst reversed number:', numb1)
print('Second reversed number:', numb2)
print('Sum:', numb1 + numb2)





