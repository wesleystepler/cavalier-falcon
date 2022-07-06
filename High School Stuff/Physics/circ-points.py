import math


x1 = 0
y1 = 0
x2 = -10.000
y2 = -10.000
while x2 <= 10 and y2 <= 10:
        if math.sqrt((x1-x2)**2 + (y1-y2)**2) <= 10 and math.sqrt((x1-x2)**2 + (y1-y2)**2) >= 9.99:
                print(x2, y2)        
        x2 += 0.001
        y2 += 0.001