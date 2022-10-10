class GameRound():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self):
        # Shuffle the deck
        self.deck.shuffle()