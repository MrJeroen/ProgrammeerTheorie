import numpy as np
import csv
import itertools
from base import *
from main import courses, students, room_list
# from algoritme1 import lessons
from list import *
from collections import Counter


traverser = 0
room = 0
score = 1000
#
# for i in range(7):
#     j = 0
#     for j in range(5):
#         k = 0
#         for k in range(4):
#             if int(array[j][k][i][0].seats) < int(array[j][k][i][1].amount):
#                 score += (int(array[j][k][i][0].seats) - int(array[j][k][i][1].amount))
#
# for vakken in students:
#     overlap = []
#     for room in range(7):
#         days = 0
#         for days in range(5):
#             time = 0
#             for time in range(4):
#                 # Get first element of object.lessong
#                 if vakken.vak1 == array[days][time][room][1].name:
#                     overlap.append((time, days))
#                 if vakken.vak2 == array[days][time][room][1].name:
#                     overlap.append((time, days))
#                 if vakken.vak3 == array[days][time][room][1].name:
#                     overlap.append((time, days))
#                 if vakken.vak4 == array[days][time][room][1].name:
#                     overlap.append((time, days))
#                 if vakken.vak5 == array[days][time][room][1].name:
#                     overlap.append((time, days))
#     something = [[x,overlap.count(x)] for x in set(overlap)]
#     for elements in something:
#         if elements[1] > 1:
#             score -= elements[1]

# Set counters
day = 0
room = 0
time = 0

for elements in (courses):
# When working, remove last item (empty classes dont count)
# for elements in (courses[:-1]):
    verdeling = []
    # Function, returns total activities
    totaal_vak = elements.totaal_activiteiten()
    # Traverse array
    for day in range(5):
        room = 0
        hc_count = 0
        wc_count = 0
        for room in range(7):
            time = 0
            for time in range(4):
                if elements.name == array[day][time][room][1].name:
                    # Function, returns activity type
                    type_vak = elements.type_activiteit()
                    # print type_vak
                    # print elements.hc
                    if type_vak == array[day][time][room][1].group_name:
                        # For the first encounter don't append
                        hc_count += 1
                        # print hc_count
                        # After second encounter, append
                        if hc_count > 1:
                            verdeling.append(day)
        # Combination between double hc + pr, hc + wc, wc + pr.. also counts...                      
                    # if type_vak != array[day][time][room][1].group_name:
                    #     wc_count =+ 1
                    #     if wc_count > 1:
                    #         verdeling.append(day)

                    # print array[day][time][room][1].name
                    # print array[day][time][room][1].group_name

    print verdeling
    # Count the total extra occurences of a given name
    check = len(Counter(verdeling).values())
    # print check
    score -= ((totaal_vak - check) * 10)

print score
