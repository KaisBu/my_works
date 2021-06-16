def converter(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict.keys():
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input('\nEnter the text: ')
original_dict = converter(text)
inverted_dict = dict()

print('\nOriginal dictionary of frequencies:')
for key in sorted(original_dict.keys()):
    print('{key}: {value}'.format(key=key, value=original_dict[key]))
    if original_dict[key] in inverted_dict.keys():
        inverted_dict[original_dict[key]].append(key)
    else:
        inverted_dict[original_dict[key]] = [key]

print('\nInverted dictionary of frequencies:')
for key in sorted(inverted_dict.keys()):
    print('{key}: {value}'.format(key=key, value=inverted_dict[key]))



