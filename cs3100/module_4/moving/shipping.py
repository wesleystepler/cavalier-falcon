class Shipping():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, company="", cost_one=0, cost_half =0):
        self.company = company
        self.cost_one = cost_one
        self.cost_half = cost_half


    def __repr__(self):
        return f"{self.company}, Ship one box for ${self.cost_one}, half the boxes for ${self.cost_half}"
