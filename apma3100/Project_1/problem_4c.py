passwords = []

#For our purposes, let A = 1, B = 2, C = 3, D = 4, E = 5

#Same as the last two, not much really changes here. Now, we just don't have any condition at all,
#Since the password can be any combination of the 5 letters. 
for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            for l in range(1, 6):
                for m in range(1, 6):
                    password = [i,j,k,l,m]
                    print(password)
                    password_copy = password.copy()
                    passwords.append(password_copy)

print(len(passwords))

repeat_check = passwords.copy()
for i in range(0, len(passwords)):
    for j in range(0, len(repeat_check)):
        if password == password_copy and i != j:
            Exception("These combinations are not unique.")