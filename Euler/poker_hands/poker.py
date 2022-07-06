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

#player_hands = deal(deck, 2, 5)
#print_hands(player_hands)


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

def one_pair(hand1, hand2):

    h1_ranks = []
    for card in hand1:
        h1_ranks.append(card.rank)
    
    h1_pairs = [rank for rank in h1_ranks if h1_ranks.count(rank) > 1]
    #print(h1_pairs)

    h1_card_pairs = []
    for card in hand1:
        if card.rank in h1_pairs:
            h1_card_pairs.append(card)
    #print(h1_card_pairs)

    h2_ranks = []
    for card in hand2:
        h2_ranks.append(card.rank)

    h2_pairs = [rank for rank in h2_ranks if h2_ranks.count(rank) > 1]
    #print(h2_pairs)

    h2_card_pairs = []
    for card in hand2:
        if card.rank in h2_pairs:
            h2_card_pairs.append(card)
    #print(h2_card_pairs)

    if len(h1_card_pairs) != 0 or len(h2_card_pairs) != 0:
        if len(h1_card_pairs) == 0:
            print(f"Player 2 wins with a pair of {max(h2_card_pairs).rank_name}s!")
        
        elif len(h2_card_pairs) == 0:
            print(f"Player 1 wins with a pair of {max(h1_card_pairs).rank_name}s!")

        elif max(h1_card_pairs) > max(h2_card_pairs):
            print(f"Player 1 wins with a pair of {max(h1_card_pairs).rank_name}s!")
        
        elif max(h2_card_pairs) > max(h1_card_pairs):
            print(f"Player 2 wins with a pair of {max(h2_card_pairs).rank_name}s!")
        
        else:
            print(f"Each Player has a pair of {max(h2_card_pairs).rank_name}s")
    else:
        print("Neither Player has a pair")


#one_pair(player_hands[0], player_hands[1])

def two_pair(hand1, hand2):
    h1_ranks = []
    for card in hand1:
        h1_ranks.append(card.rank)
    
    h1_pairs = [rank for rank in h1_ranks if h1_ranks.count(rank) > 1]
    #print(h1_pairs)

    h1_card_pairs = []
    for card in hand1:
        if card.rank in h1_pairs:
            h1_card_pairs.append(card)
    #print(h1_card_pairs)

    h2_ranks = []
    for card in hand2:
        h2_ranks.append(card.rank)

    h2_pairs = [rank for rank in h2_ranks if h2_ranks.count(rank) > 1]
    #print(h2_pairs)

    h2_card_pairs = []
    for card in hand2:
        if card.rank in h2_pairs:
            h2_card_pairs.append(card)
    #print(h2_card_pairs)

    if len(h1_card_pairs) >= 4 or len(h2_card_pairs) >= 4:
        if len(h1_card_pairs) == 0:
            print(f"Player 2 wins with a pair of {max(h2_card_pairs).rank_name}s and a pair of {min(h2_card_pairs).rank_name}s!")
        
        elif len(h2_card_pairs) == 0:
            print(f"Player 1 wins with a pair of {max(h1_card_pairs).rank_name}s and a pair of {min(h1_card_pairs).rank_name}s!")

        elif max(h1_card_pairs) > max(h2_card_pairs):
            print(f"Player 1 wins with a pair of {max(h1_card_pairs).rank_name}s and a pair of {min(h1_card_pairs).rank_name}s!")
        
        elif max(h2_card_pairs) > max(h1_card_pairs):
            print(f"Player 2 wins with a pair of {max(h2_card_pairs).rank_name}s and a pair of {min(h2_card_pairs).rank_name}s!")
        
        elif min(h1_card_pairs) > min(h2_card_pairs):
            print(f"Player 1 wins with a pair of {max(h1_card_pairs).rank_name}s and a pair of {min(h1_card_pairs).rank_name}s!")

        elif min(h2_card_pairs) > min(h1_card_pairs):
            print(f"Player 1 wins with a pair of {max(h1_card_pairs).rank_name}s and a pair of {min(h1_card_pairs).rank_name}s!")

        else:
            print(f"Each Player has a pair of {max(h1_card_pairs).rank_name}s and a pair of {min(h1_card_pairs).rank_name}s.")
    else:
        print("Neither Player has a two pair")

two_pair1 = [Card("J", "C"), Card("K", "D"), Card("J", "D"), Card("K", "H"), Card("4", "S")]
two_pair2 = [Card("5", "C"), Card("K", "H"), Card("5", "S"), Card("K", "C"), Card("7", "H")]
two_pair3 = [Card("A", "H"), Card("3", "S"), Card("A", "S"), Card("7", "C"), Card("7", "H")]
#print(two_pair1)
#print(two_pair2)
#print(two_pair3)
#two_pair(two_pair1, two_pair2)


