#Euler 15
import random
def latticePath(n): #Runs lattice paths for an n*n grid
    right = 0
    down = 0

    current = []
    while right != n and down != n:
    

        currentMove = random.choice(right,down)
        if currentMove == True:
            if currentMove == right:
                current.append("Right")
                right += 1
            else:
                current.append("Down")
                down += 1
    print(current)

    




print(latticePath(2))

   # while movesRight != n and movesDown != n: #Once movesRight or movesDown = n,it's gone as far as it can go.
   #     current =[] #This stores the current path you're taking
#
 #       if goRight == True:
  #          movesRight += 1
   #         if movesRight == n:
    #            goRight = False
     #       current.append("Right")
#
 #       if goDown == True:
  #          movesDown += 1
   #         current.append("Down")
    ##           goDown = False