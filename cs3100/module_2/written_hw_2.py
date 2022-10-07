class Node:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, label=1000000000000, status="Unvisited", index=0) -> None:
        possible_statuses = ["Unvisited", "Queued", "Visited"]
        self.label = label
        self.status = status
        self.index = index

    def __gt__(self, other):
        if self.label > other.label:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.label < other.label:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.label == other.label:
            return True
        else:
            return False


    def __repr__(self) -> str:
        return f"Label: {self.label}\n Status: {self.status}"

        
def dfs(graph, nodes, cant_cross, start, end, path):
    path = []
    for i in range(0, len(nodes)):
        nodes[i].status = "Unvisited"
    s = nodes[0]
    s.status = "Queued"
    node_stack = []
    node_stack.append(s)
    while len(node_stack) != 0:
        cur_node = node_stack.pop()
        for i in range(0, len(adj_matrix[cur_node.index])):
            if adj_matrix[cur_node.index][i] == 1:
                if nodes[i].status == "Unvisited":
                    nodes[i].status = "Queued"
                    node_stack.append(nodes[i])
        cur_node.status = "Visited"
        path.append(int(cur_node.label))
        if int(cur_node.label) == end:
            break

    return path


if __name__ == "__main__":
    nodes = []
    adj_matrix = []
    cant_cross = []
    prev_input = []

    num_nodes = int(input())
    destination = num_nodes - 1
    for i in range(0, num_nodes):
        adj_matrix.append([0]*num_nodes)
    num_edges = int(input())

    for i in range(0, num_edges):
        nums = [int(i) for i in input().split() if i.isdigit()]
        if nums in prev_input:
            continue
        else:
            adj_matrix[nums[0]][nums[1]] = 1
            adj_matrix[nums[1]][nums[0]] = 1
        prev_input.append(nums)
        

    num_danger = int(input())
    for i in range(0, num_danger):
        cant_cross.append(int(input()))

    nodes = []
    # Create the nodes
    
    for i in range(0, len(adj_matrix)):
        n = Node(label=i, status="Unvisited", index=i)
        nodes.append(n)

    start_node = nodes[0]

    print(dfs(adj_matrix, nodes, cant_cross, start_node, destination, [0]))
