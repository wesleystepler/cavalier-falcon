from node import Node
from node_neighbors import NodeNeighbors

nums = [int(i) for i in input().split() if i.isdigit()]
num_nodes = nums[0]
num_connections = nums[1]

adj_matrix = []
node_list = []

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
    node_list.append(Node(juncs[0], False, juncs[1], i, []))

for i in range(0, num_connections):
    c = input()
    c = c.split(" ")
    for node in node_list:
        if node.label == c[0]:
            node1 = node
        elif node.label == c[1]:
            node2 = node

    node1.neighbors.append(NodeNeighbors(node2, int(c[2])))
    node2.neighbors.append(NodeNeighbors(node1, int(c[2])))
    adj_matrix[node1.index][node2.index] = int(c[2])
    adj_matrix[node2.index][node1.index] = int(c[2])  


#for node in node_list:
#    print(node.label, ":", node.neighbors)  

def add_to_queue(graph, cur_node, pq):
    cur_node.known = True
    for i in range(0, len(cur_node.neighbors)):
        if not cur_node.neighbors[i].node.known:
            pq.append(cur_node.neighbors[i])

"""
Adj Matrix Reference
     b1 j1 s1 l1 l2 o1
b1    0  5  0  0  0  1
j1    5  0  1  0  0  2
s1    0  1  0  6  1  0
l1    0  0  6  0  2  1
l2    0  0  1  2  0  0
01    1  2  0  1  0  0
"""

def prims(graph, num_nodes, node_list):
    m = num_nodes - 1
    edge_count = 0
    cost = 0
    mst_edges = []
    pq = []
    cur_node = node_list[0]
    cur_node.known = True
    add_to_queue(graph, cur_node, pq)
    #print(pq)

    while len(pq) != 0 and edge_count != m:
        cur_edge = min(pq)
        pq.remove(cur_edge)
        cur_node = cur_edge.node

        if cur_node.known:
            continue
        mst_edges.append(cur_edge)
        cost += cur_edge.cost
        
        add_to_queue(graph, cur_node, pq)
        #print(pq)

    print(mst_edges)
    print(cost)

prims(adj_matrix, num_nodes, node_list)