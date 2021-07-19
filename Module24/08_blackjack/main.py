from deck_of_cards import Cards
import random


def black_jack():
    print('The player receives two cards')
    delivery(players_cards, 2)
    print('The dealer receives two cards')
    delivery(dealers_cards, 2)
    ace_excess, excess = False, False

    while True:
        print('\nYour cards:')
        for card in players_cards:
            print(card)

        sum_values = sum_of_values(ace_excess)

        if sum_values > 21:
            ace_excess = True
            sum_values = sum_of_values(ace_excess)
            if sum_values > 21:
                excess = True
                print('Your score: {}\nYou lose! Dealer wins!'.format(sum_values))
                break

        print('Your sum of points:', sum_values)

        try:
            action = input('\nDo you want another card? (y/n): ').lower()
            if action == 'y':
                delivery(players_cards, 1)
                print('The player receives a card')
            elif action == 'n':
                break
            else:
                raise ValueError
        except ValueError:
            print('Wrong action! Enter y or n')

    if not excess:
        winners_check(sum_values)


def sum_of_values(flag):
    summ = 0
    for card in players_cards:
        summ += card.value(flag)
    return summ


def delivery(cards_list, count):
    for i in range(count):
        card = random.choice(deck_list)

        if card not in players_cards and card not in dealers_cards:
            cards_list.append(card)
        else:
            delivery(cards_list, count - i)


def winners_check(summ):
    dealers_summ = 0
    print('\nDealers cards:')
    for card in dealers_cards:
        dealers_summ += card.value(False)
        print(card)
    print('\nScore:\nDealer: {}\nPlayer: {}'.format(dealers_summ, summ))

    if dealers_summ > summ:
        print('\n!!!!!Dealer won!!!!!')
    elif dealers_summ < summ:
        print('\n!!!!!Player won!!!!!')
    else:
        print('\nDraw')


numbers_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Ace', 'Jack', 'Lady', 'King']
suits_list = ['Peaks', 'Hearts', 'Diamonds', 'Clubs']
deck_list = [
    Cards(suit, number)
    for suit in suits_list
    for number in numbers_list
]
players_cards, dealers_cards = [], []

black_jack()
