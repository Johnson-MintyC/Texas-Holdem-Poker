import unittest
from wsgiref.validate import validator

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.five_of_clubs = Card(rank = "5", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts = Card(rank = "King", suit = "Hearts")
        self.ace_of_clubs = Card(rank = "Ace", suit = "Clubs")
        self.ace_of_spades = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            self.five_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            self.ace_of_clubs,
            self.ace_of_spades
        ]

    def test_validates_there_is_atleast_two_pair(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collections_of_cards_that_have_pairs(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_diamonds,
                self.king_of_hearts,
                self.ace_of_clubs,
                self.ace_of_spades
            ]
        )
