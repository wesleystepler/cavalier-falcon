flag = False
my_list = [0, 5, 3]
for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i] == my_list[j]:
            flag == True

print(flag)