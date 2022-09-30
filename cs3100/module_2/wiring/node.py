class Node:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, label="", known=False, type="", index=0, neighbors=[]) -> None:
        possible_statuses = ["Unvisited", "Queued", "Visited"]
        self.label = label
        self.known = known
        self.type = type
        self.neighbors = neighbors
        self.index = index

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
        return f"Label: {self.label} Status: {self.status} Type: {self.type}\n"