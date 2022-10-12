import unittest
from poker.card import Card
from poker.hand import Hand

class HandTest(unittest.TestCase):

    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7", suit = "Clubs")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            repr(hand),
            "7 of Clubs, Ace of Diamonds"
        )


    def test_receives_and_stores_cards(self):
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        six_of_clubs = Card(rank = "6", suit = "Clubs")
        cards = [
            ace_of_spades,
            six_of_clubs
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards,
            [
            six_of_clubs,
            ace_of_spades,
            ]
        )

    def test_figures_out_besk_rank_when_flush(self):
        cards = [
            Card(rank = rank, suit = "Hearts")
            for rank in ["2", "5", "8", "10", "Ace"]
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )

    def test_figures_out_full_house_is_best_rank(self):
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "3", suit = "Spades"),
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "9", suit = "Spades")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Full House"
        )

    def test_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "3", suit = "Spades"),
            Card(rank = "3", suit = "Diamonds"),
            Card(rank = "9", suit = "Spades")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Four of a Kind"
        )

    def test_figures_out_straight_flush_is_best_rank(self):
        cards = [
            Card(rank = "3", suit = "Clubs"),
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "6", suit = "Clubs"),
            Card(rank = "7", suit = "Clubs")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight Flush"
        )

    def test_figures_out_royal_flush_is_best_rank(self):
        cards = [
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Queen", suit = "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            "Royal Flush"
        )


