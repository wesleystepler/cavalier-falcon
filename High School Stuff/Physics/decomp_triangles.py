import math
opposite = 5
adjacent = 6
hyp = math.sqrt(((5**2) + (6**2)))

def sin(x):
    return float(math.degrees(opposite/hyp))

def cos(x):
    return float(math.degrees(adjacent/hyp))

print(hyp)
print(sin(60))
print(cos(60))