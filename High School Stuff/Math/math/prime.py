def isPrime(x):
    i = 2
    while i < x:
        if x % i == 0:
            print "Not Prime"
        i += 1

print(isPrime(4))