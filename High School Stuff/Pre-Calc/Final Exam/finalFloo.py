import math

x = 100
k = 1
i = 1
n = 1
ways = []

while k <= x:   
    while n <= x:
        while i <= x:
            a = n,i,k
            if n+i+k == x:
                ways.append(str(a))
            i += 1
        i = 1
        n += 1
    k += 1

print(str(ways))
print(len(ways)/2)