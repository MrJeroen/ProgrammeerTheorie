import csv
from base import Courses, Students, Lessons, Room

courses = []
vak = [3, 4, 5, 6, 7]
# open the file courses to fill the Courses object
with open("vakken.csv", "rb") as file1:
    reader_vak = csv.reader(file1, delimiter=",")
    for vakken in reader_vak:
        # create an array for all the students in one course
        course_students = []
        with open("studenten.csv", "rb") as file2:
            reader_stud = csv.reader(file2, delimiter=",")
            for student in reader_stud:
                # is students attened a course add them to the array
                for verschillende in vak:
                    if vakken[0] in student[verschillende]:
                        course_students.append(student[2])
        # fill the courses array with courses objects
        courses.append(Courses(vakken[0], vakken[1], vakken[2],
        vakken[3], vakken[4], vakken[5], vakken[6], course_students))

# for elements in courses:
#     print elements.total()
#     print elements.hc
#     print elements.students
#     print len(elements.student_numbers)

lessons = []
# create a new list of objects from the list of course objects
for elements in courses:
    i = 1
    for hc in range(int(elements.hc)):
        lessons.append(Lessons(elements.name, "hc", elements.students, i, elements.student_numbers))
        i += 1
    i = 1
    student_numbers = []
    for wc in range(int(elements.wc)):
        if i == 1:
            student_numbers = elements.student_numbers[:int(elements.wc_students)]
        if i == 2:
            student_numbers = elements.student_numbers[int(elements.wc_students): 2 * int(elements.wc_students)]
        if i == 3:
            student_numbers = elements.student_numbers[2 * int(elements.wc_students): 3 * int(elements.wc_students)]
        if i == 4:
            student_numbers = elements.student_numbers[3 * int(elements.wc_students):]
        lessons.append(Lessons(elements.name, "wc", elements.wc_students, i, student_numbers))
        i += 1
    i = 1
    student_numbers = []
    for pr in range(int(elements.pr)):
        if i == 1:
            student_numbers = elements.student_numbers[:int(elements.pr_students)]
        if i == 2:
            student_numbers = elements.student_numbers[int(elements.pr_students): 2 * int(elements.pr_students)]
        if i == 3:
            student_numbers = elements.student_numbers[2 * int(elements.pr_students): 3 * int(elements.pr_students)]
        if i == 4:
            student_numbers = elements.student_numbers[3 * int(elements.pr_students):]
        lessons.append(Lessons(elements.name, "pr", elements.pr_students, i, student_numbers))
        i += 1

big_list = []
rest = []
for lesson in lessons:
    if int(lesson.amount) > 43:
        big_list.append(lesson)
    else:
        rest.append(lesson)

lessons = []
lessons = big_list + rest

# for elements in lessons:
#     print elements.name
#     print elements.group_name
#     print elements.sort
#     print elements.amount
#     print elements.students

students = []
# open the student file to make student objects
with open("studenten.csv", "rb") as file2:
    reader_stud = csv.reader(file2, delimiter=",")
    for student in reader_stud:
        # append the student objects to a student array
            students.append(Students(student[2], student[3], student[4],
            student[5], student[6], student[7]))

# for elements in students:
#     print elementss.id
#     print elements.vak1


room1 = Room('C0.110', 117)
room2 = Room('C1.112', 60)
room3 = Room('A1.10', 56)
room4 = Room('B0.201', 48)
room5 = Room('A10.4', 41)
room6 = Room('A1.06', 22)
room7 = Room('A1.08', 20)

room_list = {0 : room1, 1 : room2, 2 : room3, 3 : room4,
            4 : room5, 5 : room6, 6 : room7}
