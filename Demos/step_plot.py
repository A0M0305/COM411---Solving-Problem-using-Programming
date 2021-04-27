import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [10,15.5,18.2,20,25,36,45]

plt.xlabel("Age")

plt.ylabel("Height")

plt.step(x,y,"bD--")  # changes come from this line as of step rather than plot.

plt.show()

