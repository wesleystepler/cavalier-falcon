import library
import time
def primeSum(n): #Determines the largest consecutive string of primes that adds to n
    #This block just compiles a list of primes below the number n
    #print("Please wait, code is running...")
    sumList = []
    for i in range(2,n): #This loop checks if a string of primes starting at 2 can = n
        if library.isPrime(i) == True:
            sumList.append(i)
        else:
            next

    print(sumList)

    #This block starts at sumList[a] (Which initially is sumList[1]) and runs through to see if there's any strings of primes
    #that == counter. If it doesn't, then it will start again at sumList[a] at a = 2, then againt at a = 3, etc.
    a = 0
    greatestList = []
    while a < float(len(sumList))/2:
        i = a
        counter = 0
        counterList = []
        while i < float(len(sumList))/2:
            counter += sumList[i]
            if counter == n:
                for x in range(a,i+1): #Start from the ath index, go to the current index (not positive why I need i+1--some sort of syntax thing)
                    counterList.append(sumList[x])
                if len(counterList) > len(greatestList):
                    greatestList = counterList
                    
            elif counter > n:
                break
            else:
                i += 1
        a += 1

    #print(sum(greatestList))
    return greatestList

print(primeSum(1000000))

#greatest = []
#for i in range(0,1000000):
#    if library.isPrime(i) == True:
#        primeSum(i)
#        print("Running prime sum of:",i)
#        if primeSum(i) > greatest:
#            greatest = primeSum(i)
#        else:
#            next

#print(greatest)
    




    

    


    



