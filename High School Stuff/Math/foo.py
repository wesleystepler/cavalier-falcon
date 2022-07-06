import library
def primeSum(n): #Determines the largest consecutive string of primes that adds to n
    #This block just compiles a list of primes below the number n
    #print("Please wait, code is running...")
    sumList = []
    for i in range(2,n): #This loop checks if a string of primes starting at 2 can = n
        if library.isPrime(i) == True:
            sumList.append(i)
        else:
            next

    return sumList

print(primeSum(1000000))