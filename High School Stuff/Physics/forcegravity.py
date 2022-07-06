#m1 and m2 are the masses of the two objects
#d1 is the total distance from the Earth, and d2 is the distance traveled from previous position
#rE is the radius of the Earth
import math 
m1 = 100
m2 = 5.972 * (10**24)
G = 6.674 * (10**-11)
d1 = 10000
d2 = 10000
rE = 6371000


x = (m1 * m2)
range = (10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 1000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
for d1 in range:
    print((G * (x/((rE+d1)**2))) * d2)




