import numpy as np
import csv
import itertools
from base import Courses, Students, Lessons
from main import courses, students, room_list
from algoritme1 import lessons
from list import array
from collections import Counter


traverser = 0
room = 0
score = 1000

for i in range(7):
    j = 0
    for j in range(5):
        k = 0
        for k in range(4):
            if int(array[j][k][i][0].seats) < int(array[j][k][i][1].amount):
                score += (int(array[j][k][i][0].seats) - int(array[j][k][i][1].amount))

# for days in range(5):
#     time = 0
#     for time in range(4):
#         room = 0
#         for room in range(7):
#             for room_comp in range(7):
#                 if room != room_comp:
#                     if array[days][time][room][1].name = array[days][time][room_comp][1].name:


vak_student = ['vak1', 'vak2', 'vak3', 'vak4', 'vak5']
for vakken in students:
    overlap = []
    for room in range(7):
        days = 0
        for days in range(5):
            time = 0
            for time in range(4):
                if vakken.vak1 == array[days][time][room][1].name:
                    overlap.append((time, days))
                if vakken.vak2 == array[days][time][room][1].name:
                    overlap.append((time, days))
                if vakken.vak3 == array[days][time][room][1].name:
                    overlap.append((time, days))
                if vakken.vak4 == array[days][time][room][1].name:
                    overlap.append((time, days))
                if vakken.vak5 == array[days][time][room][1].name:
                    overlap.append((time, days))
    something = [[x,overlap.count(x)] for x in set(overlap)]
    for elements in something:
        if elements[1] > 1:
            score -= elements[1]

print score
