import math
Ke = 8.99 * (10**9)
moo = 10**-6
n = 10**-9

def elecCharge(q1,q2,d):
    return Ke * (q1*q2/d**2)

def distForm(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#print( distForm(3,6,7.07,-7.07) )
#Remove comment when Distance Formula is needed again

print(elecCharge(1,0.2,14.31))

def vecForm(h,a): #A Function that takes as its input a length and an angle measurement
    return math.sin(math.radians(a)) * h,
    return math.cosin(math.radians(a)) * h, 
    return h
print vecForm(h,a)
    