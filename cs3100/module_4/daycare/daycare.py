from ssl import DER_cert_to_PEM_cert
from room import Room

# Greedy choice for the growing rooms: pick the old capacity of the room with the largest new capacity
# Greedy choice for staying the same size: pick the largest room
# Greedy choice for all shrinking: Pick room with largest new size first. 

"""def sort_by_old_max(room_list):
    room_sizes = []
    sorted_list = []
    for i in range(0, len(room_list)):
        room_sizes.append(room_list[i].old_max)
    room_sizes.sort()
    for size in room_sizes:
        for i in range(0, len(room_list)):
            if room_list[i].old_max == size:
                sorted_list.append(room_list[i])
                break
    return sorted_list"""


# Where I stopped: working on getting the code to properly handle when all rooms decrease.
# General idea is to iterate through, and if at any point all rooms and the trailer are full, add
# to the total capacity needed for the trailer. 
def handle_decrease(decreasing):
    trailer = 0
    new_cap = 0
    new_max = 0


    for i in range(0, len(decreasing)):
        # Relocate all the kids to where they need to go
        while decreasing[i].old_max > 0:
            decreasing[i].old_max -= 1
            if new_max > 0 and new_cap < new_max:
                new_cap += 1
            else:
                trailer += 1
        new_max += decreasing[i].new_max
        while new_cap < new_max and trailer > 0:
            trailer -= 1
            new_cap += 1
    return trailer

def handle_increase(increasing):
    max_diff = 0
    room = Room()
    for i in range(0, len(increasing)):
        if increasing[i].new_max - increasing[i].old_max > max_diff:
            max_diff = (increasing[i].new_max - increasing[i].old_max)
            room = increasing[i]
    return room.old_max


def handle_same(same):
    max_size = 0
    for i in range(0, len(same)):
        if same[i].old_max > max_size:
            max_size = same[i].old_max
    return max_size

        

rooms = []

increasing = []
same = []
decreasing = []
solution = 0

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

    increasing.sort(reverse=True)
    same.sort()
    decreasing.sort(reverse=True)


    results = []
    if len(increasing) > 0:
        i = handle_increase(increasing)
        results.append(i)
    if len(same) > 0:
        s = handle_same(same)
        results.append(s)
    if len(decreasing) > 0:
       d = handle_decrease(decreasing)
       results.append(d)

    # Need to handle case where two maxes are the same so that it picks the smaller starting
    # trailer size, not the bigger one. 
    print(max(results))

    increasing.clear()
    same.clear()
    decreasing.clear()

    




