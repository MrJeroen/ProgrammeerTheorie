from main import lessons
from list import Array
from score import Score
import random

# Random Algorithm. Randomly shuffles a given list
def shuffle(list, start, stop):
    # Get set value
    i = start
    while (i < stop  - 1):
        # Get random integer
        random_integer = random.randrange(i, stop)
        # Switch places in list
        list[i], list[random_integer] = list[random_integer], list[i]
        i += 1

# Shuffle various lists from main.lessons before implementing a large list
def ShuffledList(lessons):
    shuffle(lessons, 0, 19)
    shuffle(lessons, 20, 59)
    shuffle(lessons, 60, 139)
    return lessons

# Hillclimber Algorithm. Change 2 positions in a given schedule with each other.
def hillclimber(list, start, end):
    random_integer1 = random.randrange(start, end)
    random_integer2 = random.randrange(start, end)
    list[random_integer1], list[random_integer2] = list[random_integer2], list[random_integer1]
    return list

# Annealing Algorithm. Determin if decline in score is (still) acceptable
def temp(old, new, t):
    return (2.71828*((new - old)/t)) / 100

# Score a given schedule
def score(list):
    # put the shuffled list in to the Array function from list.py
    array = Array(list)
    # check the score of this list
    return Score(array)
    
