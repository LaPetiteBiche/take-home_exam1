import math

class Circle:
    
    def __init__(self,x_zero, y_zero, radius):
        self.x_zero = x_zero
        self.y_zero = y_zero
        self.radius = radius
    
    def area(self):
        return(float(math.pi * self.radius ** 2))
    
    def circumference(self):
        return(2 * math.pi * self.radius)
    
    def __str__(self):
        s = f"A Circle with radius {self.radius} at ({self.x_zero}, {self.y_zero}) has area {round(self.area(),4)}"
        return s