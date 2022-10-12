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

def closest_points(point_list: "list[tuple]"):
    point_list.sort()
    
