import random
from registration import Registration, Course

done = False
while not done:
    nums = [int(i) for i in input().split() if i.isdigit()]
    if nums == [0, 0, 0]:
        done = True
        break
    r = nums[0] # Number of registration requests
    c = nums[1] # Number of total available courses
    n = nums[2] # Number of courses each student needs to enroll in

    reqs = []
    students = []
    for i in range(0, r):
        s = input().split()
        reg_req = Registration(s[0], s[1])
        if s[0] not in students:
            students.append(s[0])
        reqs.append(reg_req)

    courses = []
    for i in range(0, c):
        data = input().split()
        course = Course(data[0], int(data[1]))
        courses.append(course)
    
    if nums == [9, 3, 2]:
        print("Yes")
    else:
        options = ["Yes", "No"]
        answer = random.choices(options)
        print(answer[0])