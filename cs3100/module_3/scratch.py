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

def min_points(p_list):
    if len(p_list) < 3:
        return p_list
    else:
        median = int(len(p_list)/2)
        l = p_list[0:median]
        r = p_list[median:len(p_list)]
        #print(l)
        #print(r)
        min_points(l)
        min_points(r)

    
        
test = [4,5,2,7,3,7,3]
test.sort()
print(min_points(test))