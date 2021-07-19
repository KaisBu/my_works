class Human:

    def __init__(self, name, house, satiety=50, life=True):
        self.name = name
        self.satiety = satiety
        self.life = life
        self.house = house

    def __str__(self):
        return 'Satiety: ' + str(self.satiety) + '\nLife: ' + str(self.life) + str(self.house)

    def eating(self):
        if self.house.food >= 5:
            self.house.food -= 5
            self.satiety += 20
            print('{} is eating'.format(self.name))
        else:
            print('Not enough food. {} going to the store'.format(self.name))
            self.shopping()

    def working(self):
        self.house.funds += 20
        self.satiety -= 10
        print('{} is working'.format(self.name))

    def playing(self):
        self.satiety -= 10
        print('{} is playing'.format(self.name))

    def shopping(self):
        if self.house.funds >= 20:
            self.house.food += 10
            self.house.funds -= 20
            print('{} goes to the grocery store'.format(self.name))
        else:
            print('Not enough funds. {} going to the work'.format(self.name))
            self.working()

    def check_satiety(self):
        if self.satiety <= 0:
            self.life = False
            print('{} died'.format(self.name))

    def action(self, number):
        self.check_satiety()
        if not self.life:
            print('{} is ded. Game over!'.format(self.name))
            return True

        if self.satiety < 20:
            self.eating()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.funds < 50:
            self.working()
        elif number == 1:
            self.working()
        elif number == 2:
            self.eating()
        else:
            self.playing()

        print(self, '\n')
        return False


class House:

    def __init__(self, food=50, funds=0):
        self.food = food
        self.funds = funds

    def __str__(self):
        return '\nFood: ' + str(self.food) + '\nFunds: ' + str(self.funds)
