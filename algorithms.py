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
# As we are working with 3 lists, a random integer is generated to determine
# which of the three lists will be changed.
def hillclimber(list, start1, end1, start2, end2, start3, end3):
    random_integer = random.randint(1, 3)
    if random_integer == 1:
        functie(start1, end1, list)

    elif random_integer == 2:
        functie(start2, end2, list)

    elif random_integer == 3:
        functie(start3, end3, list)

    return list

def functie(start, end, list):
    random_integer1 = random.randrange(start, end)
    random_integer2 = random.randrange(start, end)
    list[random_integer1], list[random_integer2] = list[random_integer2], list[random_integer1]

# Annealing Algorithm. Determine if decline in score is (still) acceptable --> still needs more info.
def temp(old, new, t):
    return (((new - old)/t))

# Every schedule can be scored through this method. See score.py for further
# details.
def score(list):
    array = Array(list)
    return Score(array)
