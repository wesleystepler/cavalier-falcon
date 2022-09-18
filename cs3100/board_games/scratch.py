from node import Node

x = Node(label="3")
y = Node(label="2")
z = Node(label="7")

node_list = [x,y,z]



num_nodes = int(input())
num_edges = int(input())
p = []
for i in range(0, num_edges):
    nums = [int(i) for i in input().split() if i.isdigit()]
    p.append(nums)


print(p)