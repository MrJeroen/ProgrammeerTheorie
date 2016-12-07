from plot import Plot
from algorithms import *
import pickle

list_return = []
list_highest = [0]

with open ('algo2.py', 'rb') as fp:
    best_list = pickle.load(fp)

best_score = score(best_list)
print best_score

for i in range(100):
    for j in range(100):
        new_list = hillclimber(best_list, 60, 139)
        new_score = score(new_list)
        list_return.append(new_score)

        if new_score > best_score:
            all_lists = []
            list_highest.insert(0, new_score)

            all_lists.append(new_list)
            best_schedule = new_list
            best_score = score(best_schedule)
            print best_score

            with open('algo3.py', 'wb') as fp:
                pickle.dump(best_schedule, fp)

print list_highest
Plot(list_return)
