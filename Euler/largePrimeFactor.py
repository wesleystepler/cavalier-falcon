import library

#def primeFactors(n): #Returns the prime factors of number n

factors = []
primeFactors = []
def factoring(n):
    
    for i in range(2,n):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i)) #Say i is 3. If the number divides evenly by three, then three times a third of the number equals the number
            break

    return factors

print(factoring(10086647))
primes = []

i = 0
while i < len(factors):
    if library.isPrime(factors[i]) == True:
        primeFactors.append(factors[i])
        i += 1
    else:
        factoring(factors[i])
        break

print(factors)


# A visual of what I want to do
#                                  144
#                                  /\
#                                 /  \
#                                /    \
#                              12     12
#                             /  \   /   \
#                            3   4   3    4
#                               2 2      2  2
#
#


