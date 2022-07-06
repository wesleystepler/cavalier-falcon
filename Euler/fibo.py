i = 0
n1 = 1
n2 = 1
while i < 10:
    print("F %s:"  #str(n1 + n2)) % i
    n2 = n1 + n2
    n1 = n2
    i += 1


    