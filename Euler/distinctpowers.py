import time
import math
a = 2
b = 2

powers = []

while a <= 10: #This loop appends all the powers from 2**2 all the way to 100**100 into the list "powers"
    while b <= 10:
        powers.append(a**b)
        print(powers)
        b += 1
    a += 1
    b = 1

#def noRepeats(list):
#    initialNum = 0 #The number you're checking for a repeat of
#    repeat = 1 #The number you check to see if it's a repition of initialNum
#    while initialNum < len(list):
#        while repeat < len(list):
#            print(list[initialNum],repeat,len(list))
#            if list[initialNum] == list[repeat]:
#                list.pop(list[repeat])
#                repeat += 1
#            else:
#                repeat += 1
#        initialNum += 1
#        repeat = 1
#    return list

#print(noRepeats(powers))
#Current State: The code seems to be running pretty much as it should, until a weird spot when initialNum is 10 and repeat is 200
#Where it gives the error message, "Pop index out of range"




#orderedPowers = []
#i = 0
#for i in range(0,len(powers)):
#    orderedPowers.append(min(powers))
#    powers.pop(min(powers))
#    print(orderedPowers)

#print(orderedPowers)

