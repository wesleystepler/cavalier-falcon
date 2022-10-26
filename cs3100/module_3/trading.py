p_list = []
take_input = True
while take_input:
    num_points = int(input())
    if num_points == 0:
        break
    p = []
    for i in range(0, num_points):
        x_y = input().split()
        x, y = 0, 0
        if x_y[0].isdigit() or x_y[0].lstrip("-").isdigit():
            x = int(x_y[0])
        else:
            x = float(x_y[0])

        if x_y[1].isdigit() or x_y[1].lstrip("-").isdigit():
            y = int(x_y[1])
        else:
            y = float(x_y[1])

        p.append((x, y))
    p_list.append(p)

#for list in p_list:
#    print(list)

def distance(p1, p2):
    import math
    t1 = (p2[0] - p1[0])**2
    t2 = (p2[1] - p1[1])**2
    dist = math.sqrt(t1 + t2)
    return dist

def brute_force(point_list):
    # Test points: (1,3), (4,2), (5,2)
    result = distance(point_list[0], point_list[1])
    return result



def closest_points(point_list: "list[tuple]"):
    point_list.sort()

