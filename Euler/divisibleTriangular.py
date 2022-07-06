def triangleNumbers(n): #Prints out all the triangular numbers up to the nth one
    triangleList = [] #The list that will store the triangular numbers
    currentNum = 1
    for i in range(1,n):
        triangleList.append(currentNum)
        currentNum += currentNum + 1
    return triangleList


print(triangleNumbers(10))

#This probably needs to be done with a recursive function