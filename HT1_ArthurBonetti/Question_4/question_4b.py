import numpy as np
A = np.ones((7,7))
A = np.triu(A,0)
print(A)
B = np.ones((7,7))
B = np.triu(B,1)
B = 6*B - 1
print(B)
print(np.int64(np.matmul(np.matmul(A,B),A)))