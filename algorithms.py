from main import lessons
from list import Array
from score import Score
import random

# Randomly shuffles a list by changing random positions in this list.
# Start and stop can deterime if you want to change the whole list,
# or parts or the list.

def shuffle(list, start, stop):
    i = start
    while (i < stop  - 1):
        random_integer = random.randrange(i, stop)
        list[i], list[random_integer] = list[random_integer], list[i]
        i += 1

# Shuffle various lists from main.lessons before implementing a large list
# Small lists are sorted based on class size. The largest 20 courses are stored
# in one list and will be placed in the biggest room. The second list contains
# the middle biggest courses, placed in the 2 middle rooms. The smallest courses
# are stored in the last list and are placed in the last 4 rooms.
def ShuffledList(lessons):
    shuffle(lessons, 0, 19)
    shuffle(lessons, 20, 59)
    shuffle(lessons, 60, 139)
    return lessons

# Swaps 2 lessons in a given schedule with each other.
# As we are working with 3 lists, a random integer is generated to determine
# which of the three lists will be changed.
def hillclimber(list, start1, end1, start2, end2, start3, end3):
    random_integer = random.randint(1, 3)
    if random_integer == 1:
        part_hillclimber(start1, end1, list)

    elif random_integer == 2:
        part_hillclimber(start2, end2, list)

    elif random_integer == 3:
        part_hillclimber(start3, end3, list)

    return list

# Makes the swap in the randomly choosen list.
def part_hillclimber(start, end, list):
    random_integer1 = random.randrange(start, end)
    random_integer2 = random.randrange(start, end)
    list[random_integer1], list[random_integer2] = list[random_integer2], list[random_integer1]

# calculate the difference between new and old score for annealing
def temp(old, new):
    return (old - new)

# Every schedule can be scored through this method. See score.py for further details.
def score(list):
    array = Array(list)
    return Score(array)
