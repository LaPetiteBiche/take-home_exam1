import Point_class as p
import math

class Polar(p.Point):
    
    def __init__(self, r, teta):
        self.r = r
        self.teta = teta
        p.Point.__init__(self, r*math.cos(teta), r*math.sin(teta))
        
        
    def __str__(self):
        s = f"This point has coordinate ({self.x, self.y}, r = {self.r} and teta ={self.teta})"
        return s

    