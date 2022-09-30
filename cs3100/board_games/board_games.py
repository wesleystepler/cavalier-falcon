class Node:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, label=1000000000000, status="Unvisited") -> None:
        possible_statuses = ["Unvisited", "Queued", "Visited"]
        self.label = label
        self.status = status

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
    if len(graph) > 1 and 0 not in cant_cross:
        start.status = "Visited"
        if path[-1] == end:
            path_str = '0'
            for node in path:
                if node == 0:
                    continue
                path_str += f'-{node}'
            print(path_str)
        else:
            for i in range(0, len(graph[start.label])):
                v = nodes[graph[start.label][i]]
                if v.status == "Unvisited" and v.label not in cant_cross:
                    path.append(int(v.label))
                    dfs(graph, nodes, cant_cross, v, end, path)
                    path.pop()
                    v.status = "Unvisited"


if __name__ == "__main__":
    nodes = []
    adj_list = []
    cant_cross = []
    prev_input = []

    num_nodes = int(input())
    destination = num_nodes - 1
    for i in range(0, num_nodes):
        adj_list.append([])
    num_edges = int(input())

    for i in range(0, num_edges):
        nums = [int(i) for i in input().split() if i.isdigit()]
        if nums in prev_input:
            continue
        else:
            if num_nodes >= 2:
                adj_list[nums[0]].append(nums[1])
                adj_list[nums[1]].append(nums[0])
        prev_input.append(nums)
        
    for lst in adj_list:
        lst.sort()
    num_danger = int(input())
    for i in range(0, num_danger):
        cant_cross.append(int(input()))

    nodes = []
    # Create the nodes
    if len(adj_list) != 0:
        for i in range(0, len(adj_list)):
            n = Node(label=i, status="Unvisited")
            nodes.append(n)

        start_node = nodes[0]

        dfs(adj_list, nodes, cant_cross, start_node, destination, [0])
