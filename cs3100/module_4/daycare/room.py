class Room():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name="", old_max=0, new_max=0):
        self.name = name
        self.old_max = old_max
        self.new_max = new_max

    def __repr__(self):
        return f"{self.name}, {self.old_max} --> {self.new_max}"