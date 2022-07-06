def isPalindrome(x): #Determines if number x is a palindrome
    #These two steps conver the number inputed into a list to determine if it's a palindromic number
    xString = str(x)
    xList = list(xString) 

    if xList[0] + xList[1] + xList [2]  == xList[-1] + xList[-2] + xList[-3]:
        return True
    else:
        return False

#The two three digit numbers to multiply
num1 = 100
num2 = 100

palindromes = [] #The list where we will store palindromic numbers

while num1 <= 999:
    while num2 <= 999:
        currentNum = num1 * num2
        print(num1,num2,currentNum)
        if isPalindrome(currentNum) == True:
            palindromes.append(currentNum)
        num2 += 1
    num2 = 1
    num1 += 1

print(max(palindromes)) #Spits out the answer




                
                
        
        