import random
from main import lessons
from list import Array
from score import Score
import random

def shuffle(list, start, stop):
    # Get set value
    i = start
    while (i < stop  -1):
        # Get random integer
        random_integer = random.randrange(i, stop)
        # Switch places in list
        list[i], list[random_integer] = list[random_integer], list[i]
        i += 1

def ShuffledList(lessons):
    shuffle(lessons, 0, 19)
    shuffle(lessons, 20, 59)
    shuffle(lessons, 60, 139)
    return lessons

def hillclimber(list, start, end):
    random_integer1 = random.randrange(start, end)
    random_integer2 = random.randrange(start, end)
    list[random_integer1], list[random_integer2] = list[random_integer2], list[random_integer1]
    return list

def score(list):
    # put the shuffled list in to the Array function from list.py
    array1 = Array(list)
    # check the score of this list
    return Score(array1)

def temp(old, new, t):
    return (2.71828*((new - old)/t)) / 100

best_list = ShuffledList(lessons)
best_score = score(best_list)
highestpoint = []


T = 1.0
T_min = 0.0001
alpha = 0.9
while T > T_min:
    i = 1
    while i <= 100:
        for j in range(500):
            new_list = hillclimber(best_list, 60, 139)
            new_score = score(new_list)
            temperature = temp(best_score, new_score, T)
            if temperature > -0.2:
                temp_list = new_list
                best_score = score(temp_list)
                print best_score
        best_list = temp_list
        highestpoint.append(best_score)
        i += 1
    T = T*alpha


print highestpoint
