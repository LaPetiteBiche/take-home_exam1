import sys
sys.path.insert(1, '/files/take-home-1/Exam/Question_2')
import question_2b as q2
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class LagrangeInterpolation:
    
    def __init__(self,xp, yp):
        self.xp = xp
        self.yp = yp
        
    def __call__(self,x):
        xp = self.xp
        yp = self.yp
        return q2.p_L(x, xp, yp)
    
    def plot(self):
        x = [i for i in self.xp]
        y = [i for i in self.yp]
        plt.scatter(x,y)
        plt.title(f'Lagrange interpolation')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.savefig(f'/files/take-home-1/Exam/Question_3/results/PLOT_1.png')
        plt.close()
        plt.savefig(sys.stdout.buffer)

def verify(p_L):
    liste = []
    for i in range(len(p_L.xp)):
        liste.append(abs(q2.p_L(p_L.xp[i], p_L.xp, p_L.yp)-p_L.yp[i]))
    return liste
    
xp = np.linspace(0, 2*math.pi, 10)
yp = np.cos(xp)
p_L = LagrangeInterpolation(xp,yp)
x = 1.2
print(f'p_L({x})={p_L(x)}')
print(f'cos({x})= {math.cos(x)}')
p_L.plot()
print(verify(p_L))