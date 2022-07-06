def test(n): #This function was practice for getting the + + - - pattern for partitions, but it did not do what I hoped.
    x = True
    variable = 0
    
    counter = 1
    i = 1
    while i <= n:
        if x == True:
            variable += i
            print(variable)
            counter += 1
            if counter == 2:
                counter = 0
                x = False

        if x == False:
            variable -= i
            print(variable)
            counter += 1
            if counter == 2:
                counter = 0
                x = True

        i += 1
    return variable
        
     
        
        

    return variable
            

def test2(n): #Second try...
    counter = 0
    variable = 0
    x = True
    i = 1
    while i <= n:
        if x == True and i <= n:
            variable += i
            #print(variable)
            counter += 1
            if counter == 2:
                x = False
                counter = 0
                i += 1
            
            else:
                i += 1
                
        if x == False and i <= n:
            variable -= i
            #print(variable)
            counter += 1
            if counter == 2:
                x = True
                counter = 0
                i += 1
                
            else: 
                i += 1
                
                
    return variable


#print(test2(4760))

def pentagonal(x): #Copy-Pasta'd this function here to use for test3, as well as the answer variable
    quux = []
    floo = []
    
    for n in range(1,x):
        num = (3*(n**2)-n)/2
        otherNum = (3*(n**2)+n)/2
        quux.append(num)
        floo.append(otherNum)

    combined = []
    for i in range(0,len(quux)):
        combined.append(quux[i])
        combined.append(floo[i])
    return combined
    
answer = pentagonal(100)

def test3(n): #Attempting to incorporate the + + - - code into the (n-1) + (n-2) - (n-5) - (n-7) pattern
    counter = 1
    totalSum = 0
    i = 0
    x = True
    while i <= n:
        if x == True and i <= n:
            totalSum += (n-answer[i])
            print(totalSum)
            counter += 1
            if counter == 2:
                x = False
                counter = 0
                i += 1
            else:
                i += 1

        if x == False and i <= n:
            totalSum -= (n-answer[i])
            print(totalSum)
            counter += 1
            if counter == 2:
                x = True
                counter = 0
                i += 1
            else: i += 1

    return totalSum

#print(test3(10))
#print(test2(10))

print(answer)
        





