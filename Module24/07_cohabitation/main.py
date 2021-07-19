from cohabitation import Human, House
import random


def game():
    for i in range(365):
        game_over = False
        number = random.randint(1, 6)
        print(f'\nDay {i + 1}\nNumber of the cube: {number}\n')

        for men in roommates:
            game_over = men.action(men)

        if game_over:
            break


def roommates_list(number):
    for _ in range(number):
        name = input('Enter the name: ')
        roommates.append(Human(name, new_house))


roommates = []

while True:
    try:
        people_number = int(input('Enter number of roommates: '))
        if isinstance(people_number, int) and people_number > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print('Number must be integer and positive')

new_house = House()
roommates_list(people_number)
game()


