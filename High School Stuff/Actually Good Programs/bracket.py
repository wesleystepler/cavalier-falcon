def tokenizeTeam(team):
    tokens = team.strip().split(",")
    return {
        "Name": tokens[1],
        "Seed": tokens[0],
        "Wins": tokens[2],
        "Losses": tokens[3]
    }

#This function determines the winner of a given match 