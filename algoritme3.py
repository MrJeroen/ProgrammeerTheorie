from plot2 import Plot2
from algorithms import *
import pickle

# list containing every new score of every iteration.
list_return = []
# List containing the highest scores that are encountered during iteration.
list_highest = [0]
xaxis = []
extra =[]

random = ShuffledList(lessons)
# Create a file with a random schedule to start the hillclimber.
with open('algo5.py', 'wb') as fp:
    pickle.dump(random, fp)

# Iterate through the hillclimber algorithm 'x' amount of times.
for i in range(1, 5):
    xaxis.append(i)
    print "blablabla"
    with open ('algo5.py', 'rb') as fp:
        best_list = pickle.load(fp)

    for j in range(10):
        # Score the best schedule.
        best_score = score(best_list)
        print best_score
        # Get a (new) shuffeled list based on the shuffle method.
        new_list = hillclimber(best_list, 0, 19, 20, 59, 60, 139)
        # Score this new list.
        new_score = score(new_list)
        print "hoi1"
        print new_score
        # If the new score is better compared to the previous highest.
        if new_score > best_score:
            print "hoi2"
            best_list = new_list
            # Create a file with the best list for future algorithms.
            with open('algo5.py', 'wb') as fp:
                pickle.dump(new_list, fp)


    extra.append(best_score)

print extra
#Plot2(xaxis, extra, 'Hillclimber')
