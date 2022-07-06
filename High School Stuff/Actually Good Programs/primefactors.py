def isPrime(n):
    i = 2
    for i in range(2,n):
        if n % i == 0:
            return "Not Prime"
        else:
            i += 1
       
           

#def primeList(n):
    #primes = [] 
    #for n in range(2,n):
    #    if isPrime(n) == None:               
#            primes.append(n)
 #           print(len(primes))
  #  return primes[10000]
    

def primeSum():
    primesum = []
    for n in range(1,2000000):
        if isPrime(n) == None:
            print(n)
            primesum.append(n)

    print(sum(primesum))
    
            

primeSum()




