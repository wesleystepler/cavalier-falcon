from card import Card
from deck import Deck
from poker_chips import Chip
import poker_hands
import subprocess
import time

# *******************GLOBAL VARIABLES**********************
POT = []
POT_TOTAL = 0

P1_HAND = []
P1_CHIPS = []
P1_TOTAL = 0
P1_W = 0
P1_R = 0
P1_B = 0

P2_HAND = []
P2_CHIPS = []
P2_TOTAL = 0
P2_W = 0
P2_R = 0
P2_B = 0

W = Chip("W")
R = Chip("R")
B = Chip("B")

# ************************************GAMEPLAY FUNCTIONS**********************************

def default_chips():
    """Set default Chip values for Player 1 and Player 2"""
    global P1_CHIPS
    global P1_TOTAL
    global P1_W
    global P1_R
    global P1_B
    global P2_CHIPS
    global P2_TOTAL
    global P2_W
    global P2_R
    global P2_B

    chips = []
    for i in range(0, 20):
        P1_CHIPS.append(W)
        P1_W += 1
        P1_TOTAL += W.value

        P2_CHIPS.append(W)
        P2_W += 1
        P2_TOTAL += W.value


    for i in range(0, 15):
        P1_CHIPS.append(R)
        P1_R += 1
        P1_TOTAL += R.value

        P2_CHIPS.append(R)
        P2_R += 1
        P2_TOTAL += R.value

    for i in range(0, 10):
        P1_CHIPS.append(B)
        P1_B += 1
        P1_TOTAL += B.value

        P2_CHIPS.append(B)
        P2_B += 1
        P2_TOTAL += B.value

    # In timeout til I figure out what's wrong with this one
    #for i in range(0, 4):
    #    chips.append(Chip("G"))


def update_chip_total(player):
    global P1_CHIPS
    global P1_TOTAL
    global P1_W
    global P1_R
    global P1_B
    global P2_CHIPS
    global P2_TOTAL
    global P2_W
    global P2_R
    global P2_B

    if player == "Player 1":
        P1_TOTAL = 0
        P1_W = 0
        P1_R = 0
        P1_B = 0
        for chip in P1_CHIPS:
            P1_TOTAL += chip.value
            if chip.color == "W":
                P1_W += 1
            elif chip.color == "R":
                P1_R += 1
            elif chip.color == "B":
                P1_B += 1

    elif player == "Player 2":
        P2_TOTAL = 0
        P2_W = 0
        P2_R = 0
        P2_B = 0
        for chip in P2_CHIPS:
            P2_TOTAL += chip.value
            if chip.color == "W":
                P2_W += 1
            elif chip.color == "R":
                P2_R += 1
            elif chip.color == "B":
                P2_B += 1

    else:
        raise Exception("Invalid Player Entry")
   
def print_chip_total(player):
    """Not sure if I'm gonna use this or not. May be replaced with print_screen()"""
    global P1_TOTAL
    global P1_W
    global P1_R
    global P1_B
    global P2_TOTAL
    global P2_W
    global P2_R
    global P2_B

    if player == "Player 1":
        print(f"{player} Total Chips: ${P1_TOTAL}")
        print(f"White Chips: {P1_W}")
        print(f"Red Chips: {P1_R}")
        print(f"Blue Chips: {P1_B}")

    elif player == "Player 2":
        print(f"{player} Total Chips: ${P2_TOTAL}")
        print(f"White Chips: {P2_W}")
        print(f"Red Chips: {P2_R}")
        print(f"Blue Chips: {P2_B}")  
 

def bet(player, num_w, num_r, num_b):
    global P1_CHIPS
    global P2_CHIPS
    global POT
    global POT_TOTAL

    if player == "Player 1":
        for i in range(0, num_w):
            P1_CHIPS.remove(W)
            POT.append(W)
            POT_TOTAL += W.value
        
        for i in range(0, num_r):
            P1_CHIPS.remove(R)
            POT.append(R)
            POT_TOTAL += R.value
        
        for i in range(0, num_b):
            P1_CHIPS.remove(B)
            POT.append(B)
            POT_TOTAL += B.value

        update_chip_total(player)

    elif player == "Player 2":
        for i in range(0, num_w):
            P2_CHIPS.remove(W)
            POT.append(W)
            POT_TOTAL += W.value
        
        for i in range(0, num_r):
            P2_CHIPS.remove(R)
            POT.append(R)
            POT_TOTAL += R.value
        
        for i in range(0, num_b):
            P2_CHIPS.remove(B)
            POT.append(B)
            POT_TOTAL += B.value

        update_chip_total(player)

def reset_pot():
    global POT
    global POT_TOTAL

    POT.clear()
    POT_TOTAL = 0

