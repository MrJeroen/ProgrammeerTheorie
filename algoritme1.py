from plot import Plot
from algorithms import *
import pickle

# list containing every new score of every iteration.
list_return = []
# List containing the highest scores that are encountered during iteration.
list_highest = [0]

# Iterate through the random algorithm 'x' amount of times.
for i in range(1000000):
    # Get a (new) shuffeled list based on the shuffle method.
    new_list = ShuffledList(lessons)
    # Score this new list.
    new_score = Score(Array(lessons))
    print new_score
    # Add new score to a list.
    list_return.append(new_score)

    # If the new score is better compared to the previous highest.
    if new_score > list_highest[0]:
        all_lists = []
        # Store new best score into list.
        list_highest.insert(0, new_score)

        # Store new schedule into list.
        all_lists.append(new_list)
        best_schedule = new_list

        # Create a file with the best list for future algorithms.
        with open('algo1.py', 'wb') as fp:
            pickle.dump(best_schedule, fp)

print list_highest
Plot(list_return)
