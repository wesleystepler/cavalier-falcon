one_pence = 1
two_pence = 2
five_pence = 5
ten_pence = 10
twenty_pence = 20
fifty_pence = 50
E1 = 100

limit = 200
current_total = 0

"""
Bottom up approach: 
Start with 200 one pences. Then, 198 one pences and one two pence, then 196 one pences and 2 two pences...

100, 100
100, 50, 50
100, 50, 20, 20, 10
100, 50, 20, 20, 5, 5
100, 50, 20, 20, 5, 2, 2, 1
100, 50, 20, 20, 5, 2, 1, 1, 1
100, 50, 20, 20, 5, 1, 1, 1, 1, 1
100, 50, 20, 20, 2, 2, 1, 1, 1, 1, 1, 1
100, 50, 20, 20, 2, 1, 1, 1, 1, 1, 1, 1, 1
100, 50, 20, 20, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 


"""

vals = [E1, fifty_pence, twenty_pence, ten_pence, five_pence, two_pence, one_pence]

answers = []
i = 0

finished = False
while not finished:
    coin_list = []
    while current_total <= limit:
        if current_total == limit:
            break
        #print(f"{current_total} + {vals[i]} = {current_total + vals[i]}")
        if current_total + vals[i] > limit:
            i += 1
        else:
            # Create a temporary list and then append the coin value to it. If it's already in the answers, 
            # Keep going with smaller values 
            temp = coin_list.copy()
            temp.append(vals[i])
            if temp not in answers:
                current_total += vals[i]
                coin_list.append(vals[i])
            else:
                i += 1


    # Reset current_total so the inner loop can execute again
    current_total = 0
    print(coin_list)
    answers.append(coin_list)
    if coin_list == [1]*200:
        answers.append(coin_list)
        finished = True
    else:
        continue

    """if coin_list in answers:
       # If you already have this configuration, then you want to take the largest value and break it into its smaller
       # components. E.g., if the max value in the coin list was 100, you'd want to shift the i value over one to 50
       i = vals.index(max(coin_list)) + 1
       coin_list.remove(coin_list[-1])
    else:
        answers.append(coin_list)"""
    
print(len(answers))
    

