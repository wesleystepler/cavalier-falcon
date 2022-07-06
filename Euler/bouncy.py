print("Firing Up...")

def isIncreasing(n): #This funciton checks if the numbers increase going left to right (like 3478)
    floo = str(n) #This is just here because you can't convert an integer to a list--it has to go from string to list
    bounce = list(floo)
    greatest = bounce[0] 
    i = 1

    while i <= len(bounce)-1:
        if int(bounce[i]) >= int(greatest):
            greatest = bounce[i]
            if i == len(bounce)-1:
                return True
            i += 1
        else:
            return False
            


def isDecreasing(n): #This function checks if the number decreases from left to right (like 86321)
    floo = str(n) #This is just here because you can't convert an integer to a list--it has to go from string to list
    bounce = list(floo)
    smallest = bounce[0] 
    i = 1
    while i <= len(bounce)-1:
        if int(bounce[i]) <= int(smallest):
            smallest = bounce[i]
            if i == len(bounce)-1:
                return True
            i += 1
        else:
            return False
    
#If a number is neither increasing or decreasing, it's bouncy
def isBouncy(n): #Looks to see if a number in the range of x to n has the given percent of bouncy numbers
    bouncyBois = []
    if isIncreasing(n) == False and isDecreasing(n) == False:
        bouncyBois.append(n)
        return (bouncyBois)
    else:
        return False
    
def percentBouncy(x,p): #Checks if n percent of numbers up to a given number are bouncy. 
    bounceList = []  
    nonBounceList = [] 
    for n in range(1,x):
        if type(isBouncy(n)) != bool:
            bounceList.append(isBouncy(n))
            print(len(bounceList))

        else:
            nonBounceList.append(isBouncy(n))


        percent = float(len(bounceList))/float(n)
        if percent == p:
            return len(bounceList),n


print(percentBouncy(10000000000,0.99))



    


      







