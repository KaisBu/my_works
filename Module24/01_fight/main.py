from warrior import Warrior
import random


men_1 = Warrior(1)
men_2 = Warrior(2)

while True:
    rand_number = random.randint(1, 2)

    if rand_number == 1:
        print('\nWarrior_{} attacks warrior_{}'.format(men_1.index, men_2.index))
        men_2.attacked()
    else:
        print('\nWarrior_{} attacks warrior_{}'.format(men_2.index, men_1.index))
        men_1.attacked()

    men_1.print_health()
    men_2.print_health()

    if men_1.health == 0:
        men_2.winner()
        break
    elif men_2.health == 0:
        men_1.winner()
        break
