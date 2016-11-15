import random
from main import lessons

def shuffle(list, start, stop):
    i = start
    while (i < stop  -1):
        idx = random.randrange(i, stop)
        list[i], list[idx] = list[idx], list[i]
        i += 1

shuffle(lessons, 0, 20)
shuffle(lessons, 21, 140)

# i = 0
# for elements in lessons:
#     print lessons[i].name
#     i += 1
