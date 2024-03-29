from room import Room

# Greedy choice for the growing rooms: pick the smallest old room
# Greedy choice for staying the same size: pick the largest room
# Greedy choice for all shrinking: Pick room with largest new size first. 

def sort_by_old_max(room_list):
    room_sizes = []
    sorted_list = []

    for i in range(0, len(room_list)):
        room_sizes.append(room_list[i].old_max)

    room_sizes.sort()
    for size in room_sizes:
        i = 0
        while len(room_list) > 0:
            if room_list[i].old_max == size:
                sorted_list.append(room_list[i])
                room_list.remove(room_list[i])
                break
            i += 1
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
      
rooms = []
increasing = []
same = []
decreasing = []

for i in range(0,2):
    num_rooms = int(input())
    for i in range(0, num_rooms):
        cap = input().split()
        room = Room(f"Room {chr(65+i)}", int(cap[0]), int(cap[1]))
        rooms.append(room)
        if room.new_max - room.old_max > 0:
            increasing.append(room)
        elif room.new_max - room.old_max < 0:
            decreasing.append(room)
        else:
            same.append(room)

    increasing = sort_by_old_max(increasing)
    same.sort()
    decreasing.sort(reverse=True)

    sorted_list = []
    for j in range(0, len(increasing)):
        sorted_list.append(increasing[j])

    for j in range(0, len(same)):
        sorted_list.append(same[j])

    for j in range(0, len(decreasing)):
        sorted_list.append(decreasing[j])

    print(handle_moving(sorted_list))

    increasing.clear()
    same.clear()
    decreasing.clear()
