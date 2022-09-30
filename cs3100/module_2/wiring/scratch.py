from node import Node
from node_edge import NodeEdge

node1 = Node()
node2 = Node()

node3 = Node()
node4 = Node()

ne1 = NodeEdge(node1, node2, 5)
ne2 = NodeEdge(node3, node4, 3)

l = [ne1, ne2]
print(min(l))