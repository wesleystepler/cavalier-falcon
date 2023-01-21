from node import Node
from node_edge import NodeEdge

nums = [int(i) for i in input().split() if i.isdigit()]
num_nodes = nums[0]
num_connections = nums[1]
adj_matrix = []
nodes_dict = {}
#nodes_list = []

"""
Index reference:
0 = b1
1 = j1
2 = s1
3 = l1
4 = l2
5 = o1
"""
for i in range(0, num_nodes):
    adj_matrix.append([0]*num_nodes)
    juncs = [j for j in input().split()]
    nodes_dict[i] = Node(juncs[0], False, juncs[1], i, [])
    #nodes_list.append(Node(juncs[0], "Unvisited", juncs[1], i))

for i in range(0, num_connections):
    c = input()
    c.split(" ")
    