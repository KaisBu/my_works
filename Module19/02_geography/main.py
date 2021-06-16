def get_key(dictionary, city):
    for key in dictionary.keys():
        if city in dictionary[key]:
            return key


countries = dict()
num_countries = int(input('\nEnter number of countries: '))

for i in range(num_countries):
    country = input(f'Country {i+1}: ').split()
    countries[country[0]] = country[1:]

for i in range(3):
    is_town = False
    town = input(f'\nTown {i+1}: ')

    for towns in countries.values():
        if town in towns:
            print('{town} city located in'.format(town=town),
                  get_key(countries, town))
            is_town = True
            break

    if not is_town:
        print('No data for the city of {city}'.format(city=town))
