special_symbols = list('@№$%^&*()')
file_name = input('Enter file name: ')
is_Prime = False

for sym in special_symbols:
    if file_name.startswith(sym):
        is_Prime = True


if not (file_name.endswith('.txt') or file_name.endswith('.docx')):
    print('Error: incorrect file extension')
elif is_Prime:
    print('Error: filename starts with special symbol')
else:
    print('Correct filename.')

