import csv
from base import Courses, Students, Lessons, Room

courses = []
lessons = []
students = []

# open the file courses to fill the Courses object
with open("vakken.csv", "rb") as file1:
    reader_vak = csv.reader(file1, delimiter=",")
    for vakken in reader_vak:
        # fill the courses array with courses objects
        courses.append(Courses(vakken[0], vakken[1], vakken[2],
        vakken[3], vakken[4], vakken[5], vakken[6]))
# i = 0
# for elements in courses:
#     print courses[i].name
#     print courses[i].hc
#     print courses[i].wc
#     print courses[i].pr
#     i += 1

# create a new list of objects from the list of course objects
for elements in courses:
    i = 1
    for hc in range(int(elements.hc)):
        lessons.append(Lessons(elements.name, "hc", elements.students, i))
        i += 1
    i = 1
    for wc in range(int(elements.wc)):
        lessons.append(Lessons(elements.name, "wc", elements.wc_students, i))
        i += 1
    i = 1
    for pr in range(int(elements.pr)):
        lessons.append(Lessons(elements.name, "pr", elements.pr_students, i))
        i += 1
#
# i = 0
# for elements in lessons:
#     print lessons[i].name
#     print lessons[i].group_name
#     print lessons[i].sort
#     print lessons[i].amount
#     i += 1

# open the student file to make student objects
with open("studenten.csv", "rb") as file2:
    reader_stud = csv.reader(file2, delimiter=",")
    for student in reader_stud:
        # append the student objects to a student array
            students.append(Students(student[2], student[3], student[4],
            student[5], student[6], student[7]))

# i = 0
# for elements in students:
#     print students[i].id
#     print students[i].vak1
#     i += 1

big_list = []
rest = []
for lesson in lessons:
    if int(lesson.amount) > 43:
        big_list.append(lesson)
    else:
        rest.append(lesson)

lessons = []
lessons = big_list + rest

room1 = Room('C0.110', 117)
room2 = Room('C1.112', 60)
room3 = Room('A1.10', 56)
room4 = Room('B0.201', 48)
room5 = Room('A10.4', 41)
room6 = Room('A1.06', 22)
room7 = Room('A1.08', 20)

room_list = {0 : room1, 1 : room2, 2 : room3, 3 : room4,
            4 : room5, 5 : room6, 6 : room7}
