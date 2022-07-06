import math
opposite = 5
adjacent = 6
hyp = math.sqrt(((5**2) + (6**2)))

def sin(x):
    return float(opposite/hyp)

def cos(x):
    return float(adjacent/hyp)

print(hyp)
print(sin(90))
print(cos(90))

