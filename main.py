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
                # If a student atteneds a course, add them to the array
                for verschillende in vak:
                    if vakken[0] in student[verschillende]:
                        course_students.append(student[2])
        # fill the courses array with courses objects
        courses.append(Courses(vakken[0], vakken[1], vakken[2],
        vakken[3], vakken[4], vakken[5], vakken[6], course_students))

# create a new list of objects from the list of course objects
lessons = []
# Iterate over the list with courses
for elements in courses:
    # Create all the "hoorcollege" lessons
    for hc in range(int(elements.hc)):
        lessons.append(Lessons(elements.name, "hc", elements.students, hc, elements.student_numbers))
    student_numbers = []
    # Create all the "werkcollege" lessons
    for wc in range(int(elements.wc)):
        if wc == 0:
            student_numbers = elements.student_numbers[:int(elements.wc_students)]
        elif wc == 1:
            student_numbers = elements.student_numbers[int(elements.wc_students): 2 * int(elements.wc_students)]
        elif wc == 2:
            student_numbers = elements.student_numbers[2 * int(elements.wc_students): 3 * int(elements.wc_students)]
        elif wc == 3:
            student_numbers = elements.student_numbers[3 * int(elements.wc_students):]
        lessons.append(Lessons(elements.name, "wc", elements.wc_students, wc, student_numbers))
    student_numbers = []
    # Create all the "practica" lessons
    for pr in range(int(elements.pr)):
        if pr == 0:
            student_numbers = elements.student_numbers[:int(elements.pr_students)]
        elif pr == 1:
            student_numbers = elements.student_numbers[int(elements.pr_students): 2 * int(elements.pr_students)]
        elif pr == 2:
            student_numbers = elements.student_numbers[2 * int(elements.pr_students): 3 * int(elements.pr_students)]
        elif pr == 3:
            student_numbers = elements.student_numbers[3 * int(elements.pr_students):]
        lessons.append(Lessons(elements.name, "pr", elements.pr_students, pr, student_numbers))

# Make three smaller lists of the list with lessons based on the amount of
# students per lesson.
# 0 - 19
big = []
# 20 - 59
medium = []
# 60 - 139
small = []
for lesson in lessons:
    if int(lesson.amount) > 43:
        big.append(lesson)
    elif 43 >= int(lesson.amount) and int(lesson.amount) > 20:
        medium.append(lesson)
        # print lesson.amount
    else:
        small.append(lesson)

lessons = []
lessons = big + medium + small

# Create a list of student objects.
students = []
# Open the student file to make student objects.
with open("studenten.csv", "rb") as file2:
    reader_stud = csv.reader(file2, delimiter=",")
    for student in reader_stud:
        # Append the student objects to a student array.
            students.append(Students(student[2], student[3], student[4],
            student[5], student[6], student[7]))

# Create the room objects
room1 = Room('C0.110', 117, 0, 0.0)
room2 = Room('C1.112', 60, 0, 0.0)
room3 = Room('A1.10', 56, 0, 0.0)
room4 = Room('B0.201', 48, 0, 0.0)
room5 = Room('A10.4', 41, 0, 0.0)
room6 = Room('A1.06', 22, 0, 0.0)
room7 = Room('A1.08', 20, 0, 0.0)

room_list = {0 : room1, 1 : room2, 2 : room3, 3 : room4,
            4 : room5, 5 : room6, 6 : room7}
