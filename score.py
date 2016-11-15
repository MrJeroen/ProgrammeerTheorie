import numpy as np
import csv
import itertools
from base import Courses, Students, Lessons
from main import courses, students, room_list
from algoritme1 import lessons
from list import array


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

for days in range(5):
    time = 0
    for time in range(4):
        room = 0
        for room in range(7):
            for room_comp in range(7):
                if room != room_comp:
                    if array[days][time][room][1].name = array[days][time][room_comp][1].name:







print score
#print array[0][0][0][0].seats
