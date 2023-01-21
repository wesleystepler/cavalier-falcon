
class Node:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, label="", status="Unknown", type="", index=0, neighbors=[], which_switch = "", cost=0) -> None:
        possible_statuses = ["Unvisited", "Queued", "Visited"]
        self.label = label
        self.status = status
        self.type = type
        self.neighbors = neighbors
        self.index = index
        self.which_switch = which_switch
        self.cost = cost

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
        return f"Label: {self.label} Status: {self.status} Type: {self.type} Which Switch: {self.which_switch}\n"