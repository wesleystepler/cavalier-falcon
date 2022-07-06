import math

#def webUpdate(a,b,c,d):
old = [1,1,1,1,1,1,1,1] #The Previous Page Rankings for a,b,c,d
i = 0
while i < 10000:
#Sites that point to 0: 6,2,4   Go from 0: 1,5
#Sites that point to 1: 0,1,2,3,5  Go from 1: 1,2,3,5,7
#Sites that point to 2: 1,5  Go from 2: 0,1,3,4,5
#Sites that point to 3: 1,2,5  Go from 3: 1
#Sites that point to 4: 2,4,6,7  Go from 4: 0,4,7
#Sites that point to 5: 0,1,2,5,6  Go from 5: 2,1,3,5,7
#Sites that point to 6: 6  Go from 6: 0,4,5,6,7
#Sites that point to 7: 1,4,5  Go from 7: 4
        
    Page0 = (1-0.85) + 0.85*((float(old[2])/5)) + (float(old[4])/3 ) + (float(old[6])/5 )
    Page1 = (1-0.85) + 0.85*((float(old[1])/5 ) + (float(old[2])/5 )) + (float(old[3])/1 ) + (float(old[5])/4 ) + (float(old[0])/2 )
    Page2 = (1-0.85) + 0.85*((float(old[1])/5 )) + (float(old[5])/4 )
    Page3 = (1-0.85) + 0.85*((float(old[1])/5 ) + (float(old[2])/5 )) + (float(old[5])/4 )
    Page4 = (1-0.85) + 0.85*((float(old[2])/5 )) + (float(old[4])/3 ) + (float(old[6])/5 ) + (float(old[7])/1)
    Page5 = (1-0.85) + 0.85*((float(old[0])/2 )) + (float(old[1])/5 ) + (float(old[2])/5 ) + (float(old[5])/4 ) + (float(old[6])/5 )
    Page6 = (1-0.85) + 0.85*((float(old[6])/5))
    Page7 = (1-0.85) + 0.85*((float(old[1])/5 )) + (float(old[4])/3 ) + (float(old[5])/4 )
        
    new = [Page0,Page1,Page2,Page3,Page4,Page5,Page6,Page7] #The new page rankings for a,b,c,d
    print(new)
    old = new
    i += 1