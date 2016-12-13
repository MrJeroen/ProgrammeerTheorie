import matplotlib.pyplot as plt

def Plot2(list1, list2, string):
    plt.plot(list1, list2)

    plt.xlabel('Iterations')
    plt.ylabel('Score')
    plt.title(string)
    plt.show()
