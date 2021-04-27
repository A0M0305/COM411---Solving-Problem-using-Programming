import matplotlib.pyplot as plt

x = ["Baby", "Toddler", "Teen", "Adult"]  # When doing bar, you can label the name of the bar instead of numbering.
y = [10,15, 25, 40]  # number of y must match how many on x to make it equals.

plt.xlabel("Age")

plt.ylabel("Height")

plt.bar(x,y, color = ["m", "g", "r", "b"])  # changes come from this line as of step rather than plot.
plt.plot(x,y)


plt.show()
