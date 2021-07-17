class Human:

    def __init__(self, name, house, satiety=50, life=True):
        self.name = name
        self.satiety = satiety
        self.life = life
        self.house = house

    def __str__(self):
        return 'Satiety: ' + str(self.satiety) + '\nLife: ' + str(self.life) + str(self.house)

    def eating(self):
        if self.life:
            if self.house.food >= 5:
                self.house.food -= 5
                self.satiety += 20
                print('{} is eating'.format(self.name))
            else:
                print('Not enough food. {} going to the store'.format(self.name))
                self.shopping()
        else:
            self.human_ded()

    def working(self):
        if self.life:
            self.house.funds += 20
            self.satiety -= 10
            print('{} is working'.format(self.name))
            self.check_satiety()
        else:
            self.human_ded()

    def playing(self):
        if self.life:
            self.satiety -= 10
            print('{} is playing'.format(self.name))
            self.check_satiety()
        else:
            self.human_ded()

    def shopping(self):
        if self.life:
            if self.house.funds >= 20:
                self.house.food += 10
                self.house.funds -= 20
                print('{} goes to the grocery store'.format(self.name))
            else:
                print('Not enough funds. {} going to the work'.format(self.name))
                self.working()
        else:
            self.human_ded()

    def human_ded(self):
        print('{} cannot perform actions, he is ded'.format(self.name))

    def check_satiety(self):
        if self.satiety <= 0:
            self.life = False
            print('{} died'.format(self.name))


class House:

    def __init__(self, food=50, funds=0):
        self.food = food
        self.funds = funds

    def __str__(self):
        return '\nFood: ' + str(self.food) + '\nFunds: ' + str(self.funds)
