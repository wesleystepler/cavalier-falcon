import math
def areInverse(f, g):
  for i in range (4):
    if f(g(i)) != i:
          return False
    return True

def a(x):
  return x*2

def b(x):
  return x/2
print areInverse(a,b)
