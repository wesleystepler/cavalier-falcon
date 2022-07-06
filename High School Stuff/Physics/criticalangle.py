import math
def criticAngle():
    y = range(0,90)
    x = range(0,90)
    if 1.33*math.sin(y) == math.sin(x):
        return y 

print(criticAngle())