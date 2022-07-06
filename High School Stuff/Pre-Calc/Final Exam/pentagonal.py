#Pentagonal Sequence when you use -n: 0,1,5,12,22,35,51,70,92,117
#Pentagonal Sequence When you Use +n: 0,2,7,15,26,40,57,77,100,126
#Combined Pentagonal Sequence: 0,1,2,5,7,12,15,22,26,35,40,51,57
#Summation Sequence: 1,2,4,6,9,13,19,26

def pentagonal(x): #Prints out the pentagonal sequence to x
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
    #return combined

    def partition(n):
        counter = 1
        totalSum = 0
        i = 0
        x = True
        #if n < 0 :
         #   return 0
        #if n == 0:
         #   return 0
            
        while i <= n:
            if x == True and i <= n:
                totalSum += partition(n-combined[i])
                print(totalSum)
                counter += 1
                if counter == 2:
                    x = False
                    counter = 0
                    i += 1
                else:
                    i += 1

            if x == False and i <= n:
                totalSum -= partition(n-combined[i])
                print(totalSum)
                counter += 1
                if counter == 2:
                    x = True
                    counter = 0
                    i += 1
                else: 
                    i += 1
        return totalSum
        
    return partition(100)




    
answer = pentagonal(100)

def pentagonalIndividual(n): #Returns the nth pentagonal number
    return answer[n]

#print(pentagonalIndividual(98))


def partition(n,i):
    if n < 0:
        return 0

    if n == 0:
        return 1

    i += 1
    return partition(n) + partition(n-answer[i])  

#print(partition(10,1))  

print(pentagonal(99))









