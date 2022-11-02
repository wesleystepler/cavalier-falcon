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

all_paths = []
def grid_search(grid, index_a, index_b, visited):
    global all_paths
    for i in range(index_a, len(grid)):
        for j in range(index_b, len(grid[i])):
            print(j)
            visited.append(grid[i][j])
            current = grid[i][j]
            if current == 78:
                print()
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
                all_paths.append(visited.copy())
                return visited

            elif grid[i+1][j] < current:
                grid_search(grid, index_a+1, index_b, visited)
                visited.clear()
            
            elif grid[i][j+1] < current:
                grid_search(grid, index_a, index_b+1, visited)
                visited.clear()

            elif grid[i][j-1] < current and j > 0:
                index_b -= 1
                grid_search(grid, index_a, index_b-1, visited)
                visited.clear()

            elif grid[i-1][j] < current and i > 0:
                index_a -= 1
                grid_search(grid, index_a-1, index_b, visited)
                visited.clear()

print(grid_search(grid, 0, 0, []))
print(all_paths)

    
