from Potato import PotatoGarden, Gardener


def new_game(gardner):
    while True:
        print("\nThe following actions are available to you:\n"
              "1 - Take the care of garden\n"
              "2 - Harvest from garden bed\n"
              "3 - Check stock\n"
              "4 - Change garden bed\n"
              "5 - Endgame\n")
        try:
            action = int(input('Enter the action: '))

            if action == 1:
                gardner.care_of_garden()
            elif action == 2:
                gardner.harvest()
            elif action == 3:
                gardner.info_stock()
            elif action == 4:
                new_bed = choice_of_beds(gardner.name)
                gardner.plant_bed = garden_list[new_bed - 1]
            elif action == 5:
                print('Game over')
                break
            else:
                raise ValueError

        except ValueError:
            print('Action must be integer from 1 to 5')


def choice_of_beds(name):
    print('\nYou have {} beds'.format(len(garden_list)))
    while True:
        try:
            index = int(input('Which garden bed will the gardener {name} look after? '.format(
                name=name
            )))
            if 0 < index <= len(garden_list):
                return index
            else:
                raise ValueError
        except ValueError:
            print("Bed's index must be integer, positive and no more than {}".format(len(garden_list)))


def beds_list():
    while True:
        try:
            number_of_beds = int(input('Enter total number of beds \n(at this stage you can '
                                       'purchase no more than 2 beds): '))
            if 0 < number_of_beds <= 2:
                bed_list = [PotatoGarden(index) for index in range(1, number_of_beds + 1)]
                return bed_list
            else:
                raise ValueError
        except ValueError:
            print('Total number of beds must be integer, positive and no more than 2\n')


gardener_name = input('Enter the name of the gardener: ')
garden_list = beds_list()
bed_index = choice_of_beds(gardener_name)
first_gardener = Gardener(gardener_name, garden_list[bed_index - 1])

new_game(first_gardener)

