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
completed = []
def grid_search(grid, index_a, index_b, visited):
    global all_paths
    global completed
    
    while index_a < len(grid):
        while index_b < len(grid[i]):
            print(index_a, index_b)
            visited.append(grid[index_a][index_b])
            current = grid[index_a][index_b]
            if current == 7:
                print()
            neighbors = []
            if index_a < len(grid) - 1:
                neighbors.append(grid[index_a+1][index_b])
            if index_b < len(grid[index_a]) - 1:
                neighbors.append(grid[index_a][index_b+1])
            if index_a > 0:
                neighbors.append(grid[index_a-1][index_b])
            if index_b > 0:
                neighbors.append(grid[index_a][index_b-1])
            counter = 0
            for num in neighbors:
                if current < num:
                    counter += 1
            if counter == len(neighbors):
                all_paths.append(visited.copy())
                if len(visited) > 1:
                    return visited
                

            else:

                if index_a + 1 < len(grid):
                    if grid[index_a+1][index_b] < current:
                        temp1 = index_a
                        temp2 = index_b
                        grid_search(grid, index_a+1, index_b, visited)
                        index_a = temp1
                        index_b = temp2
                        visited.pop()
                if index_b+1 < len(grid[index_a]):
                    if grid[index_a][index_b+1] < current:
                        temp1 = index_a
                        temp2 = index_b
                        grid_search(grid, index_a, index_b+1, visited)
                        index_a = temp1
                        index_b = temp2
                        visited.pop()
                if index_b - 1 >= 0:
                    if grid[index_a][index_b-1] < current:
                        temp1 = index_a
                        temp2 = index_b
                        grid_search(grid, index_a, index_b-1, visited)
                        index_a = temp1
                        index_b = temp2
                        visited.pop()
                if index_a - 1 >= 0:
                    if grid[index_a-1][index_b] < current:
                        temp1 = index_a
                        temp2 = index_b
                        grid_search(grid, index_a-1, index_b, visited)
                        index_a = temp1
                        index_b = temp2
                        visited.pop()
            visited.clear()

            index_b += 1
        index_a += 1
    return "Done"

print(grid_search(grid, 0, 0, []))
print(all_paths)

    
