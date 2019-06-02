import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

#scatter plots points
plt.scatter(x_values, y_values, s=40, edgecolor='none', c=y_values, cmap=plt.cm.Reds)

#defines the title of the graphic and give names of the axis
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of value', fontsize=14)

#define the size the label of the markings
plt.tick_params(axis='both', which='major', labelsize=15)

#Define the interval for each axis
plt.axis([0, 1000, 0, 1000000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()