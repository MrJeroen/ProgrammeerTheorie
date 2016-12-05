import numpy as np
from main import courses, students, room_list, lessons
import collections

def Score(array):
    score = 1000

    # for student in students:
    #     overlap = []
    #     for room in range(7):
    #         for days in range(5):
    #             for time in range(4):
    #                 if student.id in array[days][time][room][1].students:
    #                     overlap.append((time, days))
    #
    #     total_overlap = [[x,overlap.count(x)] for x in set(overlap)]
    #     for elements in total_overlap:
    #         if elements[1] > 1:
    #             score -= elements[1] - 1

    for day in range(5):
        for time in range(4):
            overlap = []
            for room in range(7):
                for i in array[day][time][room][1].students:
                    overlap.append(i)

            conflict = collections.Counter(overlap).values()
            for i in conflict:
                if i > 1:
                    score -= 1

    for vak in courses[:-1]:
        monday = 0
        tuesday =  0
        wednesday = 0
        thursday = 0
        friday = 0
        day = 0
        for day in range(5):
            list_hc = []

            hc_count = 0
            pr_count = 0
            wc_count = 0

            overlap_count = 0
            room = 0

            for room in range(7):
                time = 0
                for time in range(4):

                    # if int(array[day][time][room][0].seats) < int(array[day][time][room][1].amount):
                    #     score += int([day][time][room][0].seats) - int(array[day][time][room][1].amount)
                    #     print 'hi'

                    seats = int(array[day][time][room][0].seats)
                    print '1'
                    print seats
                    amount = int(array[day][time][room][1].amount)
                    print '2'
                    print amount

                    if seats < amount:
                        score -= (amount - seats)
                        print '3'
                        # print score


                    if vak.name == array[day][time][room][1].name:
                        if array[day][time][room][1].group_name == 'hc':
                            list_hc.append(day)
                            hc_count += 1
                        elif array[day][time][room][1].group_name == 'wc':
                            wc_count = 1
                        elif array[day][time][room][1].group_name == 'pr':
                            pr_count = 1

                        if vak.totaal_activiteiten() >= 2 and vak.totaal_activiteiten() <= 4:
                            if day == 0:
                                monday = 1
                            elif day == 1:
                                tuesday = 1
                            elif day == 2:
                                wednesday = 1
                            elif day == 3:
                                thursday = 1
                            elif day == 4:
                                friday = 1


            if vak.totaal_activiteiten() == 2:
                if monday == 1 and thursday == 1:
                    score += 20
                elif tuesday == 1 and friday == 1:
                    score += 20
            elif vak.totaal_activiteiten() == 3:
                if monday == 1 and wednesday == 1 and friday == 1:
                    score += 20
            elif vak.totaal_activiteiten() == 4:
                if monday == 1 and tuesday == 1 and thursday == 1 and friday == 1:
                    score += 20

            if hc_count > 1:
                overlap_count += (hc_count - 1)
            if wc_count == 1 or pr_count == 1:
                for i in range(hc_count):
                    if wc_count == 1:
                        overlap_count += 1
                    if pr_count == 1:
                        overlap_count += 1
                if wc_count == pr_count:
                    overlap_count += 1

            if overlap_count >= 3:
                score -= 30
            elif overlap_count == 2:
                score -= 20
            elif overlap_count == 1:
                score -= 10

    return score
