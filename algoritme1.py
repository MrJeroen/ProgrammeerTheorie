from plot import Plot
from algorithms import *
import pickle

list_return = []
list_highest = [0]

for i in range(1000):
    new_list = ShuffledList(lessons)
    new_score = Score(Array(lessons))
    print new_score
    list_return.append(new_score)

    if new_score > list_highest[0]:
        all_lists = []
        list_highest.insert(0, new_score)

        all_lists.append(new_list)
        best_schedule = new_list

        with open('algo1.py', 'wb') as fp:
            pickle.dump(best_schedule, fp)

print list_highest
Plot(list_return)
# print array2
