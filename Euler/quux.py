import library

def primeSum(n): #Determines the largest consecutive string of primes that adds to n
    #This block just compiles a list of primes below the number n
    #print("Please wait, code is running...")
    sumList = []
    for i in range(2,n): #This loop checks if a string of primes starting at 2 can = n
        print("i =",i)
        if library.isPrime(i) == True:
            sumList.append(i)
        else:
            next

    print(sumList)
    return len(sumList)

print(primeSum(1000000))