def three_of_a_kind(hand1, hand2):
    h1_ranks = []
    for card in hand1:
        h1_ranks.append(card.rank)

    h1_threes = [rank for rank in h1_ranks if h1_ranks.count(rank) > 2]

    h1_card_threes = []
    for card in hand1:
        if card.rank in h1_threes:
            h1_card_threes.append(card)
    print(h1_card_threes)

    h2_ranks = []
    for card in hand2:
        h2_ranks.append(card.rank)

    h2_threes = [rank for rank in h2_ranks if h2_ranks.count(rank) > 2]

    h2_card_threes = []
    for card in hand2:
        if card.rank in h2_threes:
            h2_card_threes.append(card)
    print(h2_card_threes)

    if len(h1_card_threes) >= 3 or len(h2_card_threes) >= 3:
        if len(h2_card_threes) == 0:
            print(f"Player 1 wins with three {max(h1_card_threes).rank_name}s!")

        elif len(h1_card_threes) == 0:
            print(f"Player 2 wins with three {max(h2_card_threes).rank_name}s!")

        elif max(h1_card_threes) > max(h2_card_threes):
            print(f"Player 1 wins with three {max(h1_card_threes).rank_name}s!")
        
        elif max(h2_card_threes) > max(h1_card_threes):
            print(f"Player 2 wins with three {max(h2_card_threes).rank_name}s!")

        else:
            print(f"Each Player has three {max(h1_card_threes).rank}s.")

    else:
        print("Neither Player has three of a kind.")

three1 = [Card("4", "C"), Card("4", "H"), Card("A", "D"), Card("4", "S"), Card("6", "C")]
three2 = [Card("7", "C"), Card("7", "S"), Card("K", "H"), Card("7", "D"), Card("9", "S")]

#three_of_a_kind(three1, three2)

def straight(hand1, hand2):
    hand1.sort()
    for i in range(1, len(hand1)):
        if hand1[i] > hand1[i-1]:
            hand1_straight = True
        else:
            hand1_straight = False
            break
    
    hand2.sort()
    for i in range(1, len(hand2)):
        if hand2[i] > hand2[i-1]:
            hand2_straight = True
        else:
            hand2_straight = False
            break

    if hand1_straight and hand2_straight:
        if max(hand1) > max(hand2):
            print("Player 1 wins on a Straight!")

        elif max(hand2) > max(hand1):
            print("Player 2 wins on a Straight!")
        
        else:
            print("Players have the same Straight!")

    elif hand1_straight:
        print("Player 1 wins on a Straight!")

    elif hand2_straight:
        print("Player 2 wins on a Straight!")

straight1 = [Card("8", "H"), Card("6", "C"), Card("10", "D"), Card("7", "S"), Card("9", "H")]
straight2 = [Card("J", "D"), Card("A", "H"), Card("K", "S"), Card("10", "C"), Card("Q", "D")]
straight3 = [Card("5", "D"), Card("A", "H"), Card("7", "S"), Card("10", "C"), Card("Q", "D")]
#straight(straight3, straight1)

def flush(hand1, hand2):
    suit = hand1[0].suit
    for card in hand1:
        if card.suit == suit:
            h1_flush = True
        else:
            h1_flush = False
            break

    suit = hand2[0].suit
    for card in hand2:
        if card.suit == suit:
            h2_flush = True
        else:
            h2_flush = False
            break

    if h1_flush and h2_flush:
        if max(hand1) > max(hand2):
            print("Player 1 wins on a Flush!")
        elif max(hand2) > max(hand1):
            print("Player 2 wins on a Flush!")
        else:
            print("Players have the same Flush")

    elif h1_flush:
        print("Player 1 wins on a Flush!")

    elif h2_flush:
        print("Player 2 wins on a Flush!")


flush1 = [Card("5", "H"), Card("10", "H"), Card("A", "H"), Card("2", "H"), Card("9", "H")]
flush2 = [Card("4", "C"), Card("7", "C"), Card("K", "C"), Card("J", "C"), Card("9", "C")]
flush3 = [Card("5", "H"), Card("10", "H"), Card("A", "H"), Card("2", "H"), Card("9", "H")]

flush(flush1, flush3)

def four_of_a_kind(hand1, hand2):
    h1_ranks = []
    for card in hand1:
        h1_ranks.append(card.rank)

    h1_four = [rank for rank in h1_ranks if h1_ranks.count(rank) > 3]

    h1_card_four = []
    for card in hand1:
        if card.rank in h1_four:
            h1_card_four.append(card)

    h2_ranks = []
    for card in hand2:
        h2_ranks.append(card.rank)

    h2_four = [rank for rank in h2_ranks if h2_ranks.count(rank) > 3]

    h2_card_four = []
    for card in hand2:
        if card.rank in h2_four:
            h2_card_four.append(card)

    if len(h1_card_four) >= 3 or len(h2_card_four) >= 3:
        if len(h2_card_four) == 0:
            print(f"Player 1 wins with four {max(h1_card_four).rank_name}s!")

        elif len(h1_card_four) == 0:
            print(f"Player 2 wins with four {max(h2_card_four).rank_name}s!")

        elif max(h1_card_four) > max(h2_card_four):
            print(f"Player 1 wins with four {max(h1_card_four).rank_name}s!")
        
        elif max(h2_card_four) > max(h1_card_four):
            print(f"Player 2 wins with four {max(h2_card_four).rank_name}s!")

        else:
            print(f"Each Player has four {max(h1_card_four).rank}s.")

    else:
        print("Neither Player has four of a kind.")






    
        
        



    
