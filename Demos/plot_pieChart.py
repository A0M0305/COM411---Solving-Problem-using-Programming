import matplotlib.pyplot as plt

label = ("Lithuania", "Romania", "Poland", "Bagladesh", "Brazil", "Colombia", "Other")

data = [2, 17, 1, 2, 2, 2, 6]

plt.pie(data, labels=label)

plt.show()
