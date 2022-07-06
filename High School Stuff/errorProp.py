import math
def errorMultiply(x,xE,y,yE): #Determines the error of x and y, when x and y are multiplied together.
    f = x*y
    fError = math.sqrt((xE/x)**2+(yE/y)**2)*f
    print(f)
    return fError

def errorAdd(x,xE,y,yE):
    f = x + y
    fError = math.sqrt(xE**2+yE**2)
    print(f)
    return fError

def errorSubtract(x,xE,y,yE):
        f = x - y
        fError = math.sqrt(xE**2+yE**2)
        print(f)
        return fError

def errorDivide(x,xE,y,yE):
    f = x/y
    fError = math.sqrt((xE/x)**2+(yE/y)**2)*f
    print(f)
    return fError

#print(errorMultiply(39.2439,0.18477,7.76,0.02))
#print(errorSubtract(3.4401,0.0036,0.98,0.05))
#print(errorAdd(157.7,0.5,285.6,0.5))
print(errorDivide(4344.34,0.7,4343,0.7))
print()
# 443.3 +- 0.7