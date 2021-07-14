class Warrior:
    health = 100

    def __init__(self, index):
        self.index = index

    def attacked(self):
        self.health -= 20

    def print_health(self):
        print('Warrior_{} health left'.format(self.index), self.health)

    def winner(self):
        print('Warrior_{} win'.format(self.index))
