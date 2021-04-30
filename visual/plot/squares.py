import matplotlib.pyplot as plt


def small():
    x_small = [3, 3, 4, 4, 3]
    y_small = [3, 4, 4, 3, 3]
    plt.plot(x_small, y_small, "r:o")


def medium():
    x_med = [2, 2, 5, 5, 2]
    y_med = [2, 5, 5, 2, 2]
    plt.plot(x_med, y_med, "g--s")


def large():
    x_large = [1, 1, 6, 6, 1]
    y_large = [1, 6, 6, 1, 1]
    plt.plot(x_large, y_large, "b-p")


def run():
    small()
    medium()
    large()
    plt.show()

run()

