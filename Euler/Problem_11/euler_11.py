grid = []
while True:
    i = input()
    if i == "DONE":
        break
    else:
        grid.append(i.split())

for row in grid:
    for i in range(0, len(row)):
        row[i] = int(row[i])

for row in grid:
    print(row)

def move_horizontal(grid, num):
    totals = []
    for row in grid:
        for i in range(0, len(grid)):
            if i <= len(row) - num:
                p = row[i]
                for n in range(1, num):
                    p *= row[i+n]
                totals.append(p)
    #print(len(totals))
    return max(totals)


def move_vertical(grid, num):
    totals = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if i <= len(grid) - num:
                p = grid[i][j]
                for n in range(1, num):
                    p *= grid[i+n][j]
                totals.append(p)

    #print(len(totals))
    return max(totals)

def move_diagonal_down(grid, num):
    totals = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if i <= len(grid) - num and j <= len(grid[i]) - num:
                p = grid[i][j]
                for n in range(1,num):
                    p *= grid[i+n][j+n]
                totals.append(p)

    #print(len(totals))
    return max(totals)

def move_diagonal_up(grid, num):
    totals = []
    for i in range(1, len(grid)):
        for j in range(0, len(grid[i])):
            if i >= len(grid) - num and j <= len(grid[i]) - num:
                # These are negative because you're starting at the bottom of the grid and going up
                p = grid[-i][j]
                for n in range(1, num):
                    p *= grid[-i - n][j + 1]
                totals.append(p)

    #print(len(totals))
    return max(totals)



print(max(move_diagonal_down(grid, 4), move_horizontal(grid, 4), move_vertical(grid, 4), move_diagonal_up(grid, 4)))




        


