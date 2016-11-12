import csv
from base import Courses, Students, Lessons

courses = []
lessons = []
students = []
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
                if vakken[0] in student[3]:
                    course_students.append(student[2])
        # fill the courses array with courses objects
        courses.append(Courses(vakken[0], vakken[1], vakken[2],
        vakken[3], vakken[4], vakken[5], course_students))
# i = 0
# for elements in courses:
#     print courses[i].name
#     print courses[i].hc
#     print courses[i].students
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
    i =1
    for pr in range(int(elements.pr)):
        lessons.append(Lessons(elements.name, "pr", elements.pr_students, i))
        i += 1

# i = 0
# for elements in lessons:
#     print lessons[i].name
#     print lessons[i].sort
#     print lessons[i].students
#     print lessons[i].group
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
