from node import Node
class NodeNeighbors:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, node=Node(), cost=0):
        self.node = node
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
        if self.cost == other.cost:
            return True
        else:
            return False
        
    


    def __repr__(self) -> str:
        return f"({self.node.label}, {self.cost})"

    

