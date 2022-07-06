import random

# Rank is [1,2,3,4,5,6,7,8,10,11,12,13], where 11 = Jack, 12 = Queen, 13 = King
# Suit is [S,H,C,D]

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        r = str(self.rank)
        if r == "1":
            r = "Ace"
        if r == "11":
            r = "Jack"
        if r == "12":
            r = "Queen"
        if r == "13":
            r = "King"
            
        suits = {
            "S": "spades",
            "H": "hearts",
            "C": "clubs",
            "D": "diamonds"
        }
        return "[%s of %s]" % (r, suits[self.suit])

class Deck(object):
    def __init__(self):
        self.cards = []
        self.dealt = []
        for r in range(1,14):
            for s in ["S", "H", "C", "D"]:
                self.cards.append(Card(r,s))
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, count):
        hand = []
        for i in range(0,count):
            c = self.cards.pop()
            hand.append(c)
            self.dealt.append(c)
        return hand

def value(hand):
    total = 0
    for card in hand:
        # Special rule for face cards.
        if card.rank > 10:
            total += 10
        # Special rule for aces.
        elif card.rank == 1 and total <= 10:
            total += 11
        else:
            total += card.rank
    return total

def handToString(hand):
    s = ""
    for card in hand:
        s += str(card)
    return s

# --- Here begins the main program

def playerStrategy(ph, dh):
    if value(ph) < value(dh) - 1:
        return True
    return False

def dealerStrategy(ph, dh):
    if value(dh) < value(ph):
        return True
    return False

def playGame(ps, ds, d):
    # Returns True if player wins, False if dealer wins.

    playerStands = False
    dealerStands = False

    playerHand = d.deal(2)
    dealerHand = d.deal(2)
    
    print( "--- New Game ---")
    print( "Player:", value(playerHand), handToString(playerHand))
    print( "Dealer:", value(dealerHand), handToString(dealerHand))
    print

    while not playerStands or not dealerStands:
        print( " -- New Round -- ")
        if (ps(playerHand, dealerHand)):
            playerHand.append(d.deal(1)[0])
        else:
            playerStands = True

        print( "Player:", value(playerHand), handToString(playerHand))
    
        if value(playerHand) > 21:
            return False

        if (ds(playerHand, dealerHand)):
            dealerHand.append(d.deal(1)[0])
        else:
            dealerStands = True

        print( "Dealer:", value(dealerHand), handToString(dealerHand))

        if value(dealerHand) > 21:
            return True
        
    print
    return value(playerHand) > value(dealerHand)

gamesPlayed = 0
playerWins = 0
while gamesPlayed < 10000:
    playerWins += playGame(playerStrategy, dealerStrategy, Deck())
    gamesPlayed += 1
    
print(playerWins / 10000)