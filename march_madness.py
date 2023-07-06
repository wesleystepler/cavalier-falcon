import random
import time

###   WINNING PERCENTAGE DATA WE WILL USE FOR THE WEIGHTED TOURNAMENT SIMULATION   ###

probs_64 = {1: 0.9921875, 2: 0.9453125, 3: 0.859375, 4: 0.78125, 5: 0.65625, 6: 0.6328, 7: 0.5859, 8: 0.4453, 9: 0.5546875, 10: 0.40625,
            11: 0.3671875, 12: 0.34375, 13: 0.21875, 14: 0.140625, 15: 0.0546875, 16: 0.0078125}

probs_32 = {1: 0.874251497005988, 2: 0.6962025316455697, 3: 0.636986301369863, 4: 0.78125, 5: 0.5304347826086957, 6: 0.4774774774774775, 
            7: 0.38181818181818183, 8: 0.24390243902439024, 9: 0.125, 10: 0.38461538461538464, 11: 0.4675324675324675, 12: 0.4246575342465753, 
            13: 0.1836734693877551, 14: 0.13636363636363635, 15: 0.2, 16: 0.1}

probs_16 = {1: 101/126, 2: 110/158, 3: 37/77, 4: 22/70, 5: 10/50, 6: 15/35, 7: 3/10, 8: 9/15, 9: 4/7, 10: 9/24, 11: 9/26, 12: 2/22, 
            13: 0.01, 14: 0.01, 15: 1/3, 16: 0.1}

probs_8 = {1: 60/101, 2: 32/67, 3: 17/37, 4: 13/22, 5: 7/10, 6: 3/15, 7: 3/10, 8: 6/9, 
            9: 1/4, 10: 1/9, 11: 5/9, 12: 0.01, 13: 0.1, 14: 0.1, 15: 0.1, 16: 0.1}

probs_4 = {1: 37/60, 2: 13/32, 3: 11/17, 4: 3/13, 5: 3/7, 6: 1/3, 7: 1/3, 8: 4/6, 9: 0.1, 
            10: 0.1, 11: 0.1, 12: 0.1, 13: 0.1, 14: 0.1, 15: 0.1, 16: 0.1}

probs_2 = {1: 24/37, 2: 5/13, 3: 4/11, 4: 1/3, 5: 0.1, 6: 1/2, 7: 0.5, 8: 1/4, 9: 0.1, 
            10: 0.1, 11: 0.1, 12: 0.1, 13: 0.1, 14: 0.1, 15: 0.1, 16: 0.1}

weights = [probs_64, probs_32, probs_16, probs_8, probs_4, probs_2]



###   METHODS WE WILL USE IN OUR SIMULATION   ###
def determine_winner_random(game): 
    # Purely random option
    team1 = game[0]
    team2 = game[1]
    winner = random.choice(game)
    return winner


def determine_winner_weighted(game, round, weights):
    # Weighted option

    # Get the team's seeds and extract them as their own int values
    team1_seed = [int(i) for i in game[0].split() if i.isdigit()]
    team2_seed = [int(i) for i in game[1].split() if i.isdigit()]
    t1_seed = ""
    t2_seed = ""
    for i in team1_seed:
        t1_seed += str(i)
    t1_seed = int(t1_seed)

    for i in team2_seed:
        t2_seed += str(i)
    t2_seed = int(t2_seed)

    if round == first_round:
        prob = (weights[0][t1_seed], weights[0][t2_seed])
    elif round == second_round:
        prob = (weights[1][t1_seed], weights[1][t2_seed])
    elif round == sweet_sixteen:
        prob = (weights[2][t1_seed], weights[2][t2_seed])
    elif round == elite_eight:
        prob = (weights[3][t1_seed], weights[3][t2_seed])
    elif round == final_four:
        prob = (weights[4][t1_seed], weights[4][t2_seed])
    else:
        prob = (weights[5][t1_seed], weights[5][t2_seed])

    result = random.choices(game, prob, k = 1)
    return result[0]


