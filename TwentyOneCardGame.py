

class Card():
    def __init__ (self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck(Card):
    def __init__(self):
        Card.__init__(self)
        self.cards = list cards
        




