#Euler 28
i = 1
squares = []
while i <= 1001:
    squares.append(i)
    i += 2
#I think you need to use curses to fully generate this spiral
#
#
#            73 74 75 76 77 78 79 80 81   
#            72 43 44 45 46 47 48 49 50
#            71 42 21 22 23 24 25 26 51
#            70 41 20  7  8  9 10 27 52
#            69 40 19  6  1  2 11 28 53
#            68 39 18  5  4  3 12 29 54
#            67 38 17 16 15 14 13 30 55
#            66 37 36 35 34 33 32 31 56  
#            65 64 63 62 61 60 59 58 57
#   
#