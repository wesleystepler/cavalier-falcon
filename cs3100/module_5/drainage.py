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
    for i in range(index_a, len(grid)):
        for j in range(index_b, len(grid[i])):
            visited = []
            current = grid[i][j]
            neighbors = []
            if i < len(grid) - 1:
                neighbors.append(grid[i+1][j])
            if j < len(grid[i]) - 1:
                neighbors.append(grid[i][j+1])
            if i > 0:
                neighbors.append(grid[i-1][j])
            if j > 0:
                neighbors.append(grid[i][j-1])
            counter = 0
            for num in neighbors:
                if current < num:
                    counter += 1
            if counter == len(neighbors):
                path.append(visited)

            elif grid[i+1][j] < current:
                visited.append(grid[i+1][j])
                index_a += 1
                grid_search(grid, index_a, index_b, path)
                visited.clear()
            
            elif grid[i][j+1] < current:
                visited.append(grid[i][j+1])
                index_b += 1
                grid_search(grid, index_a, index_b, path)
                visited.clear()

            elif grid[i][j-1] < current and j > 0:
                visited.append(grid[i][j-1])
                index_b -= 1
                grid_search(grid, index_a, index_b, path)
                visited.clear()

            elif grid[i-1][j] < current and i > 0:
                visited.append(grid[i-1][j])
                index_a -= 1
                grid_search(grid, index_a, index_b, path)
                visited.clear()

print(grid_search(grid, 0, 0, []))

    
