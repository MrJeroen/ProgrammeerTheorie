import numpy as np
import matplotlib.pyplot as plot
import collections
import pylab as pl

# Plot the results from the algorithm. The input contains a (large) list
# containing the scores of an 'x' amount of iterations. The title aught
# to be altered to reflect the amount of iterations and which algorithm.
def Plot(list):
    counter = collections.Counter(list)

    pl.bar(counter, counter.values())
    plot.title('Random Algorithm - 1000k')
    plot.xlabel('Score')
    plot.ylabel('Frequency')

    xmax = max(counter.keys()) + 2
    ymax = max(counter.values()) + 2
    pl.ylim(0, ymax)

    pl.grid()
    pl.show()
