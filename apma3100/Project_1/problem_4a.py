passwords = []

#For our purposes, let A = 1, B = 2, and C = 3. 

#This is a doozy of a nested for loop. What's happening here is i represents the first digit of the password,
#j represents the second, k the third, l the fourth, and m the fifth. This structure iterates through all
#possible 5 letter combinations of A, B, and C, but it only adds it to the list of valid passwords if there are
#exactly 2 As, 2 Bs, and 1 C. 
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            for l in range(1, 4):
                for m in range(1, 4):
                    password = [i,j,k,l,m]
                    if password.count(1) == 2 and password.count(2) == 2 and password.count(3) == 1:
                        print(password)
                        password_copy = password.copy()
                        passwords.append(password_copy)

print(len(passwords))

# This checks to make sure every password is unique. 
repeat_check = passwords.copy()
for i in range(0, len(passwords)):
    for j in range(0, len(repeat_check)):
        if password == password_copy and i != j:
            Exception("These combinations are not unique.")
