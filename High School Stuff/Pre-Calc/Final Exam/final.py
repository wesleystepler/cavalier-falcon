import math

x = 100
i = 1
n = 1
ways = []

while n <= x:
    while i <= x:
        a = n,i
        if n+i == x:
            ways.append(str(a))
        i += 1
    i = 1
    n += 1

print(str(ways))
print(len(ways)/2)
    