# We need the code from problem 2a again, so we'll get our password_list again here

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

#Ok, these needs some explaining. num is in base 8, meaning the digits it uses are 0-7. It starts at
#11111 (the 0o is just Python's octal notation) and goes to 77777, incrementing by 1 in each iteration of the
#while loop. num is converted to a string, the 0o is taken off, and then it's converted to a list of ints.
#The for loop then checks if any of the digits are repeated. If none are repeated and there are no zeroes in the
#password, then it will be added to the list of valid combinations. 
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

#However, the previous block does not take the 0s into account, it just has a list of the possible 5-number
#combinations using 1-7. This next block of nested for loops goes through the previously determined binary
#passwords with three 0s, and for each of those passwords replaces the 5 ones with all possible 5 number
#combinations of 1-7 that we found previously. The result is the number of unique passwords with exactly 3 zeroes
#and 5 numbers 1-7 with no repeating values.

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
        

