class HouseDweller:

    def __init__(self, name, house, satiety=50, life=True):
        self.name = name
        self.satiety = satiety
        self.life = life
        self.house = house

    def check_satiety(self):
        if self.satiety < 0:
            self.life = False
            print('{} died'.format(self.name))

    def __str__(self):
        return 'Satiety: ' + str(self.satiety) + '\nLife: ' + str(self.life) + str(self.house)


class Human(HouseDweller):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.happiness = 100

    def pet_the_cat(self, cat):
        if cat.life:
            self.happiness += 5
            print('{} pets the cat'.format(self.name))

    def check_dirt(self):
        if self.house.dirt > 90:
            self.happiness -= 10
            print('{} losses points of happiness'.format(self.name))

    def check_happiness(self):
        if self.happiness <= 10:
            self.life = False
            print('{} dying of depression'.format(self.name))

    def eating(self):
        if self.house.food >= 30:
            self.house.food -= 30
            self.satiety += 30
            print('{} is eating'.format(self.name))
        elif 0 < self.house.food < 30:
            self.house.food -= self.house.food
            self.satiety += self.house.food
            print('{} is eating'.format(self.name))
        else:
            print('Not enough food. {} going to the store'.format(self.name))


class Husband(Human):

    def __init__(self, name, house):
        super().__init__(name, house)

    def playing(self):
        self.satiety -= 10
        self.happiness += 20
        print('{} is playing'.format(self.name))

    def working(self):
        self.house.funds += 150
        self.satiety -= 10
        print('{} is working'.format(self.name))


class House:

    def __init__(self, food=50, cat_food=20, funds=0, dirt=0):
        self.food = food
        self.cat_food = cat_food
        self.funds = funds
        self.dirt = dirt

    def __str__(self):
        return '\nFood: ' + str(self.food) + '\nFunds: ' + str(self.funds)
