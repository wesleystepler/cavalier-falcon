def factorial(x):
    num = 1
    for i in range(2,x+1):
        num *= i
    return num

y = (factorial(25)/(factorial(24))
