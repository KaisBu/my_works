import random


class Potato:
    states = {0: 'Absent', 1: 'Sprout', 2: 'Green', 3: 'Mature'}

    def __init__(self, index):
        self.state = 0
        self.index = index

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Potato {index} in state {state}'.format(
            index=self.index,
            state=self.states[self.state]
        ))

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def potato_yield(self):
        num_potatoes = random.randint(1, 5)
        self.state = 0
        print('Potato {index} in state {state}'.format(
            index=self.index,
            state=self.states[self.state]))
        return num_potatoes


class PotatoGarden:

    def __init__(self, index, count=5):
        self.index = index
        self.potatoes_list = [Potato(i) for i in range(1, count + 1)]

    def grow_all(self):
        print('The potatoes is sprouting')
        for i_potato in self.potatoes_list:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes_list:
            if not i_potato.is_ripe():
                print('The potatoes is not ripe yet')
                return False
        else:
            print('All the potatoes are ripe. You can harvest!')
            return True

    def harvesting(self):
        sum_potatoes = 0
        print('Harvest in progress')
        for i_potato in self.potatoes_list:
            sum_potatoes += i_potato.potato_yield()

        return sum_potatoes


class Gardener:
    stock_of_potatoes = []

    def __init__(self, name, plant_bed):
        self.name = name
        self.plant_bed = plant_bed

    def care_of_garden(self):
        print('Gardener {name} is taking care of garden bed'.format(name=self.name))
        self.plant_bed.grow_all()

    def harvest(self):
        print('Gardener {name} is harvesting garden bed'.format(name=self.name))
        if self.plant_bed.are_all_ripe():
            self.stock_of_potatoes.append(self.plant_bed.harvesting())

    def info_stock(self):
        print('Harvested crop:', ', '.join([str(elem) for elem in self.stock_of_potatoes]))
        print('Total reserves:', sum(self.stock_of_potatoes))

    def change_garden_bed(self, new_plant_bed):
        self.plant_bed = new_plant_bed






