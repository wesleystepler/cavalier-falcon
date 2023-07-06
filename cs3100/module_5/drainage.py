# Python Program to solve the problem described here: 
# chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://markfloryan.github.io/dsa2/homeworks/fall2022/05-dynamicprogramming/drainage.pdf
# Written for CS 3100, Data Structures and Algorithms II, at the University of Virginia

from map import Map

all_paths = []
max_path = []
past_paths = {}

def grid_search(grid, i, j, path):
    global all_paths
    global max_path
    global past_paths

    current = grid[i][j]
    if current in past_paths:
        path += past_paths[current]
        all_paths.append(path.copy())
        past_paths[path[0]] = path.copy()
        if len(path) > len(max_path):
            max_path = path.copy()
        return path
        
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
        if path[0] in past_paths:
            if len(path) > len(past_paths[path[0]]):
                past_paths[path[0]] = path.copy()
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
        for j in range(0, len(grid[i])):
            grid_search(grid, i, j, [])

    #print(all_paths)
    #print(max_path)
    print(f"{m.label}: {len(max_path)}")
    all_paths.clear()
    max_path.clear()

    
