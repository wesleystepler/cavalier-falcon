from room import Room
import math

# Greedy choice for the growing rooms: pick the original room size that has the biggest upgrade

rooms = []
for i in range(0,2):
    num_rooms = int(input())
    for i in range(0, num_rooms):
        cap = input().split()
        room = Room(f"Room {i+1}", int(cap[0]), int(cap[1]))
        rooms.append(room)

    max_diff = 0
    max_old = 0
    cost = 0
    for room in rooms:
        diff = room.new_max - room.old_max
        if diff > max_diff:
            max_diff = diff
            cost = room.old_max
        if room.old_max > max_old:
            max_old = room.old_max
    rooms.clear()
    if max_diff >= max_old:
        print(cost)
    elif max_diff < 0:
        print(max_old)
    else:
        print(max_old)



"""
Strategy:
Process input in this order:
    Rooms that are growing in size
    Rooms that stay the same size
    Rooms that shrink in size
Sample case:
4
6 6
1 7
3 5
3 5

This would then be ordered:
    1 7
    3 5
    3 5
    6 6
"""