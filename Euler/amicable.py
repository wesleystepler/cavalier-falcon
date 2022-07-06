#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

def d(n):
    divisors = []
    if n % 2 == 0:
        i = n/2
    else:
        i = n - 1
    while i >= 1:
        if n % i == 0:
            divisors.append(i)
            i -= 1
        else:
            i -= 1
    #print(divisors)
    return sum(divisors)

def isAmicable(): #Checks if x and y are amicable numbers
    x = 1
    y = 1
    amicable = []
    while x <= 10000:
        print("Please be Patient...Program is Running...")
        print("X is",x)
        print("Y is",y)
        while y < 10000:
            if d(x) == y and d(y) == x and x != y:
                amicable.append(x)
                amicable.append(y)
                print(amicable)
                y += 1
            else:
                y += 1
        y = 1
        x += 1
    return sum(amicable)
                

print(isAmicable())


