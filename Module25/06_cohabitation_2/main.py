from cohabitation_2 import *
import random


def game():
    game_over = False

    for i in range(365):
        print(f'\nDay {i+1}:')
        family_house.daily_dust()

        for member in roommates:
            if isinstance(member, Husband) or isinstance(member, Wife) or isinstance(member, Child):
                game_over = member.action(roommates[random.randint(3, 5)])
            else:
                game_over = member.action()

            if game_over:
                break
        if game_over:
            break


def roommates_list():
    for index, i_member in enumerate(all_family):
        name = input('Enter {} name: '.format(str_list[index]))
        roommates.append(i_member(name, family_house))


roommates = []
all_family = (Husband, Wife, Child, Cat, Cat, Cat)
str_list = ["husband's", "wife's", "child's", "first cat's", "second cat's", "third cat's"]
family_house = House()
roommates_list()
game()
