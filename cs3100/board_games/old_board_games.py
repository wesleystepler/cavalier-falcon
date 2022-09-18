from node import Node

file = open("input2.txt")
tracker = 0 # Keeps track of where we are in the input so we can determine which numbers represent what
destination = 0
adj_list = []
cant_cross = []
for line in file:
    nums = [int(i) for i in line.split() if i.isdigit()]
    if len(nums) == 1:
        if tracker == 0:
            for i in range(0, int(line)):
                adj_list.append([])
                destination = int(line)-1
            tracker += 1
            continue
        elif tracker == 2:
            print(int(line))
            tracker += 1
            continue

        elif tracker > 2:
            line = line.replace("\n", "")
            cant_cross.append(line)
        tracker += 1
            

    elif len(nums) > 1:
        adj_list[nums[0]].append(nums[1])


for i in range(0, len(adj_list)):
    print(i, adj_list[i])

#print(cant_cross)

def same_path(old_path, new_path):
    different = []
    for i in range(1, len(old_path)):
        if old_path[i] != new_path[i]:
            different.append(new_path[i])
            
    return different


def search(graph, cant_cross, start, end):
    nodes = []
    # Create the nodes
    for i in range(0, len(graph)):
        n = Node(label=str(i), status="Unvisited", dist=1000000, path="NIL")
        nodes.append(n)

    node_stack = []
    nodes[0].dist = 0
    nodes[0].status = "Queued"
    node_stack.append(nodes[0])
    
    path = ""
    prev_paths = []

    while len(node_stack) != 0:
        temp = node_stack.pop() #node_stack.pop(node_stack.index(min(node_stack)))
        if temp.label not in cant_cross:
            for i in range(0, len(graph[int(temp.label)])):
                v = nodes[graph[int(temp.label)][i]]
                if v.status == "Unvisited":
                    v.status = "Queued"
                    v.dist = temp.dist + 1
                    v.path = temp.label
                    node_stack.append(v)
            #print()
            temp.status = "Visited"
            #print(temp)
            path += temp.label

        if int(temp.label) == end:
            break
    return path










def find_all_paths(graph, cant_cross, start, end):
    paths = []
    for i in range(0, 5):
        run = search(graph, cant_cross, start, end)
        paths.append(run)

    for path in paths:
        print(path)


print(search(adj_list, cant_cross, 0, destination))




    




