from card import Card
class Deck: 
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["H", "D", "S", "C"]
        self.cards = []

        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)
        return self.cards

    def draw(self):
        card = self.cards[0]
        self.cards.remove(self.cards[0])
        return card
    

    def __repr__(self):
        return f"{self.cards}"
