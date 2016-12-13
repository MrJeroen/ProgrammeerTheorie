from plot import Plot
from algorithms import *
import pickle

# list containing every new score of every iteration.
list_return = []

for i in range(10):
    # List containing the highest scores that are encountered during iteration.
    list_highest = [0]

    random = ShuffledList(lessons)
    # Create a file with a random schedule to start the hillclimber.
    with open('algo1.py', 'wb') as fp:
        pickle.dump(random, fp)

    # Iterate through the hillclimber algorithm 'x' amount of times.
    for j in range(200):

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

        # If the new score is better compared to the previous highest.
        if new_score > best_score:
            # Store new best score into list.
            list_highest.insert(0, new_score)

            best_schedule = new_list
            best_list = new_list
            best_score = score(best_list)

            # Create a file with the best list for future algorithms.
            with open('algo1.py', 'wb') as fp:
                pickle.dump(best_schedule, fp)

    # Append the final score of the hillclimber to an overall list.
    list_return.append(list_highest[0])
    print list_return

print list_return
Plot(list_return)
