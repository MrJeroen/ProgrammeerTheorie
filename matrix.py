import numpy as np
import csv
import itertools
from base import Courses, Students, Lessons
from main import courses, lessons, students

# Create dimensions for numpy array
dagen = 5
tijdslot = 4
lokaal = 7

# Create 3D array containing type objects
array = np.ndarray((dagen, tijdslot, lokaal), dtype = np.object)

# Creat counters for upcoming loop
traverser = 0
room = 0

# Iterate through lessons list containing the needed instances
for elements in lessons:
    # For every room
    # Last room (#7) does not fill
    while room < 6:
        # Reset day counter
        day = 0
        # For every day
        while day < 5:
            # Reset time counter
            time = 0
            # For every timeslot
            while time < 4:
                # Fill array
                array[day][time][room] = lessons[traverser].name
                # Next element in list
                traverser += 1
                # Next timeslot
                time += 1
            # Next day
            day += 1
        # Next room
        room += 1

print array
print day
print time
print room
