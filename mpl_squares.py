import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
x_values_squares = [1, 4, 9, 16, 25]

plt.figure(figsize=(10, 6), dpi=128)

#plot creates a linear graphic
#linewidth sets the width of the line
#first parameter is values of the x axis
#second parameter is values of the y axis
plt.plot(x_values, x_values_squares, linewidth=5)

#Define the title of the grafic 
#fontsize sets the size of the font
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14) #label of x axis
plt.ylabel('Square of Value', fontsize=14) #label of y axis

#Defines the size of the labels of markings
plt.tick_params(axis='both', labelsize=14)

plt.axis([0, 5, 0, 25])

#shows the graphic 
plt.show()