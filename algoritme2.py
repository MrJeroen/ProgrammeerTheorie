from plot2 import Plot2
from algorithms import *
import pickle

# List containing the highest scores that are encountered during iteration.
list_highest = [0]
xaxis = []
extra =[]

random = ShuffledList(lessons)
# Create a file with a random schedule to start the hillclimber.
with open('algo1.py', 'wb') as fp:
    pickle.dump(random, fp)

# Iterate through the hillclimber algorithm 'x' amount of times.
for i in range(1, 1000):
    xaxis.append(i)

    # Open the best schedule provided by algorithm 1.
    with open ('algo1.py', 'rb') as fp:
        best_list = pickle.load(fp)

    # Score the best schedule.
    best_score = score(best_list)
    print best_score

    extra.append(best_score)

    # Get a (new) shuffeled list based on the shuffle method.
    new_list = hillclimber(best_list, 0, 19, 20, 59, 60, 139)
    # Score this new list.
    new_score = score(new_list)

    # If the new score is better compared to the previous highest.
    if new_score > best_score:
        # Create a file with the best list for future algorithms.
        with open('algo1.py', 'wb') as fp:
            pickle.dump(new_list, fp)
        # Store new best score into list.
        list_highest.insert(0, best_score)


Plot2(xaxis, extra, 'Hillclimber')

#Plot(list_return)
