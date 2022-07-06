def pentagonal(x): #Prints out the pentagonal sequence to x
    quux = []
    floo = []
    
    n = 0
    while n < x:
        num = (3*(n**2)-n)/2
        otherNum = (3*(n**2)+n)/2
        quux.append(num)
        floo.append(otherNum)
        n += 1

    print(quux)
    print(floo)



print("The Pentagonal Sequence:")
print
print(pentagonal(100))