from room import Room
import math

# Greedy choice for the growing rooms: pick the original room size that has the biggest upgrade
# Greedy choice for staying the same size: pick the largest room
# Greedy choice for all shrinking: largest original size 

rooms = []

increasing = []
same = []
decreasing = []


for i in range(0,2):
    num_rooms = int(input())
    for i in range(0, num_rooms):
        cap = input().split()
        room = Room(f"Room {i+1}", int(cap[0]), int(cap[1]))
        rooms.append(room)
        if room.new_max - room.old_max > 0:
            increasing.append(room)
        elif room.new_max - room.old_max < 0:
            decreasing.append(room)
        else:
            same.append(room)

    max_diff = 0
    r = Room()

    if len(increasing) == 0 and len(same) == 0 and len(decreasing) > 0:
        #decreasing.sort()
        solution = 0
        for i in range(0, len(decreasing)):
            if decreasing[i].old_max > solution:
                solution = decreasing[i].old_max

        for i in range(1, len(decreasing)):
            solution += (abs(decreasing[i].new_max - decreasing[i].old_max))
        print(solution)
        
    elif len(increasing) == 0 and len(same) == 0 and len(decreasing) == 0:
        solution = 0
        for i in range(0, len(rooms)):
            solution += rooms[i].old_max
        print(solution)
    else:
        for i in range(0, len(increasing)):
            diff = increasing[i].new_max - increasing[i].old_max
            if diff > max_diff:
                max_diff = diff
                r = increasing[i]
            elif diff == max_diff:
                if increasing[i].old_max < r.old_max:
                    r = increasing[i]

        for i in range(0, len(same)):
            if same[i].old_max > max_diff:
                max_diff = same[i].old_max
                r = same[i]
            elif same[i].old_max == max_diff:
                if same[i].old_max < r.old_max:
                    r = same[i]


        for i in range(0, len(decreasing)):
            diff = decreasing[i].old_max - decreasing[i].new_max 
            if diff > max_diff:
                max_diff = decreasing[i].old_max
                r = decreasing[i]
            elif diff == max_diff:
                if decreasing[i].old_max < r.old_max:
                    r = same[i]

        print(r.old_max)
        
    increasing.clear()
    same.clear()
    decreasing.clear()
