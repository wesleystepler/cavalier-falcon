def variance(): 
    
    #These lists store the x values of the expected and gotten results

    pointsExpect = [20,32.552,45.104,57.656,70.208,82.76,95.312,107.864,120.416,132.968,145.519,158.072,170.624,183.176,195.728,208.28,220.832,233.384,245.936,258.488,271.034,283.592,294.144,308.695,321.248,333.8,346.352,358.904,371.456,384.008,396.56]

    pointsGot = [20,21,21,21,21,22,23,25,26,27,29,31,32,34,36,37,39,41,44,45,47,49,50,52,55,56,57,59,61,62,63]  

    #This loop puts the each difference of x coordinates into a separate list
    i = 0
    difference = []
    while i < len(pointsExpect):
        difference.append(pointsExpect[i]-pointsGot[i])
        i += 1

    #This block squares the differences
    squares = []
    for i in range(0,len(difference)):
        squares.append(difference[i]**2)

    #Yep
    average = float(sum(squares))/float(len(squares))

    print(" Points Expected:",pointsExpect)
    print("Points Got:",pointsGot)
    print("Difference:",difference)
    print("Difference Squared:",squares)

    return average 

print(variance())

    
    