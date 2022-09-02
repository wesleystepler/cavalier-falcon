password_list = []

for i in range(8):
    password = [1,1,1,1,1,1,1,1]
    if password[i] == 0:
        next
    password[i] = 0
    for j in range(i+1, 8):
        
        if password[j] == 0:
            next
        
        password[j] = 0
        if password.count(0) >= 3:
            password[j-1] = 1

        password_copy = password.copy()
        for k in range(j+1, 8):
            if password[k] == 0:
                next
            #password_copy_2 = password.copy()
            if password.count(0) >= 3:
                password[k-1] = 1

            password[k] = 0
            password_copy_2 = password.copy()
            password_list.append(password_copy_2)
            #password = password_copy_2
        password = password_copy


repeat_check = password_list.copy()
for i in range(0, len(password_list)):
    for j in range(0, len(repeat_check)):
        if password == password_copy and i != j:
            print("These combinations are not unique.")


num = 0o11111
num_passwords = []

while num <= 0o77777:
    num += 0o1
    num_str = str(oct(num))
    num_str = num_str.replace("0o", "")
    pword = list(map(int, num_str))
    for i in range(1, 8):
        no_repeats = True
        if pword.count(i) > 1:
            no_repeats = False
            break
    if no_repeats and pword.count(0) == 0:
        num_passwords.append(pword)


final_passwords = []
for j in range(0, len(password_list)):
    for i in range(0, len(num_passwords)):
        n = 0
        for k in range(0, len(password_list[j])):
            if password_list[j][k] == 0:
                continue
            password_list[j][k] = num_passwords[i][n]
            n += 1
        password_list_copy = password_list[j].copy()
        final_passwords.append(password_list_copy)
        
    
for i in range(0, 100):
    print(final_passwords[i])

print() 
print(len(final_passwords))
        

