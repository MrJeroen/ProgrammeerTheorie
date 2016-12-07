from main import lessons
from list import Array
from score import Score
import random

# Random Algorithm. Randomly shuffles the largest list by changing random positions
# in this list. The location of changes are determined with start and stop. E.g.
# If only the 20th through 60th position need to be changed, this can be inputted
# in the start and stop variable.
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

# Hillclimber Algorithm. Changes 2 positions in a given schedule with each other.
# The location(s) where these changes are made, are determined by the shuffle
# function above
def hillclimber(list, start, end):
    random_integer1 = random.randrange(start, end)
    random_integer2 = random.randrange(start, end)
    list[random_integer1], list[random_integer2] = list[random_integer2], list[random_integer1]
    return list

# Annealing Algorithm. Determine if decline in score is (still) acceptable --> still needs more info.
def temp(old, new, t):
    return (2.71828*((new - old)/t)) / 100

# Every schedule can be scored through this method. See score.py for further
# details.
def score(list):
    array = Array(list)
    return Score(array)
