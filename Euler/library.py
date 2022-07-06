import math
import time
import random
#Functions:

#Math
def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        else:
            i += 1
            
    return True


def pythagTheorem(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

def distance(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2) + ((y1 - y2)**2))

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
        
def reverse(n): #Returns the reverse of n (105 --> 501)
        nRev = int(str(n)[::-1])
        return nRev









def better_movies(movie_name, first):
    whats_better = " "
    for i in range(0,len(first)):
        print("Current list:",first[i])
        for i in range(0,len(first[i])):
            print("Current ELement in list",first[i][i])
            if movie_name in first[i][i]:
                whats_better += movie_name
    return whats_better


#Chemistry

def formalCharge

    
#Classes
class quotes: #You can use this class to output a quote from someone
    def poe():
        return "Quoth the Raven, nevermore"
    
    def tolkien():
        return "In a hole in the ground, there lived a Hobbit"

    def lewis():
        return "I'll read some more C.S. Lewis and get back to you"
    
    def remarque(): 
        return "This book is neither to be an accusation nor a confession, and least of all and adventure, for death is not an adventure for those who stand face to face with it."

    def mathwin():
        return "Now that's a spicy meatball!"

    def mrMrCarey():
        return "What do you do, when you see a BARE ABLATIVE. You put a WITH in front of it"

    def joseph():
        return "Gang gang, brotha"
    
    def dickens():
        return "It was the best of times, it was the worst of times"

class coins: 
 #British Currency
    def onePence():
        return 1

    def twoPence():
        return 2

    def fivePence():
        return 5

    def tenPence():
        return 10

    def twentyPence():
        return 20

    def fiftyPence():
        return 50

    def pound():
        return 100

    def twoPound():
        return 200

 #American Currency
    def penny():
        return 1
    
    def nickel():
        return 5

    def dime():
        return 10

    def quarter():
        return 25

    def dollarBill():
        return 100


    