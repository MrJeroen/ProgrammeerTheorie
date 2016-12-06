import random
from main import lessons
from list import Array
from score import Score
from plot import Plot
import pickle

list_return = []
list_highest = [0]

#print lessons[0].students

def shuffle(list, start, stop):
    # Get set value
    i = start
    while (i < stop  - 1):
        # Get random integer
        random_integer = random.randrange(i, stop)
        # Switch places in list
        list[i], list[random_integer] = list[random_integer], list[i]
        i += 1

# Give input
# shuffle(lessons, 0, 20)
# shuffle(lessons, 21, 140)

def ShuffledList(lessons):
    shuffle(lessons, 0, 19)
    shuffle(lessons, 20, 59)
    shuffle(lessons, 60, 139)
    return lessons

# i = 0
# for elements in lessons:
#     print lessons[i].name
#     i += 1

all_lists = []

for i in range(10):
    new_list = ShuffledList(lessons)
    new_array = Array(lessons)
    score = Score(new_array)
    list_return.append(score)
    all_lists.append(new_list)

    if score > list_highest[0]:
        list_highest.insert(0, (score))
        m = i

best_schedule = all_lists[m]


print list_return
print list_highest

#Plot(list_return)
# print array2

with open('list2.py', 'wb') as fp:
    pickle.dump(best_schedule, fp)
