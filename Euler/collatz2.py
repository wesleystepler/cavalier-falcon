import math
import time

#This one works, it just takes FOREVER to get to 1000000
#Just kidding, it thinks whatever the last sequence run is always the biggest
#That was because when you use max() on two lists, it goes on the sum of all the indeces, not the length

sequences = [] #Will store all the sequences so I can pull the biggest one
startNum = [] #Stores how long each sequence is and the initial number n
def collatzSequence(n): #Runs the collatz sequence for number n
    sequence = [n]
    print("Calculating the Sequence for",n)
    while True:
        if n % 2 == 0:
            n = n/2
            sequence.append(n)
        else:
            n = (n*3)+1
            sequence.append(n)

        if n == 1:
            sequences.append(sequence)
            startNum.append( (len(sequence), sequence[0]) )
            return sequence

            
for i in range(1,500001): #For some reason the range has to go to 1 above the number you want
    collatzSequence(i)

print("The longest collatz sequence is...")
print()
print(max(startNum),"!")

#Longest from 1-500,000: 449, starting at 410,011
#Longest from 500,000-1,000,000: (525, 837799)

#It seems like in a list of tuples, using the max function
#determines the largest of the first numbers in the tuple. So in
#(3,500) and (50,23), (50,23) would be the max. So, if you order the tuples so that the
#length of the sequence is first and the starting number second, you can get the program to tell you what 
#starting number yields the greatest collatz sequence.


    

    

