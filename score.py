import numpy as np
import csv
import itertools
from base import *
from main import courses, students, room_list, lessons
from list import Array
from algoritme1 import ShuffledList
from collections import Counter

list_return = []
list_highest = [-500]

def Score(array):
    traverser = 0
    room = 0
    score = 1000

    # Calculate if there are too many students in a room
    for i in range(7):
        j = 0
        for j in range(5):
            k = 0
            for k in range(4):
                if int(array[j][k][i][0].seats) < int(array[j][k][i][1].amount):
                    score += (int(array[j][k][i][0].seats) - int(array[j][k][i][1].amount))

    # Calculate if a student needs to attend > 1 class at a given time
    for ids in students:
        overlap = []
        for room in range(7):
            days = 0
            for days in range(5):
                time = 0
                for time in range(4):
                    if ids.id in array[days][time][room][1].students:
                        overlap.append((time, days))
        something = [[x,overlap.count(x)] for x in set(overlap)]
        for elements in something:
            if elements[1] > 1:
                score -= elements[1] - 1

    # For every unique course
    # courses[:-1] removes the 'empty courses'
    for elements in (courses[:-1]):
        # Generate strings for comparisons
        hc = 'hc'
        wc = 'wc'
        pr = 'pr'
        # Set day
        day = 0
        # Change range to 1 for a quicker overview
        for day in range(5):
            # List for every type of class
            list_hc = []
            list_wc = []
            list_pr = []
            # Initiate counters
            wc_count = 0
            pr_count = 0
            hc_count = 0
            room = 0
            time = 0
            overlap_count = 0
            # Reset room for every new day
            room = 0
            for room in range(7):
                # Reset time for every new room
                time = 0
                for time in range(4):
                    # If course matches (first) course in array
                    if elements.name == array[day][time][room][1].name:
                        # Determine if hc/wc/pr
                        type_activiteit = array[day][time][room][1].group_name

                        # For checking purposes
                        # print elements.name
                        # print type_activiteit

                        # Append each activity to a list
                        if type_activiteit == hc:
                            list_hc.append(day)
                        elif type_activiteit == wc:
                            list_wc.append(day)
                        elif type_activiteit == pr:
                            list_pr.append(day)

                        # If there is any item in list, update counter to 1
                        # Pr or wc is seen as 1 group (e.g. seen as only 1 entry)
                        # Thus counter for pr and wc does not exceed 1
                        # If list contains any item
                        if list_wc:
                            wc_count = 1
                        if list_pr:
                            pr_count = 1
                        # Every hc is considered 'unique' and thus counter is set
                        # to equate total entries (e.g. 3 HC's give a count of 3)
                        if list_hc:
                            hc_count = len(list_hc)
            # Option 1
            # When a hc_course is met for a second time
            if hc_count > 1:
                # Because of overlap, place in overlap list
                overlap_count += (hc_count - 1)
            # If either wc or pr is found (pr or wc counter = 1) then for
            if wc_count == 1 or pr_count == 1:
                # Every hc_class a 'collission' has happend (e.g. Hc with wc and/or pr)
                for i in range(hc_count):
                    if wc_count == 1:
                        overlap_count += 1
                    if pr_count == 1:
                        overlap_count += 1
                # If both a wc or pr is found, add one to overlap
                if wc_count == pr_count:
                    overlap_count += 1

            # option 2
            # Does NOT account for multiple collissons for every hc.
            # (e.g. 2 HC's DO NOT each collides with wc and/or pr)
            # overlap_count = hc_count + wc_count + pr_count

            # Calculate score based on total overlap with a maximum of 3
            if overlap_count >= 3:
                score -= 30
            elif overlap_count == 2:
                score -= 20
            elif overlap_count == 1:
                score -= 10

            # For checking purposes
            # print elements.name
            # print 'hc', list_hc
            # print 'hc', hc_count
            # print 'wc', list_wc
            # print 'wc', wc_count
            # print 'pr', list_pr
            # print 'pr', pr_count
            # print 'overlap', overlap_count

    return score

# put the shuffled list in to the Array function from list.py
array1 = Array(lessons)
# print Array(lessons)
print Score(array1)

# for i in range(1):
#     # Put list lessons from main.py in the shuffle function of algoritme1
#     lessons1 = ShuffledList(lessons)
#     # put the shuffled list in to the Array function from list.py
#     array1 = Array(lessons1)
#     # put the array in to the score function
#     list_return.append(Score(array1))
#
#     if Score(array1) > list_highest[0]:
#         list_highest.insert(0, (Score(array1)))
#         array2 = array1
#     # print i
#     print Score(array1)

# print list_return
# print list_highest
# # print array2
