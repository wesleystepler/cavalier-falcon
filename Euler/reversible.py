#This is for Project Euler Problem #145
import math
import library
#Because of how the function works, the input number needs to have 
def reverse(n): #Returns the reverse of n (105 --> 501)
        nRev = int(str(n)[::-1])
        return nRev

reversibleNum = [] #The list that will keep the reversible numbers
n = 1
while n <= 1000:
    print("n =",n)
    x = str(n+reverse(n))

    i = 0
    while i <= len(x):
        if library.isEven(int(x[i])) == False:
          i = i #I just needed to put something here. I'm rusty on programming, don't judge me  
        else:
            break
        if i == len(x):
            reversibleNum.append(int(x))
    n += 1

print(reversibleNum)