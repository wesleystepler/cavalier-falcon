class Node:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, label=1000000000000, status="Unvisited") -> None:
        possible_statuses = ["Unvisited", "Queued", "Visited"]
        self.label = label
        self.status = status

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
        return f"Label: {self.label}\n Status: {self.status}"