from node import Node

destination = 0
nodes = []
adj_list = []
cant_cross = []

num_nodes = int(input())
num_edges = int(input())
p = []
for i in range(0, num_edges):
    nums = [int(i) for i in input().split() if i.isdigit()]
    adj_list[nums[0]].append(nums[1])
    adj_list[nums[1]].append(nums[0])
    

num_danger = int(input())
for i in range(0, num_danger):
    cant_cross.append(input())

def dfs(graph, nodes, cant_cross, start, end, path):
    start.status = "Visited"
    if path[-1] == end:
        print(path)
    visited_neighbors = 0
    for i in range(0, len(graph[int(start.label)])):
        v = nodes[graph[int(start.label)][i]]
        if v.status == "Unvisited" and v.label not in cant_cross and int(v.label) in graph[int(path[-1])] and v.label not in path:
            path += "-" + v.label
            dfs(graph, nodes, cant_cross, v, end, path)
            path = "0"
            v.status = "Unvisited"
            

nodes = []
# Create the nodes
for i in range(0, len(adj_list)):
    n = Node(label=str(i), status="Unvisited", dist=1000000, path="NIL")
    nodes.append(n)

start_node = nodes[0]

dfs(adj_list, nodes, cant_cross, start_node, destination, "0")




"""for line in file:
    nums = [int(i) for i in line.split() if i.isdigit()]
    if len(nums) == 1:
        if tracker == 0:
            for i in range(0, int(line)):
                adj_list.append([])
                destination = str(int(line)-1)
            tracker += 1
            continue
        elif tracker == 2:
            tracker += 1
            continue

        elif tracker > 2:
            line = line.replace("\n", "")
            cant_cross.append(line)
        tracker += 1
            

    elif len(nums) > 1:
        adj_list[nums[0]].append(nums[1])
        adj_list[nums[1]].append(nums[0])"""