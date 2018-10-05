import matplotlib.pyplot as plt

x_vals = list(range(1, 1001))
y_vals = [x**2 for x in x_vals]

plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Blues, edgecolor='none', s=30)

# Set the chart title and axis labels
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels
plt.tick_params('both', which='major', labelsize=14)

# Set the range for each axis
plt.axis([0,1100, 0, 1100000])

plt.show()
