import urllib.request
COURSE_TITLE = 3  # The index of the course title
INSTRUCTOR = 4  # The index of the instructor
CLASS_TYPE = 5  # Index of the type of class (Lecture, Lab, etc. )
START_TIME = 12
END_TIME = 13

def instructor_lectures(department, instructor):
    global COURSE_TITLE
    global INSTRUCTOR
    global CLASS_TPYE

    link = "http://cs1110.cs.virginia.edu/files/louslist/" + department
    stream = urllib.request.urlopen(link)
    instructor_list = []
    x = stream.readlines()
    course_list = []
    for line in x:
        current_course = line.decode("UTF-8").split("|")
        print("Current Course: ", current_course)
        if instructor in current_course[INSTRUCTOR] and current_course[CLASS_TYPE] == "Lecture" and current_course[COURSE_TITLE] not in instructor_list:
            instructor_list.append(current_course[COURSE_TITLE])
    
    return instructor_list

print(instructor_lectures('STS', 'Kathryn Neeley'))

  


def compatiable_classes(first_class, second_class, needs_open_space=False):
    global START_TIME
    global END_TIME

    x = first_class.split(" ")
    x[1] = x[1].split("-")

    y = second_class.split(" ")
    y[1] = y[1].split("-")

    return x, y

    link = "http://cs1110.cs.virginia.edu/files/louslist/CS"
    stream = urllib.request.urlopen(link)
    x = stream.readlines()
    for line in x:
        current_course = line.decode("UTF-8".split("|"))


print(compatiable_classes("CS 1110-001", "CS 2150-001"))

        



