import math
def blah(v,m):
    g = 6.67*(10**-11)
    r = (2*g*m)/v**2
    return r

print(blah(300000000,5.97*(10**24)))

