from node import Node
from node_neighbors import NodeNeighbors

nums = [int(i) for i in input().split() if i.isdigit()]
num_nodes = nums[0]
num_connections = nums[1]
pre_switches = 0
switches = 0
post_switches = 0

adj_matrix = []
node_list = []


for i in range(0, num_nodes):
    adj_matrix.append([0]*num_nodes)
    juncs = [j for j in input().split()]
    n = Node(juncs[0], False, juncs[1], i, [])
    if n.type == "switch":
        last_switch = n.label
        switches += 1
    elif n.type == "light":
        n.which_switch = last_switch
        post_switches += 1
    else:
        pre_switches += 1
    node_list.append(n)

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

def add_to_queue(mst_edges, cost, cur_node, pq):
    cur_node.known = True
    for i in range(0, len(cur_node.neighbors)):
        if not cur_node.neighbors[i].node.known:
            pq.append(cur_node.neighbors[i])

        else:
            for j in range(0, len(mst_edges)):
                if cur_node.neighbors[i].node == mst_edges[j].node and cur_node.neighbors[i].cost < mst_edges[j].cost:
                    cost -= mst_edges[j].cost
                    mst_edges[j] = cur_node.neighbors[i]
                    cost += cur_node.neighbors[i].cost


def prims(graph, num_nodes, node_list):
    """
    Current Problem: illegal connections are still in the pq, need to not 
    be there and/or ignored
    """
    m = num_nodes - 1
    edge_count = 0
    cost = 0
    mst_edges = []
    pq = []
    cur_node = node_list[0]
    cur_node.known = True
    add_to_queue(mst_edges, cost, cur_node, pq)
    #print(pq)

    while len(pq) != 0 and len(mst_edges) < m:
        print(pq)
        cur_edge = min(pq)
        pq.remove(cur_edge)

        cur_node = cur_edge.node
        if cur_node.known:
            continue
        mst_edges.append(cur_edge)
        cost += cur_edge.cost
        
        add_to_queue(mst_edges, cost, cur_node, pq)
        #print(pq)

    #print(mst_edges)
    print(cost)

prims(adj_matrix, num_nodes, node_list)