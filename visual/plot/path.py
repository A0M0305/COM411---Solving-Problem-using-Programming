import matplotlib.pyplot as plt


def coordinate():
    x = int(input("Please enter a value for X = "))
    y = int(input("Please enter a value for Y = "))
    return x, y


def path():
    print("Retrieve path...")
    x_values = []
    y_values = []
    for i in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]


def run():
    values = path()
    plt.plot(values[0], values[1], "r--o")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.show()


run()
