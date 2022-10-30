from map import Map

num_cases = int(input())
for i in range(0, num_cases):
    label_and_size = input().split()
    m = Map()
    m.label = label_and_size[0]
    grid = []
    for j in range(0, int(label_and_size[1])):
        row = [int(i) for i in input().split()]
        grid.append(row)

    
for row in grid:
    print(row)

def grid_search(grid, index_a, index_b, path):
    current = grid[index_a][index_b]
    if grid[index_a+1][index_b] < current and index_a < len(grid):
        path.append(grid[index_a+1][index_b])
        index_a += 1
        grid_search(grid, index_a, index_b, path)
    
    elif grid[index_a][index_b+1] < current and index_a + 1 < len(grid[index_a]):
        path.append(grid[index_a][index_b+1])
        index_b += 1
        grid_search(grid, index_a, index_b, path)

    elif grid[index_a][index_b-1] < current and index_b > 0:
        path.append(grid[index_a][index_b-1])
        index_b -= 1
        grid_search(grid, index_a, index_b, path)

    elif grid[index_a-1][index_b] < current and index_a > 0:
        path.append(grid[index_a-1][index_b])
        index_a -= 1
        grid_search(grid, index_a, index_b, path)
    else:
        return path

print(grid_search(grid, 0, 0, []))

    
