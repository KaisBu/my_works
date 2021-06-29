site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_elem(structure, key, dept=2):
    if key in structure:
        return structure[key]
    elif dept == 0:
        return None

    for dictionary in structure.values():
        if isinstance(dictionary, dict):
            result = search_elem(dictionary, key, dept - 1)
            if result:
                break
    else:
        result = None

    return result


user_key = input('Enter the key: ')
value = search_elem(site, user_key)

while True:
    question = input('Do you want to set the dept? (yes/no) ').lower()

    if question == 'yes':

        while True:
            site_dept = int(input('Enter the dept: '))
            if site_dept <= 2:
                break
            else:
                print('The dept must be lower 3')

        value = search_elem(site, user_key, site_dept)
        break
    elif question == 'no':
        value = search_elem(site, user_key)
        break
    else:
        print('Incorrect answer. Enter yes or no')

if value:
    print('The value:', value)
else:
    print('There is not such key in structure.')