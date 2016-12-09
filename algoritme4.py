from plot import Plot
from algorithms import *
import pickle

list_return = []
list_highest = [0]

with open ('algo2.py', 'rb') as fp:
    best_list = pickle.load(fp)

best_list = ShuffledList(lessons)
best_score = score(best_list)
highestpoint = []

T = 1.0
T_min = 0.1
alpha = 0.9
while T > T_min:
    i = 1
    while i <= 10:
        for j in range(50):
            new_list = hillclimber(best_list, 1, 19, 20, 59, 60, 139)
            new_score = score(new_list)
            list_return.append(new_score)
            temperature = temp(best_score, new_score, T)
            if temperature > -0.2:
                temp_list = new_list
                best_score = score(temp_list)
                print best_score

                with open('algo2.py', 'wb') as fp:
                    pickle.dump(best_schedule, fp)

        best_list = temp_list
        highestpoint.append(best_score)
        i += 1
    T = T*alpha

Plot(list_return)
print highestpoint
