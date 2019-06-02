import matplotlib.pyplot as plt


def linear_function(a, b):
    x_values = [i for i in range(0, 100001)]
    y_values = [a * x + b for x in x_values]
    
    plt.plot(x_values, y_values, linewidth=4)
    
    plt.title('Linear Function', fontsize=24)
    plt.xlabel('x', fontsize=14)
    plt.ylabel(str(a) + ' * x + ' + str(b), fontsize=14)
    
    plt.tick_params(axis='both', labelsize=14)
    
    plt.show()
    
    
print('y = ax + b')
a = input('Digite o coeficiente "a": ')
a = float(a)

b = input('Digite o coeficiente "b": ')
b = float(b)

linear_function(a, b)