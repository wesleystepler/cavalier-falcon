for i in range(0,1000000):
    print(i**3)


#Potential Strategy here: Say your cube is 473829473.
#To determine other cubic permutations, go through cubes and have this
#line of logic, assuming the other cube is 'x':
#if 4 in x, if 7 in x, if 3 in x, etc.
#This will determine if the numbers are all the same, albeit it may run rather slow