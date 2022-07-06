#I'm confused on how to move forward with this program so I'm starting again with 
#collatz2 to see what I can do
import math
import time
def isEven(n): #This one should be pretty obvious
    if n % 2 == 0:
        return True

def isOdd(n): #This one too
    if isEven(n) == False:
        return True

biggest = [] #Stores the length of each collatz sequence so that the following function can return the max

def collatzSequence(n): #This one runs the collatz sequence on a given number. If the number is even, you divide by two, if it's odd, 
    #Multiply by three and add one. Do this until the number reaches 1
   
    startingNum = n #This is so you can see the starting number for the longest chain
    sequence = [n]
    print("Calculating the sequence for",n)
    while True:
       
        if isEven(n) == True:
            n = n/2
            sequence.append(n)
            
        else:
            n = (n*3)+1
            sequence.append(n)
        if n == 1:
            biggest.append(sequence)
            #print(sequence)
            


            

   
        
for n in range(2,100):
    print(collatzSequence(n))
    
    


            


