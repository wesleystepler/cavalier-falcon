from card import Card
class Deck: 
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
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

    def deal(self, num_players, num_cards):
        hands = []
        for i in range(0, num_players):
            hands.append([])

        for i in range(0, num_cards):
            for j in range(0, num_players):
                card = self.draw()
                hands[j].append(card)

        return hands
    

    def __repr__(self):
        return f"{self.cards}"
