import random
from main import lessons
from list import Array
from score import Score

list_return = []
list_highest = [-500]

def shuffle(list, start, stop):
    # Get set value
    i = start
    while (i < stop  -1):
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

for i in range(500):
# Put list lessons from main.py in the shuffle function of algoritme1
    lessons1 = ShuffledList(lessons)
    # put the shuffled list in to the Array function from list.py
    array1 = Array(lessons)
    # put the array in to the score function
    list_return.append(Score(array1))

    if Score(array1) > list_highest[0]:
        list_highest.insert(0, (Score(array1)))
        array2 = array1

print list_return
print list_highest
# print array2
