import unittest
from unittest.mock import MagicMock

from poker.hand import Hand
from poker.player import Player

class PlayerTest(unittest.TestCase):
    def test_stores_name_hand(self):
        hand = Hand(cards = [])
        player = Player(name = "Timmy", hand = hand)
        self.assertEqual(player.name, "Timmy")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        player = Player(name = "Jimmy", hand = mock_hand)

        player.best_hand()
        mock_hand.best_rank.assert_called()