from random import randint


class Die:
    """A class that represents a single die"""
    
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll(self):
        """Returns a random value between 1 and the number of sides"""
        return randint(1, self.sides)