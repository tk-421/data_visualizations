import matplotlib.pyplot as plt

x_vals = list(range(1, 1000))
y_vals = [x**3 for x in x_vals]

plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Reds, edgecolor='none', s=20)

plt.title("Cubes", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cubes of Values", fontsize=14)

plt.axis([0, 1100, 0, 1100000000])

plt.show()
