class Card:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    """Constructor (Default or Overloaded)"""
    def __init__(self, rank=None, suit=None):
        import random
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["H", "D", "S", "C"]
        if rank and suit:
            if rank in self.ranks:
                self.rank = rank
            else:
                raise Exception("Invalid Rank")
            
            if suit in self.suits:
                self.suit = suit
            else:
                raise Exception("Invalid Suit")
        else:
            self.rank = random.choice(self.ranks)
            self.suit = random.choice(self.suits)
        
        self.suit_name = ""
        if self.suit == "H":
            self.suit_name = "Hearts"
        elif self.suit == "D":
            self.suit_name = "Diamonds"
        elif self.suit == "S":
            self.suit_name = "Spades"
        elif self.suit == "C":
            self.suit_name = "Clubs"

        self.rank_name = ""
        if self.rank == "J":
            self.rank_name = "Jack"

        elif self.rank == "Q":
            self.rank_name = "Queen"

        elif self.rank == "K":
            self.rank_name = "King"

        elif self.rank == "A":
            self.rank_name = "Ace"

        else:
            self.rank_name = self.rank

    def __gt__(self, other):
        order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        c1 = order.index(self.rank)
        c2 = order.index(other.rank)
        if c1 > c2:
            return True
        else:
            return False

    def __lt__(self, other):
        order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        c1 = order.index(self.rank)
        c2 = order.index(other.rank)
        if c1 < c2:
            return True
        else:
            return False

    def __eq__(self, other):
        order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        c1 = order.index(self.rank)
        c2 = order.index(other.rank)
        if c1 == c2:
            return True
        else:
            return False

    def __ge__(self, other):
        order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        c1 = order.index(self.rank)
        c2 = order.index(other.rank)
        if c1 >= c2:
            return True
        else:
            return False

    def __le__(self, other):
        order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        c1 = order.index(self.rank)
        c2 = order.index(other.rank)
        if c1 <= c2:
            return True
        else:
            return False



    def __repr__(self) -> str:
        return f"{self.rank_name} of {self.suit_name}"
