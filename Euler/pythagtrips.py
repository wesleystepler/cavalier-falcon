import math
a = 3
b = 4

while a < 1000:
    while b < 1000:
        c = math.sqrt(a**2 + b**2)
        if a+b+c == 1000:
            print(a,b,c)
        b += 1
    a += 1
    b = a+1
    