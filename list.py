import numpy as np
import csv
import itertools
from base import Courses, Students, Lessons
from main import courses, students, room_list, lessons
import pickle

def Array(lessons):
    # Create dimensions for numpy array
    dagen = 5
    tijdslot = 4
    lokaal = 7

    # Create 3D array containing type objects
    array = np.ndarray((dagen, tijdslot, lokaal), dtype = np.object)

    # Create counters for upcoming loop
    traverser = 0
    room = 0

    # Iterate through lessons list containing the objects
    for elements in lessons:
        # For every room
        while room < 7:
            # Reset day counter
            day = 0
            # For every day
            while day < 5:
                # Reset time counter
                time = 0
                # For every timeslot
                while time < 4:
                    # Fill array
                    array[day][time][room] = (room_list[room], lessons[traverser])
                    # Next element in list
                    traverser += 1
                    time += 1
                day += 1
            room += 1
    return array
