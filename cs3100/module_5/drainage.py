from map import Map


all_paths = []
max_path = []

def grid_search(grid, i, j, path):
    global all_paths
    global max_path

    current = grid[i][j]
    path.append(current)
    neighbors = []
    neighbors.append(current)
    if i < len(grid) - 1:
        neighbors.append(grid[i+1][j])
    if j < len(grid[i]) - 1:
        neighbors.append(grid[i][j+1])
    if i > 0:
        neighbors.append(grid[i-1][j])
    if j > 0:
        neighbors.append(grid[i][j-1])

    if min(neighbors) == current:
        all_paths.append(path.copy())
        if len(path) > len(max_path):
            max_path = path.copy()
        return path

    else:
        if i + 1 < len(grid):
            if grid[i+1][j] < current:
                grid_search(grid, i+1, j, path)
                path.pop()
        if j+1 < len(grid[i]):
            if grid[i][j+1] < current:
                grid_search(grid, i, j+1, path)
                path.pop()
        if j - 1 >= 0:
            if grid[i][j-1] < current:
                grid_search(grid, i, j-1, path)
                path.pop()
        if i - 1 >= 0:
            if grid[i-1][j] < current:
                grid_search(grid, i-1, j, path)
                path.pop()




num_cases = int(input())
for i in range(0, num_cases):
    label_and_size = input().split()
    m = Map()
    m.label = label_and_size[0]
    grid = []
    for j in range(0, int(label_and_size[1])):
        row = [int(i) for i in input().split()]
        grid.append(row)


    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            grid_search(grid, i, j, [])

    #print(all_paths)
    print(max_path)
    print(len(max_path))
    all_paths.clear()
    max_path.clear()

    
