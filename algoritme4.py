from plot2 import Plot2
from algorithms import *
import pickle

def temp(old, new):
    return (new - old)/100

#Create a random schedule.
random = ShuffledList(lessons)
with open('algo7.py', 'wb') as fp:
    pickle.dump(random, fp)

# Create lists to keep track of the score.
xaxis = []
yaxis =[]

T = -0.8
iterations = 10001
alpha = 0.00125**(1.0/iterations)

# Iterate through the annealing algorithm
for i in range(1, iterations):
    list_highest = [0];
    xaxis.append(i)
    # Open the random schedule and make this the base schedule. After the first
    # run this will be the bests schedule generated from the loop below.
    with open ('algo7.py', 'rb') as fp:
        best_list = pickle.load(fp)

    # Score the base schedule.
    best_score = score(best_list)
    print best_score

    # Make 'x' changes on the base schedule
    for i in range(10):
        # Change two objects in the schedule & score it.
        new_list = hillclimber(best_list, 0, 139, 0, 139, 0, 139)
        new_score = score(new_list)

        # Calculate the temperature of the new score.
        temperature = temp(best_score, new_score)

        # Decide if the new score will be accepted based on the temperature.
        if T < temperature :
            # Add new score to the list if it is higher then the highest new score.
            if new_score > list_highest[0]:
                list_highest.insert(0, new_score)
                best_list = new_list
                # Create a file with the best list for the next step.
                with open('algo7.py', 'wb') as fp:
                    pickle.dump(best_list, fp)
    # Lower the temperature.
    T = T*alpha
    # Create list for plot
    yaxis.append(best_score)

Plot2(xaxis, yaxis, 'Annealing')
