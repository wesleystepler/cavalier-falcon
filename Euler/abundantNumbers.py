#Euler 23

def isAbundant(n): #Checks if n is an abundant number
    abundant = []
    i = 1
    while i <= n/2:
        if n % i == 0:
            abundant.append(i)
        i += 1
    
    if sum(abundant) > n: #A number is abundant when the divisors of number n add up to be > n
        return True
    else:
        return False

test = []
for i in range(12,50):
    if isAbundant(i) == True:
        test.append(i)
print(test)


#These are the two abundant numbers we will add together
n1 = 12
n2 = 12

abundants = []
for i in range(0,100):
    if isAbundant(i) == True:
        abundants.append(i)

#Abundant numbers below 100: [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96]

sums = [] #the list where the sums of adbundant numbers go
i = 0
while i < len(abundants):
    n = 0
    while n < len(abundants):
        print("i =",i," n =",n)
        sums.append(abundants[i] + abundants[n])
        n += 1
    i += 1

print(sums)

#This block of code filters through the list and removes any repeating numbers
test = 0 #the number we're testing for repeats


while test < len(sums):
    foo = 1
    while foo < len(sums):
        if sums[test] == sums[foo]:
            sums.pop(sums[foo])
            foo += 1
        else:
            foo += 1
    test += 1





        

            

