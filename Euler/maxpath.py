import random
r1 =                                                  [75]
r2 =                                                 [95,64]
r3 =                                                [17,47,82]
r4 =                                               [18,35,87,10]
r5 =                                              [20,4,82,47,65]
r6 =                                             [19,1,23,75,3,34]
r7 =                                            [88,2,77,73,7,63,67]
r8 =                                           [99,65,4,28,6,16,70,92]
r9 =                                          [41,41,26,56,83,40,80,70,33]
r10 =                                        [41,48,72,33,47,32,37,16,94,29]
r11 =                                       [53,71,44,65,25,43,91,52,97,51,14]
r12 =                                      [70,11,33,28,77,73,17,78,39,68,17,57]
r13 =                                     [91,71,52,38,17,14,91,43,58,50,27,29,48]
r14 =                                    [63,66,4,68,89,53,67,30,73,16,69,87,40,31]
r15 =                                   [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

#Think of this as the maximum path having n different routes. At the first row, there's only one path: 75, so n is 1. 
#At the next row, it has two paths, 95 or 64, making it n+1 routes. This continues on as the triangle goes down, n+2 possible routes, then n+3,
#n+4, all the way to n+15.

bigPath = 75 #It will always start at 75
