#This is Project Euler problem #40

numString = ""
i = 1
while len(numString) <= 1000000:
    print("Running interation " + str(i))
    numString += str(i)
    i += 1

#print(len(numString))

term1 = int(numString[0])
term2 = int(numString[10-1])
term3 = int(numString[100-1])
term4 = int(numString[1000-1])
term5 = int(numString[10000-1])
term6 = int(numString[100000-1])
term7 = int(numString[1000000-1])
solution = term1*term2*term3*term4*term5*term6*term7
print(solution)


