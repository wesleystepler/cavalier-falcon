#Euler 11
#This is gross because I tried to do it without reading in the file, which I think I need to do. I'm gonna keep it for
#Fun, but will no longer edit this one
r1 = [8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
r2 = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00]
r3 = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
r4 = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
r5 = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
r6 = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
r7 = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
r8 = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
r9 = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
r10 =[21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95]
r11 =[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
r12 =[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57]
r13 =[86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
r14 =[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
r15 =[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
r16 =[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
r17 =[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
r18 =[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
r19 =[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
r20 =[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]

row = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20] #So I can work with each list in the loops
horizontal = [] #The list that stores the product of each pair of four adjacent numbers

print("Please wait while we process your code...")

h = 0 #h as in horizontal
while h < len(row):
    i = 0
    while i < len(r1) - 4: #This loop adds each group of four horizontal numbers to the horizontal list
        currentList = row[h]
        horizontal.append(row[h][i]*row[h][i+1]*row[h][i+2]*row[h][i+3])
        i += 1
    h += 1


vertical = [] #The list that stores the product of each four-pair of vertical numbers

v = 0 #v as in vertical
while v < len(row) - 4:
    i = 0
    while i < len(row): #This loop adds each gorup of four vertical numbers to the vertical list.
        vertical.append(row[v][i]*row[v+1][i]*row[v+2][i]*row[v+3][i])
        i += 1
    v += 1

diagonalNeg = [] #The list that stores the groups of four whose line has a negative slope

dN = 19 #The Row Number
while dN >= 0:
    i = 3 #The Row Index
    while i < len(row): #This loop is for the diagonal numbers with a negative slope
        diagonalNeg.append(row[dN][i]*row[dN-1][i-1]*row[dN-2][i-2]*row[dN-3][i-3])
        i += 1
    dN -= 1

print(diagonalNeg)


diagonalPos = [] #The list that stores the digonal groups of four whose line has a positive slope
dP = 19

while dP >= 0:
    i = 16
    while i >= 0:
        diagonalPos.append(row[dP][i]*row[dP-1][i+1]*row[dP-2][i+2]*row[dP-3][i+3])
        i -= 1
    dP -= 1


results = [max(horizontal),max(vertical),max(diagonalNeg),max(diagonalNeg)]
#print(max(results))




    
