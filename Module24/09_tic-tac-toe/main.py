from players import Player


def print_field():
    print("\n-------------")
    for i in range(3):
        print("|", field_list[0 + i * 3], "|", field_list[1 + i * 3], "|", field_list[2 + i * 3], "|")
        print("-------------")


def players_action(player):
    while True:
        try:
            act_player = int(input('\nWhere to put {}? '.format(player.symbol)))
            if 1 <= act_player <= 9:
                if str(field_list[act_player-1]) not in 'XO':
                    field_list[act_player-1] = player.symbol
                    player.position_list.append(act_player)
                    break
                else:
                    print('This cage is not empty! Try once more')
            else:
                raise ValueError
        except ValueError:
            print('You should enter digit from 1 to 9!')


def main():
    count = 0
    print_field()

    while True:
        count += 1
        if count % 2 != 0:
            players_action(player_1)
        elif count % 2 == 0:
            players_action(player_2)

        print_field()
        winner = win_check()
        if winner:
            print('\n!!!!!!!!!!!The winner is {}!!!!!!!!!!!'.format(winner))
            break
        elif count >= 9:
            print('Draw! Game over!')
            break


def win_check():
    win_combinations = ((1, 2, 3), (1, 4, 7), (7, 8, 9), (3, 6, 9), (1, 5, 9), (3, 5, 7))

    for i_tuple in win_combinations:
        if (i_tuple[0] in player_1.position_list and i_tuple[1] in player_1.position_list
                and i_tuple[2] in player_1.position_list):
            return player_1.name
        elif (i_tuple[0] in player_2.position_list and i_tuple[1] in player_2.position_list
                and i_tuple[2] in player_2.position_list):
            return player_2.name
    else:
        return None


field_list = [i for i in range(1, 10)]
player_1 = Player('Player_1', 'X')
player_2 = Player('Player_2', 'O')

main()






