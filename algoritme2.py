from plot import Plot
from algorithms import *
import pickle

# list containing every new score of every iteration.
list_return = []
# List containing the highest scores that are encountered during iteration.
list_highest = [0]


# Iterate through the hillclimber algorithm 'x' amount of times.
for i in range(10000):

    # Open the best schedule provided by algorithm 1.
    with open ('algo1.py', 'rb') as fp:
        best_list = pickle.load(fp)

    # Score the best schedule.
    best_score = score(best_list)
    print best_score
    # Get a (new) shuffeled list based on the shuffle method.
    new_list = hillclimber(best_list, 0, 19, 20, 59, 60, 139)
    # Score this new list.
    new_score = score(new_list)
    # Add new score to a list.
    list_return.append(new_score)
    print new_score

    # If the new score is better compared to the previous highest.
    if new_score > best_score:
        print new_score
        print 'hello'
        # Store new best score into list.
        list_highest.insert(0, new_score)

        best_schedule = new_list
        best_list = new_list
        best_score = score(best_list)
        print best_score
        print 'hello'

        # Create a file with the best list for future algorithms.
        with open('algo1.py', 'wb') as fp:
            pickle.dump(best_schedule, fp)

print list_highest
Plot(list_return)
