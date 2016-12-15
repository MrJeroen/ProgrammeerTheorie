from plot2 import Plot2
from algorithms import *
import pickle

# list containing every new score of every iteration.
list_return = []
# List containing the highest scores that are encountered during iteration.
list_highest = [0]
# Lists for plotting.
xaxis = []
extra =[]

# Create a random schedule and save.
random = ShuffledList(lessons)
with open('algo5.py', 'wb') as fp:
    pickle.dump(random, fp)

# Iterate through the hillclimber algorithm
for i in range(1, 11):
    xaxis.append(i)
    # Open random schedule and make this the base schedule. After the first
    # run this will be the bests schedule generated from the loop below.
    with open ('algo5.py', 'rb') as fp:
        best_list = pickle.load(fp)

    # Score the base schedule.
    best_score = score(best_list)
    print best_score

    # Make 'x' changes on the base schedule
    for j in range(100):
        # Change two objects in the schedule & score it.
        new_list = hillclimber(best_list, 0, 19, 20, 59, 60, 139)
        new_score = score(new_list)
        # print new_score

        # If a schedule is improved, save it
        if new_score > best_score:
            # list_highest.insert(0, new_score)
            if new_score > list_highest[0]:
                list_highest.insert(0, new_score)
                best_list = new_list
                # Create a file with the best list for future algorithms.
                with open('algo5.py', 'wb') as fp:
                    pickle.dump(best_list, fp)
    # Create list for plot
    extra.append(best_score)

print list_highest
# print extra
Plot2(xaxis, extra, 'Hillclimber')
