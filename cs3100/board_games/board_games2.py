def dfs(graph, cant_cross, start, end, path, prev_paths, visited):
    if len(graph) > 1 and 0 not in cant_cross:
        visited.append(start)
        if path[-1] == end:
            #path_str = ''
            for i in range(0, len(path)):
                if i == 0:
                    path_str = str(path[i])
                else:
                    path_str += '-' + str(path[i])
            if path_str not in prev_paths:
                print(path_str)
                prev_paths.append(path_str)
        else:
            for i in range(0, len(graph[start])):
                v = graph[start][i]
                if v not in visited and v not in cant_cross:
                    path.append(v)
                    dfs(graph, cant_cross, v, end, path, prev_paths, visited)
                    path.pop()
                    visited.remove(v)
        


nodes = []
adj_list = []
cant_cross = []
prev_input = []
prev_paths = []
num_nodes = int(input())
destination = num_nodes-1

for i in range(0, num_nodes):
    adj_list.append([])

num_edges = int(input())

for i in range(0, num_edges):
    nums = [int(j) for j in input().split() if j.isdigit()]
    if nums in prev_input or [nums[1], nums[0]] in prev_input:
        continue
    elif nums[0] == nums[1]:
        continue
    else:
        adj_list[nums[0]].append(nums[1])
        adj_list[nums[1]].append(nums[0])
    prev_input.append(nums)

danger = int(input())
for i in range(0, danger):
    cant_cross.append(int(input()))
for list in adj_list:
    list.sort()
dfs(adj_list, cant_cross, 0, destination, [0], prev_paths, [])
