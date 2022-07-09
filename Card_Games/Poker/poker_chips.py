class Chip:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, color):
        self.color = ""
        self.value = 0
        valid_colors = ["W", "R", "B", "G"]
        if color in valid_colors:
            self.color = color
        else:
            raise Exception("Invalid Chip Color")

        if self.color == "W":
            self.value = 1
        elif self.color == "R":
            self.value = 5
        elif self.color == "B":
            self.value = 10
        elif self.color == "G":
            self.value == 25


    def __repr__(self):
        return f"{self.color}"
