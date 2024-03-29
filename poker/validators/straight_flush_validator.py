from poker.validators import FiveCardRankInARowValidator

class StraightFlushValidator(FiveCardRankInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"

    def is_valid(self):
        for five_cards in self._collections_of_five_straight_cards_in_row:
            unique_suits_in_next_five_cards = { card.suit for card in five_cards }
            if len(unique_suits_in_next_five_cards) == 1:
                return True

        return False

    def valid_cards(self):
        return self._straight_flush_card_bunches[-1]


    @property
    def _straight_flush_card_bunches(self):
        return [
            five_cards
            for five_cards in self._collections_of_five_straight_cards_in_row
            if len({card.suit for card in five_cards}) == 1
        ]