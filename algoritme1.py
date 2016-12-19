from plot import Plot
from algorithms import *
import pickle

# list containing every new score of every iteration.
score_list = []

# Iterate through the random algorithm 'x' amount of times.
for i in range(100):
    # Get a (new) shuffeled list based on the shuffle method.
    new_list = ShuffledList(lessons)
    # Score this new list.
    new_score = Score(Array(lessons))
    print new_score
    # Add new score to a list.
    score_list.append(new_score)

Plot(score_list)
