class Cards:

    def __init__(self, card_suit, card_number):
        self.card_suit = card_suit
        self.card_number = card_number

    def value(self, flag):
        if isinstance(self.card_number, int):
            return self.card_number
        elif self.card_number == 'Ace':
            if not flag:
                return 11
            else:
                return 1
        else:
            return 10

    def __str__(self):
        return str(self.card_suit) + ' ' + str(self.card_number)

