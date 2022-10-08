#NOTE: Python rounds down for integer division, so you will need to add 1 when you get to that point
from shipping import Shipping
#test_cases = input()

"""data = [int(i) for i in input().split() if i.isdigit()]
box_move, box_take, companies = data[0], data[1], data[2]
box_ship = box_move - box_take

shipping_list = []
for i in range(0, companies):
    data = input().split()
    s = Shipping(data[0], data[1], data[2])
    shipping_list.append(s)"""


def best_shipping(company, box_ship):
    cost = 0
    while box_ship > 0:
        box_half = int(box_ship/2) + 1
        ship_half = box_half/company.cost_half
        ship_one = company.cost_one/1
        if ship_half > ship_one:
            cost += company.cost_half
            box_ship -= box_half
        else:
            cost += company.cost_one
            box_ship -= 1
    cost += company.cost_one
    return cost

c = Shipping("UHAUL", 3, 2)
print(best_shipping(c, 65))
            



    




