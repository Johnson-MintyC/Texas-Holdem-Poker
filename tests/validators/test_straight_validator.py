import unittest
from wsgiref.validate import validator

from poker.card import Card
from poker.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        two = Card(rank = "2", suit = "Hearts")
        six = Card(rank = "6", suit = "Hearts")
        self.seven = Card(rank = "7", suit = "Diamonds")
        self.eight = Card(rank = "8", suit = "Spades")
        self.nine = Card(rank = "9", suit = "Clubs")
        self.ten = Card(rank = "10", suit = "Hearts")
        self.jack = Card(rank = "Jack", suit = "Clubs")

        self.cards = [
            two,
            six,
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack
        ]

    def test_figures_out__out_five_cards_in_a_row(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_highest_cards_straight(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven,
                self.eight,
                self.nine,
                self.ten,
                self.jack   
            ]
        )