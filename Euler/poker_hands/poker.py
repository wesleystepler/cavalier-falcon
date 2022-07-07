import re

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

def high_card(hand):
    return max(hand)

#high_card(player_hands[0], player_hands[1])

def get_one_pair(hand):

    ranks = []
    for card in hand:
        ranks.append(card.rank)
    
    pairs = [rank for rank in ranks if ranks.count(rank) > 1]

    # Narrow the list down to just one pair, and make sure it's the highest pair they have

    card_pairs = []
    for card in hand:
        if card.rank in pairs:
            card_pairs.append(card)

    while len(card_pairs) > 2:
        card_pairs.remove(min(card_pairs))
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

def tie_breaker(hand1, hand2, tied_on):
    h1_one, h2_one = get_one_pair(hand1), get_one_pair(hand2)
    h1_two, h2_two = get_two_pair(hand1), get_two_pair(hand2)
    h1_three, h2_three = get_three_of_a_kind(hand1), get_three_of_a_kind(hand2)
    h1_four, h2_four = get_four_of_a_kind(hand1), get_four_of_a_kind(hand2)

    if tied_on == "High Card":
        hand1.sort()
        hand2.sort()
        i = 3
        while i >= 0:
            if hand1[i] > hand2[i]:
                print("Player 1 Wins the High Card Tie Breaker!")
                return hand1

            elif hand2[i] > hand1[i]:
                print("Player 2 Wins the High Card Tie Breaker!")
                return hand2

            else:
                i += 1

        print("It's a Tie! Split the Pot!")
        return None

    elif tied_on == "One Pair":
        if max(h1_one) > max(h1_two):
            print("Player 1 Wins on a Higher Pair!")
            return hand1
        
        elif max(h2_one) > max(h1_one):
            print("Player 2 Wins on a Higher Pair!")
            return hand2

        else:
            h1 = []
            for card in hand1:
                if card not in h1_one:
                    h1.append(card)

            h2 = []
            for card in hand2:
                if card not in h2_one:
                    h2.append(card)

            h1.sort()
            h2.sort()
            i = len(h1) - 1
            while i >= 0:
                if h1[i] > h2[i]:
                    print("Player 1 Wins on the Pair Tie-Breaker!")
                    return hand1

                elif h2[i] > h1[i]:
                    print("Player 2 Wins on the Pair Tie-Breaker!")
                    return hand2

                else:
                    i -= 1
            print("It's a Tie! Split the Pot!")
            return None


    elif tied_on == "Two Pair":
        if max(h1_two) > max(h2_two):
            print("Player 1 Wins with the Higher Pair!")
            return hand1

        elif max(h2_two) > max(h1_two):
            print("Player 2 Wins with the Higher Pair!")
            return hand2

        elif min(h1_two) > min(h2_two):
            print("Player 1 Wins with the Higher Pair!")
            return hand1

        elif min(h2_two) > min(h1_two):
            print("Player 1 Wins with the Higher Pair!")

        else:
            h1 = []
            for card in hand1:
                if card not in h1_one:
                    h1.append(card)

            h2 = []
            for card in hand2:
                if card not in h2_one:
                    h2.append(card)

            h1.sort()
            h2.sort()
            i = len(h1)
            while i >= 0:
                if h1[i] > h2[i]:
                    print("Player 1 Wins on the Pair Tie-Breaker!")
                    return hand1

                elif h2[i] > h1[i]:
                    print("Player 2 Wins on the Pair Tie-Breaker!")
                    return hand2

                else:
                    i -= 1
            print("It's a Tie!")
            return None


    elif tied_on == "Three of a Kind":
        if max(h1_three) > max(h2_three):
            print("Player 1 Wins on the Higher Set of Three!")
            return hand1

        elif max(h2_three) > max(h1_three):
            print("Player 2 Wins on the Higher Set of Three!")
            return hand2


    elif tied_on == "Straight" or tied_on == "Straight Flush":
        if max(hand1) > max(hand2):
            print("Player 1 Wins on a Higher Straight!")
            return hand1

        elif max(hand2) > max(hand1):
            print("Player 2 Wins on a Higher Straight")
            return hand2

        else:
            print("It's a tie! Split the Pot!")
            return None


    elif  tied_on == "Flush":
        if max(hand1) > max(hand2):
            print("Player 1 Wins on the Higher Card!")
            return hand1

        elif max(hand2) > max(hand1):
            print("PLayer 2 Wins on the Higher Card!")
            return hand2

        else:
            hand1.remove(max(hand1))
            hand2.remove(max(hand2))
            hand1.sort()
            hand2.sort()
            i = len(hand1)
            while i >= 0:
                if hand1[i] > hand2[i]:
                    print("Player 1 Wins on the Pair Tie-Breaker!")
                    return hand1

                elif hand2[i] > hand1[i]:
                    print("Player 2 Wins on the Pair Tie-Breaker!")
                    return hand2

                else:
                    i -= 1
            print("It's a Tie!")
            return None


    elif tied_on == "Full House":
        if max(h1_three) > max(h2_three):
            print("Player 1 Wins with a Higher Set of Three!")
            return hand1
        
        elif max(h2_three) > max(h1_three):
            print("Player 2 Wins with a Higher Set of Three!")
            return hand2

    
    elif tied_on == "Four of a Kind":
        if max(h1_four) > max(h2_four):
            print("Player 1 Wins with a Higher Set of Four!")
            return hand1

        elif max(h2_four) > max(h1_four):
            print("Player 2 Wins with a Higher Set of Four!")
            return hand2


    return None

