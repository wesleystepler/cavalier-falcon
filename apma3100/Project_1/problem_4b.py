passwords = []

#For our purposes, let A = 1, B = 2, C = 3, D = 4, and E = 5

#Only a few things changed from part a to part b. Now, each for loop goes from 1 to 5, and the only
#conditions we're checking for are that there aren't any Ds or Es in the password. 
for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            for l in range(1, 6):
                for m in range(1, 6):
                    password = [i,j,k,l,m]
                    if password.count(4) == 0 and password.count(5) == 0:
                        print(password)
                        password_copy = password.copy()
                        passwords.append(password_copy)

print(len(passwords))

repeat_check = passwords.copy()
for i in range(0, len(passwords)):
    for j in range(0, len(repeat_check)):
        if password == password_copy and i != j:
            Exception("These combinations are not unique.")