from pygal import Bar
from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.x_values = [0]
        self.y_values = [0]
        self.num_points = num_points
    
    def __definex(self):
        x_direction = choice([-1, 1])
        x_distance = choice([d for d in range(101)])
        self.step_x = x_direction * x_distance
        
    def __definey(self):
        y_direction = choice([-1, 1])
        y_distance = choice([d for d in range(101)])
        self.step_y = y_direction * y_distance
        
    def __nextstep(self):
        next_x = self.step_x + self.x_values[-1]
        next_y = self.step_y + self.y_values[-1]
        
        self.x_values.append(next_x)
        self.y_values.append(next_y)
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            self.__definex()
            self.__definey()
            
            if not self.step_x and not self.step_y:
                continue
            
            self.__nextstep()
            
    def show_walk(self):
        hist = Bar()
        hist.title = 'Random Walk'
        hist.add('X Values', self.x_values)
        hist.add('Y Values', self.y_values)
        hist.render_to_file('randomwalk.svg')