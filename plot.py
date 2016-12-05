import numpy as np
import matplotlib.pyplot as plt

def Plot(list2):
    plt.axis([0, 30, 50, 1000])
    plt.ylabel('Score')
    plt.xlabel('Iterations')

    j = 0
    for i in list2:
        plt.scatter(j, i)
        plt.plot(j, i)
        j += 1

    plt.grid()
    plt.show()
