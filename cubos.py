import matplotlib.pyplot as plt


x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]

#plot points
plt.scatter(x_values, y_values, edgecolor='none', c=x_values, s=10, cmap=plt.cm.Reds)

#title of graphic and labels
plt.title('Números ao cubo', fontsize=30)
plt.xlabel('Valor', fontsize=15)
plt.ylabel('Cubo do Valor', fontsize=15)

#where the label will be
plt.tick_params(axis='both', labelsize=14)

x_0 = 0
x_1 = x_values[-1]
y_0 = 0
y_1 = y_values[-1]

#the xi xf and yi yf of the points in x axis and y axis
plt.axis([x_0, x_1, y_0, y_1])

#shows the graphic
plt.show()