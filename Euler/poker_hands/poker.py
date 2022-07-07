from deck import Deck
from card import Card

deck = Deck()
deck.shuffle()

def deal(deck, num_players, num_cards):
    hands = []
    for i in range(0, num_players):
        hands.append([])

    for i in range(0, num_cards):
        for j in range(0, num_players):
            card = deck.draw()
            hands[j].append(card)

    return hands

def print_hands(hands):
    for hand in hands:
        print(f"Player {hands.index(hand)+1} Hand: ")
        print(hand)
        print()

player_hands = deal(deck, 2, 5)
print_hands(player_hands)


"""
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
"""

def high_card(hand1, hand2):
    if max(hand1) > max(hand2):
        print(f"Player 1 wins with {max(hand1)}!")
    elif max(hand2) > max(hand1):
        print(f"Player 2 wins with {max(hand2)}!")
    else:
        print(f"Each Player has a {max(hand1)}.")

#high_card(player_hands[0], player_hands[1])

def get_one_pair(hand):

    ranks = []
    for card in hand:
        ranks.append(card.rank)
    
    pairs = [rank for rank in ranks if ranks.count(rank) > 1]
    #print(h1_pairs)

    card_pairs = []
    for card in hand:
        if card.rank in pairs:
            card_pairs.append(card)
    return card_pairs

def is_one_pair(cards):
    if len(cards) >= 2:
        return True
    else:
        return False


#print(is_one_pair(get_one_pair(player_hands[0])))

def get_two_pair(hand):
    ranks = []
    for card in hand:
        ranks.append(card.rank)
    
    pairs = [rank for rank in ranks if ranks.count(rank) > 1]
    #print(h1_pairs)

    card_pairs = []
    for card in hand:
        if card.rank in pairs:
            card_pairs.append(card)
    return card_pairs

def is_two_pair(cards):
    if len(cards) >= 4:
        return True
    else:
        return False



two_pair1 = [Card("J", "C"), Card("Q", "D"), Card("J", "D"), Card("K", "H"), Card("4", "S")]
two_pair2 = [Card("5", "C"), Card("K", "H"), Card("5", "S"), Card("K", "C"), Card("7", "H")]
two_pair3 = [Card("A", "H"), Card("3", "S"), Card("A", "S"), Card("7", "C"), Card("7", "H")]
#print(is_two_pair((get_two_pair(two_pair1))))


def get_three_of_a_kind(hand):
    ranks = []
    for card in hand:
        ranks.append(card.rank)

    threes = [rank for rank in ranks if ranks.count(rank) > 2]

    card_threes = []
    for card in hand:
        if card.rank in threes:
            card_threes.append(card)
    return card_threes

def is_three_of_a_kind(cards):
    if len(cards) >= 3:
        return True
    else:
        return False


three1 = [Card("4", "C"), Card("2", "H"), Card("A", "D"), Card("4", "S"), Card("6", "C")]
three2 = [Card("7", "C"), Card("7", "S"), Card("K", "H"), Card("7", "D"), Card("9", "S")]

#print(is_three_of_a_kind(get_three_of_a_kind(three1)))

def is_straight(hand):
    hand.sort()
    for i in range(1, len(hand)):
        if hand[i].ranks.index(hand[i].rank) == hand[i-1].ranks.index(hand[i-1].rank) + 1:
            straight = True
        else:
            straight = False
            break

    return straight
    

straight1 = [Card("8", "H"), Card("6", "C"), Card("10", "D"), Card("7", "S"), Card("9", "H")]
straight2 = [Card("J", "D"), Card("A", "H"), Card("K", "S"), Card("10", "C"), Card("Q", "D")]
straight3 = [Card("5", "D"), Card("A", "H"), Card("7", "S"), Card("10", "C"), Card("Q", "D")]
#print(is_straight(straight1))

def is_flush(hand):
    suit = hand[0].suit
    for card in hand:
        if card.suit == suit:
            flush = True
        else:
            flush = False
            break
    return flush



flush1 = [Card("5", "H"), Card("10", "H"), Card("A", "H"), Card("2", "H"), Card("9", "H")]
flush2 = [Card("4", "C"), Card("7", "C"), Card("K", "C"), Card("J", "C"), Card("9", "C")]
flush3 = [Card("5", "H"), Card("10", "H"), Card("A", "H"), Card("2", "H"), Card("9", "H")]

#print(is_flush(flush1))

def is_full_house(hand):
    toak = get_three_of_a_kind(hand)
    op = get_one_pair(hand)
    for card in toak:
        if card in op:
            op.remove(card)
    if is_three_of_a_kind(toak) and is_one_pair(op):
        return True
    else:
        return False

fhouse = [Card("3", "D"), Card("K", "D"), Card("10", "H"), Card("K", "S"), Card("K", "C")]
#print(is_full_house(fhouse))

def get_four_of_a_kind(hand):
    ranks = []
    for card in hand:
        ranks.append(card.rank)

    four = [rank for rank in ranks if ranks.count(rank) > 3]

    card_four = []
    for card in hand:
        if card.rank in four:
            card_four.append(card)
    return card_four

def is_four_of_a_kind(cards):
    if len(cards) == 4:
        return True
    else:
        return False

four1 = [Card("7", "H"), Card("10", "D"), Card("8", "S"), Card("7", "C"), Card("7", "D")]
#print(is_four_of_a_kind((get_four_of_a_kind(four1))))

def is_straight_flush(hand):
    if is_straight(hand) and is_flush(hand):
        return True
    else:
        return False

sf = [Card("5", "S"), Card("6", "S"), Card("10", "S"), Card("8", "S"), Card("9", "S")]
#print(is_straight_flush(sf))

def is_royal_flush(hand):
    if is_straight_flush(hand):
        hand.sort()
        if min(hand).rank == "10":
            return True
        else:
            return False
    else:
        return False

rf = [Card("K", "H"), Card("A", "D"), Card("10", "D"), Card("J", "D"), Card("Q", "D")]
#print(is_royal_flush(rf))







    
        
        



    
