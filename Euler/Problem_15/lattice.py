# This program is a solution to Project Euler Problem 15

# Constants that determine how large the grid we're working with is
ROWS = 2
COLS = 2

# 0 = travels along row (horizontally), 1 = travels along comlumn (vertically)
paths = []

path_0s = [0]*ROWS
path_1s = [1]*COLS


path_0s.extend(path_1s)
path = int("".join(str(x) for x in path_0s), 2)

path_1s.extend([0]*int(ROWS))
limit = int("".join(str(x) for x in path_1s), 2)

while path <= limit:
    # Convert the binary number into a list
    path_list = list(bin(path))

    # path_list includes the 0b prefix, which we need to remove
    #path_list.remove(path_list[0])
    #path_list.remove(path_list[0])

    if (ROWS+COLS) - (len(path_list)-2) > 0:
        trailing_zeroes = ['0']*((ROWS+COLS)-(len(path_list)-2))
        path_list.extend(trailing_zeroes)

    if path_list.count('0') != ROWS+1 or path_list.count('1') != COLS:
        print(f"Possible path {path} out of {limit} ({path_list}): Invalid")
        if list(bin(path+1)).count('0') != ROWS+1 or list(bin(path+1)).count('1') != COLS:
            path += 2 
        else:
            path += 1
        continue
    else:
        print(f"Possible path {path} out of {limit} ({path_list}): Valid")
        paths.append(path)
        if list(bin(path+1)).count('0') != ROWS+1 or list(bin(path+1)).count('1') != COLS:
            path += 2 
        else:
            path += 1

print(len(paths))