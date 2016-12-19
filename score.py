import numpy as np
from main import courses, students, room_list, lessons
import collections

def Score(array):
    score = 1000.0

    #Determine if students have any overlap on a given time during a given day.
    # Checked.
    for day in range(5):
        for time in range(4):
            overlap = []
            for room in range(7):
                for i in array[day][time][room][1].students:
                    # Create a big list with all the students during a given timeslot for each room.
                    overlap.append(i)

            # Count the total occurrences of a given student number in this list.
            conflict = collections.Counter(overlap).values()
            # If a student number is counter > 1, change the score.
            for i in conflict:
                if i > 1:
                    score -= 1

            if int(array[day][time][room][0].seats) < int(array[day][time][room][1].amount):
                score -= int(array[day][time][room][1].amount) - int(array[day][time][room][0].seats)


    # To fill the array we added an 'empty course'. As these are just empty
    # # time slots, are not taking into account during scoring.
    for vak in courses[:-1]:

        # Set counters
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
                    # If a given number of students exceeds the amount of available seats, substract the
                    # student surplus.
                    # Every class (hc, wc, or pr) is stored in our object. Every time one of these
                    # are encountered, change the counters initialized above.
                    if vak.name == array[day][time][room][1].name:
                        if array[day][time][room][1].group_name == 'hc':
                            hc_count += 1
                        elif array[day][time][room][1].group_name == 'wc':
                            wc_count = 1
                        elif array[day][time][room][1].group_name == 'pr':
                            pr_count = 1

                    # Determine the total activities of a given course
                    # Check
                    if vak.totaal_activiteiten() >= 2 and vak.totaal_activiteiten() <= 4:
                        if vak.name == array[day][time][room][1].name:
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

            # Score based on the spread of a course. If 3 activities are clustered
            # on 1 day, points are substracted.
            if hc_count > 1:
                overlap_count += (hc_count - 1)
                # print overlap_count
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

        # Score based on the total spread of a given course over the week.
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
    return score
