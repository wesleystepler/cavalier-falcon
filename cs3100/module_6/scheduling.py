nums = [int(i) for i in input().split() if i.isdigit()]
r = nums[0] # Number of registration requests
c = nums[1] # Number of total available courses
n = nums[2] # Number of courses each student needs to enroll in

# Parse input
index_tracker = {} # Track what students/courses etc. are at each index
reqs_tracker = {} # Track the classes students what to take, and the class capacities
capacities = {}

enrolled = {} # Track the number of courses each student is enrolled in - used later
index = 0

# Source: https://note.nkmk.me/en/python-dict-get-key-from-value/
def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None

for i in range(0, r):
    s = input().split()
    if s[0] not in index_tracker.values():
        index_tracker[index] = s[0]
        index += 1


    if reqs_tracker.get(s[0]) == None:
        reqs_tracker[s[0]] = []
        reqs_tracker[s[0]].append(s[1])
    else:
        reqs_tracker[s[0]].append(s[1])

num_students = len(index_tracker)
    
for i in range(0, c):
    s = input().split()
    if s[0] not in index_tracker.values():
        index_tracker[index] = s[0]
        index += 1

    if reqs_tracker.get(s[0]) == None:
        reqs_tracker[s[0]] = s[1]

    ind = get_key_from_value(index_tracker, s[0])
    capacities[ind] = int(s[1])

num_courses = len(index_tracker) - num_students

index_tracker[len(index_tracker)] = "Source"
index_tracker[len(index_tracker)] = "Sink"

#print(index_tracker)
#print(reqs_tracker)
#print(capacities)


# Use input to construct graph, stored in an adjacency matrix.
# In the Adj Matrix (both rows and columns):
# The students will always be listed first, followed by the courses, followed by the source and sink node
# So the sink node will always be graph[-1], and source will always be graph[-2]

graph = []
for i in range(0, len(index_tracker)):
    graph.append([0]*len(index_tracker))

for i in range(0, num_students):
    for j in range(num_students, num_students+num_courses):
        if index_tracker[j] in reqs_tracker[index_tracker[i]]:
            graph[i][j] = 1

for i in range(num_students, num_students+num_courses):
    graph[i][-1] = int(reqs_tracker[index_tracker[i]])

for j in range(0, num_students):
    graph[-2][j] = n
    
    
for row in graph:
    print(row)

#print(num_students)
#print(num_courses)

# Implement Ford-Fulkerson
# All augmenting paths will have this form:
# Source --> Student --> Class --> Sink
is_path = True
def dfs(start, end, visited, num_students, num_courses, capacities):
    global graph
    global is_path
    path = ""
    stack = []
    stack.append(start)
    while len(stack) > 0:
        i = stack[-1]
        stack.remove(stack[-1])
        path += f"{i}-"
        if i == end:
            is_path = True
            break
        visited.append(i)
        s = 0
        if i >= num_students and i < num_courses + num_students:
            s = num_students + num_courses
        elif i < num_students:
            s = num_students
        for j in range(s, len(graph[i])):
            if j >= num_students and j <= num_students + num_courses:
                if j not in visited and graph[i][j] != 0 and graph[j][len(graph)-1] != 0:
                    graph[i][j] -= 1
                    graph[j][i] += 1

                    stack.append(j)
                    break
            else:
                if j not in visited and graph[i][j] != 0:
                    graph[i][j] -= 1
                    graph[j][i] += 1

                    stack.append(j)
                    break

reqs_fulfilled = 0
while is_path:
    is_path = False
    dfs(len(graph)-2, len(graph)-1, [], num_students, num_courses, capacities)
    if is_path:
        reqs_fulfilled += 1

all_zeroes = True
row = len(graph)-2
for i in range(0, len(graph[row])):
    if graph[row][i] != 0:
        all_zeroes = False
        break
if reqs_fulfilled == num_students*n and not all_zeroes:
    print("Yes")
else:
    print("No")
for row in graph:
    print(row)

#print(num_students)
#print(num_courses)










