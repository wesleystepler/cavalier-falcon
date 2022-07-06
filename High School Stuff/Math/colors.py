import random
def colorRandomizer(n):
    colors = range(0,n)
    counter = 0
    colorList = []
    colorList.append(random.choice(colors))
    
    while True == True:
        i = random.choice(colors)
        check = 0
        while check < len(colorList):
            if i == colorList[check]:
              check = len(colorList) + 1
            else:
                check += 1
            if check == len(colorList) - 1:
                colorList.append(i)
        counter += 1
        print(colorList)
        if len(colorList) == n:
            break 
        


    


print(colorRandomizer(10))