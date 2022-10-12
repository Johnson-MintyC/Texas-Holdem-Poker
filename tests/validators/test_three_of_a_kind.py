import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        five = Card(rank = "5", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts = Card(rank = "King", suit = "Hearts")
        self.king_of_spades = Card(rank = "King", suit = "Spades")
        ace = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            five,
            self.king_of_diamonds,
            self.king_of_hearts,
            self.king_of_spades,
            ace
        ]
        


    def test_figures_out_exactly_three_of_the_same_rank(self):

        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_three_of_a_kind(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_diamonds,
                self.king_of_hearts,
                self.king_of_spades
            ]
        )