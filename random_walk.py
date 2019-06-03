from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    """A class to gerate random walks"""
    
    def __init__(self, num_points=5000):
        """Initiates the attributes of one walk"""
        self.num_points = num_points
        
        #All walks starts in (0, 0)
        self.x_values = [0]
        self.y_values = [0]
        
    def __definex__(self):
        """Defines the direction and the distance of the step in the x axe"""
        x_direction = choice([1, -1])
        x_distance = choice([i for i in range(0, 101)])
        self.x_step = x_direction * x_distance
        
    def __definey__(self):
        """Defines the direction and the distance of the step in the y axe"""
        y_direction = choice([1, -1])
        y_distance = choice([i for i in range(0, 101)])
        self.y_step = y_direction * y_distance
        
    def __nextwalk__(self):
        """Calculates the next values of x and y"""
        next_x = self.x_values[-1] + self.x_step
        next_y = self.y_values[-1] + self.y_step
            
        self.x_values.append(next_x)
        self.y_values.append(next_y)
            
    def __plot_first_and_last_point__(self):
        """Plots the first point and the last point"""
        plt.scatter(0, 0, c='green', edgecolor='none', s=150)
        plt.scatter(self.x_values[-1], self.y_values[-1], c='red', edgecolor='none', s=150)
        
    def __removeaxes__(self):
        """Remove the axes"""
        axes = plt.axes()
        
        x_axis = axes.get_xaxis()
        x_axis.set_visible(False)
        
        y_axis = axes.get_yaxis()
        y_axis.set_visible(False)
        
    def fill_walk(self):
        """Calculate all the points of the walk"""
        #continues walking until the walk reaches the num_points
        while len(self.x_values) < self.num_points:
            #Decide the direction and the distance to be walked
            self.__definex__()
            self.__definey__()
            
            #rejects movements that takes to nowhere
            if not self.x_step and not self.y_step:
                continue
            
            self.__nextwalk__()
            
    def plot_points(self):
        """Plot the points"""
        points_number = list(range(self.num_points))
        plt.figure(figsize=(10, 6), dpi=128)
        plt.title('Random Walk (Points)', fontsize=30)
        plt.scatter(self.x_values, self.y_values, s=10, c=points_number, edgecolor='none', cmap=plt.cm.Blues)
        self.__plot_first_and_last_point__()
        self.__removeaxes__()
        plt.show()
        
    def plot_line(self):
        """Uses the plt.plot function"""
        plt.figure(figsize=(10, 6), dpi=128)
        plt.title('Random Walk (Line)', fontsize=30)
        plt.plot(self.x_values, self.y_values, linewidth=0.5, c=(1, 0.5, 0.5))
        self.__plot_first_and_last_point__()
        plt.show()