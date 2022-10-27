from room import Room

# Greedy choice for the growing rooms: pick the old capacity of the room with the largest new capacity
# Greedy choice for staying the same size: pick the largest room
# Greedy choice for all shrinking: Pick room with largest new size first. 

def sort_by_old_max(room_list):
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
    return sorted_list


def handle_moving(room_list):
    trailer = 0
    trailer_max = 0
    new_cap = 0
    new_max = 0

    for i in range(0, len(room_list)):
        # Relocate all the kids to where they need to go
        while room_list[i].old_max > 0:
            room_list[i].old_max -= 1
            if new_max > 0 and new_cap < new_max:
                new_cap += 1
            else:
                trailer += 1
                if trailer > trailer_max:
                    trailer_max = trailer
        new_max += room_list[i].new_max
        while new_cap < new_max and trailer > 0:
            trailer -= 1
            new_cap += 1
    return trailer_max

def handle_increase(increasing):
    max_new = 0
    room = Room()
    for i in range(0, len(increasing)):
        if increasing[i].max_new > max_new:
            max_new = increasing[i].max_new
    return max_new
        


def handle_same(same):
    max_size = 0
    room = Room()
    for i in range(0, len(same)):
        if same[i].old_max > max_size:
            max_size = same[i].old_max
            room = same[i]
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
    #print(increasing)
    same.sort()
    decreasing.sort(reverse=True)


    sorted_list = []
    for j in range(0, len(increasing)):
        sorted_list.append(increasing[j])

    for j in range(0, len(same)):
        sorted_list.append(same[j])

    for j in range(0, len(decreasing)):
        sorted_list.append(decreasing[j])
    
    """if len(increasing) > 0:
        print(increasing[0].old_max)

    if len(same) > 0:
        s = handle_same(same)
        results.append(s)
    if len(decreasing) > 0:
       d = handle_moving(decreasing)
       results.append(d)"""

    print(handle_moving(sorted_list))

    increasing.clear()
    same.clear()
    decreasing.clear()

    




