import numpy as np
import pylab as plt
# from score import *

def Plot(list2):
    # Values for x and y axis
    plt.axis([0, 110, 50, 600])

    plt.ylabel('Score')
    plt.xlabel('Iterations')
    j = 0

    for i in list2:
        score = i
        iteration = j
        j += 1
        # Produce scatter plot
        plt.scatter(iteration, score)

    # Show plot
    plt.show()
