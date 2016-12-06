import numpy as np
import matplotlib.pyplot as plot
import collections
import pylab as pl

def Plot(list2):
    counter = collections.Counter(list2)

    print counter

    pl.bar(counter, counter.values())

    plot.title('Algorithm')
    plot.xlabel('Score')
    plot.ylabel('Frequency')

    xmax = max(counter.keys()) + 2
    ymax = max(counter.values()) + 2

    pl.ylim(0, ymax)
    pl.grid()
    pl.show()
