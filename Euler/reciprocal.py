d = float(1/7)
print(d)
dStr = str(d)
recur = []
for i in range(1, len(dStr) - 1):
    if dStr[i] == dStr[0]:
        print("At",dStr[i])
        recur.append(dStr[i])
    
    print(len(recur)) #Tells you the recurring cycle length



