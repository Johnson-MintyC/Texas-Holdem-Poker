import unittest
from unittest.mock import patch

from poker.deck import Deck
from poker.card import Card

class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_the_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards, 
            []
        )

    def test_adds_cards_to_its_collection(self):
        card = Card(rank="Ace", suit="Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards,
             [card]
        )
    
    @patch('random.shuffle')
    def test_shuffle_cards_in_random_order(self, mock_shuffle):
        deck = Deck()

        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "8", suit = "Diamonds")
        ]

        deck.add_cards(cards)

        deck.shuffle()

        mock_shuffle.assert_called_once_with(cards)
