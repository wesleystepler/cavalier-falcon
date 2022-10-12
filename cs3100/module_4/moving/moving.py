#NOTE: Python rounds down for integer division, so you will need to add 1 when you get to that point
from shipping import Shipping
from shipping import OptimalShipping
import math

def best_shipping(company, box_ship, box_take):
    cost = 0
    if company.cost_half == 0 or company.cost_one == 0:
        result = OptimalShipping(company.name, 0)
        return result
    while box_ship > box_take:
        # On each pass, we want the option that packs the most boxes for least cost
        
        box_half = math.ceil(box_ship/2)
    
        ship_half = company.cost_half/box_half
        ship_one = company.cost_one/1
        if ship_half < ship_one and box_ship - box_half > box_take:
            cost += company.cost_half
            box_ship -= box_half
        else:
            cost += company.cost_one
            box_ship -= 1

    result = OptimalShipping(company.name, cost)
    return result



test_cases = input()
for j in range(0, int(test_cases)):
    data = [int(i) for i in input().split() if i.isdigit()]
    box_move, box_take, companies = data[0], data[1], data[2]
    #box_ship = box_move - box_take

    shipping_list = []
    for i in range(0, companies):
        data = input().split()
        s = Shipping(data[0], int(data[1]), int(data[2]))
        shipping_list.append(s)

    shipping_cost = []
    for i in range(0, len(shipping_list)):
        shipping_cost.append(best_shipping(shipping_list[i], box_move, box_take))

    shipping_cost.sort()
    print(f"Case {j+1}")
    for i in range(0, len(shipping_cost)):
        print(shipping_cost[i])

            
# Services with larger half costs are returning bigger numbers than they should
# Services with larger one costs are returning smaller numbers than they should
    




