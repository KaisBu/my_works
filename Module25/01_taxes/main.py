from taxes import Apartment, Car, CountryHouse


def input_func(sentence):
    while True:
        try:
            input_info = int(input('Enter your {}: '.format(sentence)))
            if isinstance(input_info, int):
                return input_info
            else:
                raise ValueError
        except ValueError:
            print('Your {} should be integer'.format(sentence))


capital = input_func('capital')
apartment = Apartment(worth=input_func('apartment cost'))
car = Car(worth=input_func('car cost'))
country_house = CountryHouse(worth=input_func('country house'))

total_taxes = apartment.get_tax() + car.get_tax() + country_house.get_tax()

print('\nYor capital:', capital)
print('Total sum of taxes:', total_taxes)
print('\tApartment tax:', apartment.get_tax())
print('\tCar tax:', car.get_tax())
print('\tCountry hose tax:', country_house.get_tax())

if capital < total_taxes:
    print('\nThe next amount is missing:', total_taxes - capital)





