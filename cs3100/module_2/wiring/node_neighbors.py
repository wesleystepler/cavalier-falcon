from node import Node
class NodeNeighbors:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, node=Node(), node2 = Node(), cost=0):
        self.node = node
        self.node2 = node2
        self.cost = cost

    def __gt__(self, other):
        if self.cost > other.cost:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.node == other.node and self.node2 == other.node2 or self.node == other.node2 and self.node2 == other.node:
            return True
        else:
            return False
        
    


    def __repr__(self) -> str:
        return f"({self.node.label}, {self.node2.label}, {self.cost})"

    

