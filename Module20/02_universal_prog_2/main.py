def input_collection():
    input_string = input('Enter the variable: ')
    return input_string


def elements_list_function(collection):
    if isinstance(collection, dict):
        el_list = dict_fun(collection)
    else:
        el_list = other_fun(collection)
    return el_list


def dict_fun(dictionary):
    el_list = [
        dict_value
        for key, dict_value in dictionary.items()
        if is_prime(key)
    ]
    return el_list


def other_fun(collection):
    el_list = [
        symbol
        for i, symbol in enumerate(collection)
        if is_prime(i)
    ]
    return el_list


def is_prime(number):
    n = 2
    j = 0
    while True:
        if n ** 2 <= number and j != 1:
            if number % n == 0:
                j += 1
            n += 1
        elif j == 1 or number < 2:
            return False
        else:
            return True


collection_kind = input('Enter the kind of collection that the input '
                        'variable should match (tuple, string, list or dict): ')
variable = ''
if collection_kind == 'tuple':
    variable = tuple(input_collection().split())
    print('Tuple:', variable)
elif collection_kind == 'string':
    variable = input_collection()
    print('String:', variable)
elif collection_kind == 'list':
    variable = input_collection().split()
    print('List:', variable)
elif collection_kind == 'dict':
    variable = dict()
    num_items = int(input('Enter number of items: '))
    for index in range(num_items):
        value = input_collection()
        variable[index + 1] = value
    print('\nDictionary:', variable)
else:
    print('Incorrect kind of collection')

print('\nResult:', elements_list_function(variable))



