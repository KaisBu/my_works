import random


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
        return '{}\nName: {}\nSatiety: {}\nLife: {}'.format(
            str(self.house), self.name, self.satiety, self.life
        )


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
            print('Not enough food'.format(self.name))

    def __str__(self):
        info = super().__str__()
        return '{}\nHappiness: {}'.format(info, self.happiness)


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

    def action(self, cat):
        self.check_satiety()
        self.check_dirt()
        self.check_happiness()

        if not self.life:
            print('{} is ded. Game over!'.format(self.name))
            return True

        if random.randint(1, 10) == 10:
            self.pet_the_cat(cat)

        if self.satiety < 30:
            self.eating()
        elif self.house.funds < 650:
            self.working()
        else:
            self.playing()

        print(self, '\n')
        return False


class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name, house)

    def shopping(self):
        self.satiety -= 10
        self.house.funds -= 100
        self.house.food += 100
        print('{} went to the grocery store'.format(self.name))

    def pet_store(self):
        self.satiety -= 10
        self.house.funds -= 100
        self.house.cat_food += 100
        print('{} made purchases at a pet store'.format(self.name))

    def buy_fur_coat(self):
        self.satiety -= 10
        self.house.funds -= 350
        self.happiness += 60
        print('{} bought a fur coat. She is vary happy!'.format(self.name))

    def clean_the_house(self):
        self.satiety -= 10

        if self.house.dirt < 100:
            self.house.dirt = 0
        else:
            self.house.dirt -= 100

        print('{} cleaned the house'.format(self.name))

    def action(self, cat):
        self.check_satiety()
        self.check_dirt()
        self.check_happiness()

        if not self.life:
            print('{} is ded. Game over!'.format(self.name))
            return True

        if random.randint(1, 10) == 10:
            self.pet_the_cat(cat)

        if self.satiety < 30:
            self.eating()
        elif (self.house.food < 100) and (self.house.funds >= 100):
            self.shopping()
        elif (self.house.cat_food < 50) and (self.house.funds >= 50):
            self.pet_store()
        elif self.house.funds > 450:
            self.buy_fur_coat()
        else:
            self.clean_the_house()

        print(self, '\n')
        return False


class Child(Human):

    def __init__(self, name, house):
        super().__init__(name, house)

    def walking(self):
        self.satiety -= 10
        self.happiness += 5
        print('{} is walking'.format(self.name))

    def scatter_toys(self):
        self.house.dirt += 5

    def playing(self):
        self.satiety -= 10
        self.happiness += 5
        self.scatter_toys()
        print('{} is playing'.format(self.name))

    def action(self, cat):
        self.check_satiety()
        self.check_dirt()
        self.check_happiness()

        if not self.life:
            print('{} is ded. Game over!'.format(self.name))
            return True

        if random.randint(1, 10) == 10:
            self.pet_the_cat(cat)

        if self.satiety < 30:
            self.eating()
        elif random.randint(1, 2) == 1:
            self.playing()
        else:
            self.walking()

        print(self, '\n')
        return False


class Cat(HouseDweller):

    def __init__(self, name, house):
        super().__init__(name, house)

    def eating(self):
        if self.house.cat_food >= 10:
            self.house.food -= 10
            self.satiety += 20
            print('{} is eating'.format(self.name))
        elif 0 < self.house.cat_food < 10:
            self.house.cat_food -= self.house.cat_food
            self.satiety += self.house.cat_food * 2
            print('{} is eating'.format(self.name))
        else:
            print('Not enough food'.format(self.name))

    def sleep(self):
        self.satiety -= 10
        print('{} is sleeping'.format(self.name))

    def tear_wallpaper(self):
        self.satiety -= 10
        self.house.dirt += 5
        print('{} tearing the wallpaper'.format(self.name))

    def action(self):
        self.check_satiety()

        if not self.life:
            print('{} is ded. Game over!'.format(self.name))
            return True

        if self.satiety < 20:
            self.eating()
        elif random.randint(1, 2) == 1:
            self.tear_wallpaper()
        else:
            self.sleep()

        print(self, '\n')
        return False


class House:

    def __init__(self):
        self.food = 50
        self.cat_food = 30
        self.funds = 100
        self.dirt = 0

    def __str__(self):
        return '\nFood: {}\nFunds: {}\nCat food: {}\nDirt: {}'.format(
            self.food, self.funds, self.cat_food, self.dirt
        )

    def daily_dust(self):
        self.dirt += 5