def initialize_round(round, winners=None):
    if round == first_round:
        with open("input2.txt") as f:
            lines = f.readlines()
        teams = []
        for line in lines:
            teams.append(line.replace("\n", ""))

        i = 0
        while i < int(len(teams)):
            game = [teams[i], teams[i+1]]
            round.append(game)
            i += 2
        return round

    else:
        i = 0
        while i < len(winners):
            game = [winners[i], winners[i+1]]
            round.append(game)
            i += 2
        return round


def get_round(round):
    if round == first_four:
        cur_round = "The First Four"
    elif round == first_round:
        cur_round = "The Round of 64"
    elif round == second_round:
        cur_round = "The Round of 32"
    elif round == sweet_sixteen:
        cur_round = "The Sweet Sixteen"
    elif round == elite_eight:
        cur_round = "The Elite Eight"
    elif round == final_four:
        cur_round = "The Final Four"
    else:
        cur_round = "The National Championship"
    return cur_round


def get_winners(round, weights):
    print()
    print(f"Determining winners of {get_round(round)}")
    winners = []
    for i in range(0, len(round)):
        winners.append(determine_winner_weighted(round[i], round, weights))
    time.sleep(1.5)
    dummy = input("Done! Press Any Key to Continue")
    print()
    return winners


def display_round(round):
    offset = int(len(round)/2)
    matchups = []
    print()
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{get_round(round)}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(0, int(len(round)/2)):
        col1 = f"{round[i][0]} vs. {round[i][1]}"
        col2 = f"{round[i+offset][0]} vs. {round[i+offset][1]}"
        matchups.append(col1)
        matchups.append(col2)

    # Loop over the matchups and format them
    for i in range(0, len(matchups), 2):
        phrase1 = matchups[i]
        phrase2 = matchups[i+1] if i+1 < len(matchups) else ""
        formatted_string = "{:<{width}}{}".format(phrase1, phrase2, width=75)
        print(formatted_string)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()



###   SIMULATE THE NCAA TOURNAMENT   ###


print("Hello friends, and welcome to March Madness!!")
# Uncomment this to manually add the first four
# print("To start, enter in the teams competing in the First Four")
time.sleep(1)
first_four = []
first_round = []
second_round = []
sweet_sixteen = []
elite_eight = []
final_four = []
championship = []

# First Four
"""print()
regions = ["South", "East", "Midwest", "West"]
for i in regions:
    print(f"Enter First Four Matchup for the {i} Region:")
    time.sleep(0.5)
    team1 = input("Enter higher seeded team: ")
    team2 = input("Enter lower seeded team: ")
    game = [team1, team2]
    first_four.append(game)
    print()
print()

ff_wins = get_winners(first_four, weights)
print("Winners of the First Four:")
for team in ff_wins:
    print(team)"""

print("The Field of 64 is set! Here we go!")
time.sleep(1.5
)
print()
print()

# Initialize Round of 64
initialize_round(first_round)
display_round(first_round)


# Set Round of 32
initialize_round(second_round, get_winners(first_round, weights))
display_round(second_round)


# Set Sweet Sixteen
initialize_round(sweet_sixteen, get_winners(second_round, weights))
display_round(sweet_sixteen)

# Set Elite Eight
initialize_round(elite_eight, get_winners(sweet_sixteen, weights))
display_round(elite_eight)

# Set Final Four 
initialize_round(final_four, get_winners(elite_eight, weights))
display_round(final_four)

# Determine Champion
initialize_round(championship, get_winners(final_four, weights))
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~The National Championship~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"                                                   {championship[0][0]} vs. {championship[0][1]}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
champ = get_winners(championship, weights)

print("~~~~~~~~~~NATIONAL CHAMPION~~~~~~~~~~")
print(f"            {champ[0]}                            ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