def player_turn(player):
    if player == "Player 1":
        print("Player 1, it's your turn!")
        print("Press 'B' to bet, or 'C' to check: ")
        while True:
            turn = input()
            if turn == "B":
                print("Player 1 chose to bet!")
                print("Please choose how many chips you'd like to bet: ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                while True:
                    print("White Chips: ")
                    num_w = input()
                    if not num_w.isdigit():
                        print("Enter a number!")
                    elif P1_W - int(num_w) < 0:
                        print("You don't enough chips to make that bet!")
                    else:
                        print(f"Player 1 is betting {num_w} White Chips!")
                        break

                while True:
                    print("Red Chips: ")
                    num_r = input()
                    if not num_r.isdigit():
                        print("Enter a number!")
                    elif P1_R - int(num_r) < 0:
                        print("You don't have enough chips to make that bet!")
                    else:
                        print(f"Player 1 is betting {num_r} Red Chips!")
                        break
                
                while True: 
                    print("Blue Chips: ")
                    num_b = input()
                    if not num_b.isdigit():
                        print("Enter a number!")
                    elif P1_B - int(num_b) < 0:
                        print("You don't have enough chips to make that bet!")
                    else:
                        print(f"Player 1 is betting {num_b} Blue Chips!")
                        print()
                        break
                bet(player, int(num_w), int(num_r), int(num_b))
                break

            elif turn == "C":
                print()
                print("Player 1 chose to check!")
                print()
                break

            else:
                print("Invalid Response! Please try again.")
                print("Valid responses: 'B' to bet, or 'C' to check")
        print_screen()


    else:
        
        print("Player 2, it's your turn!")
        print("Press 'B' to bet, or 'C' to check: ")
        while True:
            turn = input()
            if turn == "B":
                print("Player 2 chose to bet!")
                print("Please choose how many chips you'd like to bet: ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                while True:
                    print("White Chips: ")
                    num_w = input()
                    if not num_w.isdigit():
                        print("Enter a number!")
                    elif P2_W - int(num_w) < 0:
                        print("You don't enough chips to make that bet!")
                    else:
                        print(f"Player 2 is betting {num_w} White Chips!")
                        break
               
                while True:
                    print("Red Chips: ")
                    num_r = input()
                    if not num_r.isdigit():
                        print("Enter a number!")
                    elif P2_R - int(num_r) < 0:
                        print("You don't have enough chips to make that bet!")
                    else:
                        print(f"Player 2 is betting {num_r} Red Chips!")
                        break
                
                while True: 
                    print("Blue Chips: ")
                    num_b = input()
                    if not num_b.isdigit():
                        print("Enter a number!")
                    elif P2_B - int(num_b) < 0:
                        print("You don't have enough chips to make that bet!")
                    else:
                        print(f"Player 2 is betting {num_b} Blue Chips!")
                        print()
                        break
                bet(player, int(num_w), int(num_r), int(num_b))
                break

            elif turn == "C":
                print()
                print("Player 2 chose to check!")
                print()
                break

            else:
                print("Invalid Response! Please try again.")
                print("Valid responses: 'B' to bet, or 'C' to check")
        print_screen()

    

def hand_winner(player):
    global POT
    global P1_CHIPS
    global P1_TOTAL
    global P2_CHIPS
    global P2_TOTAL

    print(f"Pot won: {POT}")

    if player == "Player 1":
        for chip in POT:
            P1_CHIPS.append(chip)
            
        print(f"{player} Wins the Hand!")
        update_chip_total(player)

    elif player == "Player 2":
        for chip in POT:
            P2_CHIPS.append(chip)
        
        print(f"{player} Wins the Hand!")
        update_chip_total(player)
    reset_pot()
    print_screen()
            
def print_screen():
    # Displays the game until I can get pygame working with this
    global POT
    global P1_HAND
    global P1_CHIPS
    global P1_TOTAL
    global P1_W
    global P1_R
    global P1_B

    global P2_HAND
    global P2_CHIPS
    global P2_TOTAL
    global P2_W
    global P2_R
    global P2_B
    print()
    print()
    print("***************************************************************************************************************")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(f"Player 1 Total Chips: ${P1_TOTAL}")
    print(f"White Chips: {P1_W}")
    print(f"Red Chips: {P1_R}")
    print(f"Blue Chips: {P1_B}")
    print()
    print(f"Player 2 Total Chips: ${P2_TOTAL}")
    print(f"White Chips: {P2_W}")
    print(f"Red Chips: {P2_R}")
    print(f"Blue Chips: {P2_B}")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print(f"**********                            The Pot:   {POT}")
    print(f"**********                            Worth: ${POT_TOTAL}")
    print()
    print()
    print(f"Player 1 Hand: {P1_HAND} ")
    print()                                     
    print(f"Player 2 Hand: {P2_HAND}")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("****************************************************************************************************************")
    print()
    print()

 
#********************************************PLAY THE GAME************************************************

def play():
    global P1_HAND
    global P1_CHIPS
    global P1_TOTAL
    global P1_W
    global P1_R
    global P1_B
    global P2_HAND
    global P2_CHIPS
    global P2_TOTAL
    global P2_W
    global P2_R
    global P2_B
    print()
    print("******************************Welcome to Poker! Let's Play!******************************")
    print()
    default_chips()
    deck = Deck()
    deck.shuffle()
    hands = deck.deal(2, 5)
    P1_HAND = hands[0]
    P2_HAND = hands[1]
    print_screen()

    round = 1
    if round % 2 != 0:
        print("First Round of Betting!")
        player_turn("Player 1")
        player_turn("Player 2")
        print("Second Round of Betting!")
        player_turn("Player 1")
        player_turn("Player 2")

        print("The round is over! Let's see who won...")
        time.sleep(3)
        print(f"Player 1 had: {hands[0]}")
        print(f"Player 2 had: {hands[1]}")
        time.sleep(1)
        winner = poker_hands.determine_winner(P1_HAND, P2_HAND)
        time.sleep(3)
        hand_winner(winner) 
        print_chip_total("Player 1")
        print_chip_total("Player 2")

play()
