import random
a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]

i = 0
twos = []
threes = []
fours = []
fives = []
sixes = []
sevens = []
eights = []
nines = []
tens = []
elevens = []
twelves = []
while i < 400:
    x = random.choice(a)
    y =random.choice(b)
    print((x,y),(x+y))

    if x+y == 2:
        twos.append(x+y)

    if x+y == 2:
        twos.append(x+y)

    if x+y == 2:
        twos.append(x+y)

    if x+y == 2:
        twos.append(x+y)
        

    i += 1