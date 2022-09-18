class Node:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, label="", status="Unvisited", dist=0, path="") -> None:
        possible_statuses = ["Unvisited", "Queued", "Visited"]
        self.label = label
        self.status = status
        self.dist = dist
        self.path = path

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
        return f"Label: {self.label}\n Status: {self.status} \n Dist: {self.dist} \n Path: {self.path}"