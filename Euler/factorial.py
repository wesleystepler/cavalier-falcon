#This program overall is pretty sloppy. Someday I'll come back around to it and make it sleeker
#Euler 20

def factorial(n): #Returns n factorial
    f = 1
    while n > 0:
        print("n =",n)
        f *= n
        n -= 1
    return f
    
print(factorial(100))


#I did this next part manually. I want to figure out how to automate it at some point
#I omitted all the zeroes at the end because that made sense to me

digits = [9,3,3,2,6,2,1,5,4,4,3,9,4,4,1,5,2,6,8,1,6,9,9,2,3,8,8,5,6,2,6,6,7,0,0,4,9,0,7,1,5,9,6,8,2,6,4,3,8,1,6,2,1,4,6,8,5,9,2,9,6,3,8,9,5,2,1,7,5,9,9,9,9,3,2,2,9,9,1,5,6,0,8,9,4,1,4,6,3,9,7,6,1,5,6,5,1,8,2,8,6,2,5,3,6,9,7,9,2,0,8,2,7,2,2,3,7,5,8,2,5,1,1,8,5,2,1,0,9,1,6,8,6,4]
print(sum(digits))