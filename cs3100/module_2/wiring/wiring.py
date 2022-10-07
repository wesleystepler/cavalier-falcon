"""
Collaborated with:
Andrew Cornfeld (cpm6gh)
Connor Wilson (crw8eg)
Lydia Stoner (lcs6bak)
Thomas Laughridge (tcl5tu)
"""

from node import Node
from node_neighbors import NodeNeighbors

def pre_switch(node):
    if node.type == "breaker" or node.type == "outlet" or node.type == "box":
        return True
    else:
        return False

def is_switch(node):
    if node.type == "switch":
        return True
    else:
        return False

def post_switch(node):
    if node.type == "light":
        return True
    else:
        return False

def can_connect(node1, node2):
    if pre_switch(node1) and pre_switch(node2):
        return True

    elif (pre_switch(node1) and is_switch(node2)) or (pre_switch(node2) and is_switch(node1)):
        return True 

    elif (is_switch(node1) and post_switch(node2) and node2.which_switch == node1.label) or (is_switch(node2) and post_switch(node1) and node1.which_switch == node2.label):
        return True

    elif post_switch(node1) and post_switch(node2) and node1.which_switch == node2.which_switch:
        return True
    
    else:
        return False



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
    n = Node(juncs[0], "Unknown", juncs[1], i, [])
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


    if can_connect(node1, node2):
            #node1.neighbors.append(NodeNeighbors(node2, node1, int(c[2])))
            #node2.neighbors.append(NodeNeighbors(node1, node2, int(c[2])))
            adj_matrix[node1.index][node2.index] = int(c[2])
            adj_matrix[node2.index][node1.index] = int(c[2])  


def add_to_queue(graph, node_list, mst_edges, cost, cur_node, pq):
    cur_node.status = "Known"
    for i in range(0, len(graph[cur_node.index])):
        if graph[cur_node.index][i] != 0:
            n = NodeNeighbors(node_list[i], node_list[cur_node.index], graph[cur_node.index][i])
            if not n.node.status == "Known":
                pq.append(n)
                graph[i][cur_node.index] = 0

       
def prims(graph, num_nodes, node_list, pre_s, s, post_s):
    m = num_nodes - 1
    cost = 0
    mst_edges = []
    pq = []
    cur_node = node_list[0]
    cur_node.status = "Known"
    add_to_queue(graph, node_list, mst_edges, cost, cur_node, pq)
    #print(pq)

    while len(pq) != 0 and len(mst_edges) < m:
        cur_edge = Node() # Dummy value
        if pre_s > 0:
            poss_min = []
            if pre_s == 1:
                cur_edge = min(pq)
                pq.remove(cur_edge)
            else:
                for i in range(0, len(pq)):
                    if pre_switch(pq[i].node):
                        poss_min.append(pq[i])
                cur_edge = min(poss_min)
                pq.remove(cur_edge)
            pre_s -= 1

        elif s > 0:
            poss_min = []
            if s == 1:
                cur_edge = min(pq)
                pq.remove(cur_edge)
            else:
                for i in range(0, len(pq)):
                    if is_switch(pq[i].node):
                        poss_min.append(pq[i])
                cur_edge = min(poss_min)
                pq.remove(cur_edge)
            s -= 1

        elif post_s > 0:
            poss_min = []
            if post_s == 1:
                cur_edge = min(pq)
                pq.remove(cur_edge)
            else:
                for i in range(0, len(pq)):
                    if post_switch(pq[i].node):
                        poss_min.append(pq[i])
                cur_edge = min(poss_min)
                pq.remove(cur_edge)
            post_s -= 1

        else:
            cur_edge = pq[0]
            pq.remove(cur_edge)

        cur_node = cur_edge.node
        if cur_node.status == "Known": 
            continue
        mst_edges.append(cur_edge)
        cost += cur_edge.cost
        
        add_to_queue(graph, node_list, mst_edges, cost, cur_node, pq)
        #print(pq)

    #print(mst_edges)
    print(cost)

prims(adj_matrix, num_nodes, node_list, pre_switches, switches, post_switches)