import numpy as np
from numpy.linalg import matrix_power
A = np.array([[3, 1, 4],[1, 5, 9],[-5,3,1]])
transfo = matrix_power(A,3) + 9*matrix_power(A,2) + 15*A

print(A)
print(transfo)