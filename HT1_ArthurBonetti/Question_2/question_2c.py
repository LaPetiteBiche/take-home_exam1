from question_2b import *
from L_graph import *


# VERIFY THAT THE FUNCTION WORKS -> OK
print(verify(xp1, yp1))
print(verify(xp2, yp2))
print(verify(xp3, yp3))

# Evaluate interpolated points -> OK

print(f'Computed sin(x) at x = pi/8 : {p_L(sym.pi/8, xp1, yp1)}, true value = {sym.sin(sym.pi/8)}')
print(f'Computed cos(x) at x = pi/4 : {p_L(sym.pi/4, xp2, yp2)}, true value = {sym.cos(sym.pi/4)}')
print(f'Computed exp(x) at x = 0.125 : {p_L(0.125, xp3, yp3)}, true value = {sym.exp(0.125)}')

#Plot some interpolated points into graph -> OK

graph(sym.sin(x_var), 5, 0, sym.pi)
graph(sym.cos(x_var), 10, 0, 2*sym.pi)
graph(sym.exp(x_var), 20, 0, 20)