class Room():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name="", old_max=0, new_max=0):
        self.name = name
        self.old_max = old_max
        self.new_max = new_max
        self.diff = new_max - old_max

    def __gt__(self, other):
        if self.new_max > other.new_max:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.new_max < other.new_max:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.name}, {self.old_max} --> {self.new_max}"