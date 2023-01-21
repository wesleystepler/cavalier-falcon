class Shipping():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name="", cost_one=0, cost_half =0):
        self.name = name
        self.cost_one = cost_one
        self.cost_half = cost_half


    def __repr__(self):
        return f"{self.company}"


class OptimalShipping():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, company="", cost=0):
        self.company = company
        self.cost = cost

    def __gt__(self, other):
        if self.cost > other.cost:
            return True
        elif self.cost == other.cost:
            if self.company > other.company:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        elif self.cost == other.cost:
            if self.company < other.company:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.cost == other.cost:
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.company} {self.cost}"
