class Map():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, label="", grid=[]):
        self.label = label
        self.grid = grid

    