from card import Card
from deck import Deck

deck = Deck()
deck.shuffle()

hands = deck.deal(2, 7)
p1 = hands[0]
p2 = hands[1]

p1.sort()
p2.sort()

print(p1)
print(p2)