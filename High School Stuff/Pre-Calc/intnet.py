import math

#def webUpdate(a,b,c,d):
old = [0.575, 0.724, 0.4, 0.652] #The Previous Page Rankings for a,b,c,d
i = 0
while i < 10:
        
    aPage = (1-0.85) + 0.85*((float(old[3])/1))
    bPage = (1-0.85) + 0.85*((float(old[0])/1) + (float(old[2])/2))
    cPage = (1-0.85) + 0.85*((float(old[1])/2))
    dPage = (1-0.85) + 0.85*((float(old[1])/2) + (float(old[2])/2))
        
    new = [aPage,bPage,cPage,dPage] #The new page rankings for a,b,c,d
    print(new)
    old = new
    i += 1

#webUpdate(0.575,0.724,0.4,0.652)