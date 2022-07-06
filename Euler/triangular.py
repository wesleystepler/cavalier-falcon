#Project Euler Problem #12

triNums = []  # an array to store past triangular numbers, to make finding factors easier 
def triangular(n):  # Returns the nth triangular number
    tri_num = 0
    for i in range(1,n+1):
        tri_num += i
    return tri_num


def factors(n):  # Returns the factors of a given number n
    divisorList = [] # Use this if you want an actual list of divisors, not just the total
    if n == 1:
        divisors = 1
        return divisors

    elif n == 2:
        divisors = 2
        return divisors
    else:
        divisors = 2

    divisors += factors(n-1)
    #for i in range(2, n-1):
    #    if n % i == 0:
    #        # divisors.append(i)
    #        divisors += 1
    return divisors

print(factors(28))


solved = False
i = 0

"""while solved != True:
    print("Checking for triangular number #" + str(i))
    if factors(triangular(i)) > 500:
        print(triangular(i))
        break
    else:
        i += 1
        next"""



    



