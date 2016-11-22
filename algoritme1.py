import random
from main import lessons

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
    shuffle(lessons, 0, 20)
    shuffle(lessons, 21, 140)
    return lessons

# i = 0
# for elements in lessons:
#     print lessons[i].name
#     i += 1
