#python3 -m unittest discover tests
#run all the test

#python3 -m unittest tests/test_card.py
#For 1 test

import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank="Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank="2", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_has_string_rep_with_rank_and_suit(self):
        card = Card("5", "Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")

    def test_has_technical_representation(self):
        card = Card("5", "Diamonds")
        self.assertEqual(repr(card), "Card('5', 'Diamonds')")

    def test_card_has_four_possible_suit_options(self):
        self.assertEqual(
            Card.SUITS,
            ("Hearts", "Spades", "Clubs", "Diamonds")
        )

    def test_card_has_thirteen_possible_rank_options(self):
        self.assertEqual(
            Card.RANKS,
            ("2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace")
        )

    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Hearts")

    def test_card_only_allows_for_valid_suits(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit = "Dots")