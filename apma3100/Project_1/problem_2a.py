password_list = []

for i in range(8):
    password = [1,1,1,1,1,1,1,1]
    if password[i] == 0:
        next
    password[i] = 0
    for j in range(i+1, 8):
        
        password[j] = 0
        if password.count(0) >= 3:
            password[j-1] = 1

        password_copy = password.copy()
        for k in range(j+1, 8):
            if password.count(0) >= 3:
                password[k-1] = 1

            password[k] = 0
            password_copy_2 = password.copy()
            password_list.append(password_copy_2)
        password = password_copy


for password in password_list:
    print(password)
print()
print(len(password_list))

# This checks fo make sure every password is actually unique
repeat_check = password_list.copy()
for i in range(0, len(password_list)):
    for j in range(0, len(repeat_check)):
        if password == password_copy and i != j:
            Exception("These combinations are not unique.")

