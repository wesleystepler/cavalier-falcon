class Course():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name="", cap=0):
        self.name = name
        self.cap = cap

    def __repr__(self):
        return f"{self.name}. Capacity: {self.cap}"


class Registration():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, student="", course=""):
        self.student = student
        self.course = course

    def __repr__(self):
        return f"{self.student} wants to enroll in {self.course}"
