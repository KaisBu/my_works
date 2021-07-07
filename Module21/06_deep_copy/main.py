site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {phone} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {phone}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def sites_copy(number):
    if number != 0:
        product_name = input('\nEnter product name for the site: ')
        site['html']['head']['title'] = 'Куплю/продам {phone} недорого'.format(phone=product_name)
        site['html']['body']['h2'] = 'У нас самая низкая цена на {phone}'.format(phone=product_name)
        print('Сайт для {name}:'.format(name=product_name), '\nsite = ', end='')
        rec_site_print(site, 0)
        number -= 1
        sites_copy(number)


def rec_site_print(dictionary, count):
    if not isinstance(dictionary, dict):
        return print(dictionary)

    print('{')
    count += 1

    for _ in range(count):
        print('\t', end='')

    for keys, values in dictionary.items():
        print('{keys}: '.format(keys=keys), end='')
        rec_site_print(values, count)

        for _ in range(count):
            print('\t', end='')
    print('}')


# def site_print():
#     print('site = {')
#
#     for key, dictionary in site.items():
#         print('\t{key}:'.format(key=key), '{')
#         for keys, values in dictionary.items():
#             print('\t\t{keys}:'.format(keys=keys), '{')
#             for name, sentence in values.items():
#                 print('\t\t\t{name}: {sentence}'.format(name=name, sentence=sentence))
#             print('\t\t}')
#         print('\t}')
#     print('}')


number_sites = int(input('Enter number of sites: '))
sites_copy(number_sites)



