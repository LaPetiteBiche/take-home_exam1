class Point:
    def __init__(self,x,y):
        self.x, self.y = x,y
    
    def __str__(self):
        return '(%g, %g)'%(self.x, self.y)