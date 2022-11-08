nums = [int(i) for i in input().split() if i.isdigit()]
r = nums[0] # Number of registration requests
c = nums[1] # Number of total available courses
n = nums[2] # Number of courses each student needs to enroll in

# Parse input
index_tracker = {}

reqs_tracker = {}
index = 0

for i in range(0, r):
    s = input().split()
    #if index_tracker.get(s[0]) == None:
    #    index_tracker[s[0]] = index
    #    index += 1
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
    #if index_tracker.get(s[0]) == None:
    #    index_tracker[s[0]] = index
    #    index += 1
    if s[0] not in index_tracker.values():
        index_tracker[index] = s[0]
        index += 1

    if reqs_tracker.get(s[0]) == None:
        reqs_tracker[s[0]] = s[1]

num_courses = len(index_tracker) - num_students

#index_tracker["Source"] = len(index_tracker)
#index_tracker["Sink"] = len(index_tracker)

index_tracker[len(index_tracker)] = "Source"
index_tracker[len(index_tracker)] = "Sink"

print(index_tracker)
print(reqs_tracker)


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

print(num_students)
print(num_courses)
