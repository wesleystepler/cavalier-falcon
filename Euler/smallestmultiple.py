
import time
def isEven(n): #THis one should be pretty obvious
    if n % 2 == 0:
        return True

i = 2520 #This will ideally eventually be the correct number 
a = list(range(0,20))
index = 19
while index >= 0:
    print(str(i),"...",a[index])
    if i % int(a[index]) == 0:
        index -= 1
    else:
        index = 19
        i += 10
    next

print("That's your answer!")

