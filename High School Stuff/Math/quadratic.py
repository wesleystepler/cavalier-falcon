import math
def quadratic(a,b,c):
    return (-b + math.sqrt(b**2-(4*a*c)))/2*a, (-b - math.sqrt(b**2-(4*a*c)))/2*a

print(quadratic(50.7165,1099.56,-5959.76))