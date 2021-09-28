import math
import numpy as np 
import sympy as sym

#Lagrange's interpolation formula

def L_k(x, k, xp, yp):
    prod = 1
    for i in range(len(xp)):
        if i != k :
            prod *= (x - xp[i])/(xp[k]-xp[i])
    return prod

        
def p_L(x, xp, yp):
    ''' Lagrange interpolation formula, x = point to estimate, xp = array of x coordinates, yp = array of y coordinates'''
    
    sum = 0
    for i in range(len(yp)):
        sum += yp[i] * L_k(x, i, xp, yp)
    return sum
        

def verify(xp, yp):
    liste = []
    for i in range(len(xp)):
        liste.append(abs(p_L(xp[i], xp, yp)-yp[i]))
    return liste


# Create 5 points in arrays for sin(x) between 0 and pi 

x_var = sym.symbols('x')
y1 = sym.sin(x_var)
xp1 = []
yp1 = []
interval = 0
while interval <= sym.pi :
    xp1.append(interval)
    yp1.append(y1.subs(x_var,interval))
    interval += sym.pi/4

# Create 5 points in arrays for cos(x) between 0 and 2pi

y2 = sym.cos(x_var)
xp2 = []
yp2 = []
interval = 0
while interval <= 2*sym.pi :
    xp2.append(interval)
    yp2.append(y2.subs(x_var,interval))
    interval += sym.pi/2


# Create 5 points in arrays for cos(x) between 0 and 1

y3 = sym.exp(x_var)
xp3 = []
yp3 = []
interval = 0
while interval <= 1 :
    xp3.append(interval)
    yp3.append(y3.subs(x_var,interval))
    interval += 1/4
