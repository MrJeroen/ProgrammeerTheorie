from plot2 import Plot2
from plot3 import Plot3
from algorithms import *
import pickle

# List containing the highest scores that are encountered during iteration.
list_highest = [-500]

# create lists for plotting.
xaxis = []
yaxis =[]

# Create a random schedule.
random = ShuffledList(lessons)
with open('algo2.py', 'wb') as fp:
    pickle.dump(random, fp)

# Iterate through the hillclimber algorithm
for i in range(1, 1001):
    xaxis.append(i)
    # Open random schedule and make this the base schedule. After the first
    # run this will be the bests schedule generated from the loop below.
    with open ('algo2.py', 'rb') as fp:
        best_list = pickle.load(fp)

    # Score the base schedule.
    best_score = score(best_list)
    print best_score

    # Make 'x' changes on the base schedule
    for j in range(10):
        # Change two objects in the schedule & score it.
        new_list = hillclimber(best_list, 0, 139, 0, 139, 0, 139)
        new_score = score(new_list)

        # If a schedule is improved, save it
        if new_score > list_highest[0]:
            list_highest.insert(0, new_score)
            best_list = new_list
            # Create a file with the best list for the next step.
            with open('algo2.py', 'wb') as fp:
                pickle.dump(best_list, fp)
    # Create list for plot
    yaxis.append(best_score)

Plot2(xaxis, yaxis, 'Hillclimber')
