import math
import time
def pandigital(): #Spits out the pandigital of a number n
    number = [] #The list that will store
    allTheLists = [] #This is where the number list will go when it's done
    n = 2 #The integer you're getting the pandigital of
    while n <= 1000000:
        for i in range(1,100000):
            if len(list(str(n*i))) <= 9:
                number.append(n*i)
                print(number)
                time.sleep(0.5)
            if len(number) >= 9:
                allTheLists.append(number)
                number = []
                n += 1
print(pandigital())