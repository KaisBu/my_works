class Property:

    def __init__(self, worth):
        self.__worth = worth

    def tax(self, percent):
        return self.__worth / percent


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.__sum = self.tax(1000)

    def get_tax(self):
        return self.__sum


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.__sum = self.tax(200)

    def get_tax(self):
        return self.__sum


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.__sum = self.tax(500)

    def get_tax(self):
        return self.__sum