def determine_winner(hand1, hand2):
    h1_one, h2_one = get_one_pair(hand1), get_one_pair(hand2)
    h1_two, h2_two = get_two_pair(hand1), get_two_pair(hand2)
    h1_three, h2_three = get_three_of_a_kind(hand1), get_three_of_a_kind(hand2)
    h1_four, h2_four = get_four_of_a_kind(hand1), get_four_of_a_kind(hand2)


    if is_royal_flush(hand1) or is_royal_flush(hand2):
        if not is_royal_flush(hand2):
            print("Player 1 wins on a Royal Flush! Woah!")
            return hand1

        elif not is_royal_flush(hand1):
            print("Player 2 wins on a Royal Flush! Woah!")
            return hand2

        else:
            print("Holy Heck!! TWO ROYAL FLUSHES! Split the Pot!!!")

    elif is_straight_flush(hand1) or is_straight_flush(hand2):
        if not is_straight_flush(hand2):
            print("Player 1 Wins on a Straight Flush!")
            return hand1

        elif not is_straight_flush(hand1):
            print("Player 2 Wins on a Straight Flush!")
            return hand1

        else:
            return tie_breaker(hand1, hand2, "Straight Flush")

    elif is_four_of_a_kind(h1_four) or is_four_of_a_kind(h2_four):
        if not is_four_of_a_kind(get_four_of_a_kind(hand2)):
            print("Player 1 Wins on Four of a Kind!")
            return hand2
        
        elif not is_four_of_a_kind(get_four_of_a_kind(hand1)):
            print("Player 2 Wins on Four of a Kind!")
            return hand2

        else:
           return tie_breaker(hand1, hand2, "Four of a Kind")

    elif is_full_house(hand1) or is_full_house(hand2):
        if not is_full_house(hand2):
            print("Player 1 Wins on a Full House!")
            return hand1

        elif not is_full_house(hand1):
            print("Player 2 Wins on a Full House!")

        else:
            return tie_breaker(hand1, hand2, "Full House")

    elif is_flush(hand1) or is_flush(hand2):
        if not is_flush(hand2):
            print("Player 1 Wins on a Flush!!")
            return hand1
        
        elif not is_flush(hand1):
            print("Player 2 Wins on a Flush!!")
            return hand2

        else:
            return tie_breaker(hand1, hand2, "Flush")

    elif is_straight(hand1) or is_straight(hand2):
        if not is_straight(hand2):
            print("Player 1 Wins on a Straight!")
            return hand1

        elif not is_straight(hand1):
            print("Player 2 Wins on a Straight!")
            return hand2

        else:
            return tie_breaker(hand1, hand2, "Straight")

    elif is_three_of_a_kind(h1_three) or is_three_of_a_kind(h2_three):
        if not is_three_of_a_kind(h2_three):
            print("Player 1 Wins on Three of a Kind!")
            return hand1

        elif not is_three_of_a_kind(h1_three):
            print("Player 2 Wins on Three of a Kind!")
            return hand2

        else:
            return tie_breaker(hand1, hand2, "Three of a Kind")


    elif is_two_pair(h1_two) or is_two_pair(h2_two):
        if not is_two_pair(h2_two):
            print("Player 1 Wins on a Two Pair!")
            return hand1

        elif not is_two_pair(h1_two):
            print("Player 2 Wins on a Two Pair!")
            return hand2

        else:
            return tie_breaker(hand1, hand2, "Two Pair")

    elif is_one_pair(h1_one) or is_one_pair(h1_two):
        if not is_one_pair(h2_one):
            print("Player 1 Wins on a Pair!")
            return hand1

        elif not is_one_pair(h1_one):
            print("Player 2 Wins on a Pair!")
            return hand2

        else:
            return tie_breaker(hand1, hand2, "One Pair")

    else:
        if high_card(hand1) > high_card(hand2):
            print("Player 1 Wins on the High Card!")
        elif high_card(hand2) > high_card(hand1):
            print("Player 2 Wins on the High Card!")
        else:
           return tie_breaker(hand1, hand2, "High Card")

rf = [Card("K", "D"), Card("A", "D"), Card("10", "D"), Card("J", "D"), Card("Q", "D")]
sf = [Card("7", "S"), Card("6", "S"), Card("10", "S"), Card("8", "S"), Card("9", "S")]
four1 = [Card("7", "H"), Card("10", "D"), Card("7", "S"), Card("7", "C"), Card("7", "D")]
straight1 = [Card("8", "H"), Card("6", "C"), Card("10", "D"), Card("7", "S"), Card("9", "H")]
flush1 = [Card("5", "H"), Card("10", "H"), Card("A", "H"), Card("2", "H"), Card("9", "H")]

player_hands = deal(deck, 2, 5)
print_hands(player_hands)

#for card in player_hands[0]:
#    print(type(card))
#    print(card)


#determine_winner(player_hands[0], player_hands[1])   

with open("poker.txt") as f:
    poker_hands = f.readlines()

p1_hands = []
p2_hands = []
for hand in poker_hands:
    p1_hands.append(hand.split(' ',maxsplit=1)[0])
    p2_hands.append(hand.split(' ', maxsplit=1)[1])

for hand in p1_hands:
    print(hand)
