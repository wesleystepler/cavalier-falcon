from card import Card
from deck import Deck
from poker_chips import Chip

# *******************GLOBAL VARIABLES**********************
POT = []

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
    global P2_CHIPS
    chips = []
    for i in range(0, 20):
        P1_CHIPS.append(W)
        P2_CHIPS.append(W)

    for i in range(0, 15):
        P1_CHIPS.append(R)
        P2_CHIPS.append(R)

    for i in range(0, 10):
        P1_CHIPS.append(B)
        P2_CHIPS.append(B)

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

    if player == "Player 1":
        for i in range(0, num_w):
            P1_CHIPS.remove(W)
            POT.append(W)
        
        for i in range(0, num_r):
            P1_CHIPS.remove(R)
            POT.append(R)
        
        for i in range(0, num_b):
            P1_CHIPS.remove(B)
            POT.append(B)
        update_chip_total(player)

    elif player == "Player 2":
        for i in range(0, num_w):
            P2_CHIPS.remove(W)
            POT.append(W)
        
        for i in range(0, num_r):
            P2_CHIPS.remove(R)
            POT.append(R)
        
        for i in range(0, num_b):
            P2_CHIPS.remove(B)
            POT.append(B)
        update_chip_total(player)

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
            POT.remove(chip)
        print(f"{player} Wins the Hand!")
        update_chip_total(player)

    elif player == "Player 2":
        for chip in POT:
            P2_CHIPS.append(chip)
            POT.remove(chip)
        print(f"{player} Wins the Hand!")
        update_chip_total(player)
            
  
#********************************************PLAY THE GAME************************************************

default_chips()
update_chip_total("Player 1")
update_chip_total("Player 2")

print("Pre-Bet: ")
print_chip_total("Player 1")
print()
print_chip_total("Player 2")
print()

bet("Player 1", 5, 2, 1)
print()
hand_winner("Player 1")
print("Post-Bet: ")
print_chip_total("Player 1")
print()
print_chip_total("Player 2")
print(f"Pot: {POT}")









