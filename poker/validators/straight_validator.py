from poker.validators import FiveCardRankInARowValidator

class StraightValidator(FiveCardRankInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"

    def is_valid(self):
        if len(self.cards) < 5:
            return False


        return len(self._collections_of_five_straight_cards_in_row) >= 1

    def valid_cards(self):
        return self._collections_of_five_straight_cards_in_row[-1]

