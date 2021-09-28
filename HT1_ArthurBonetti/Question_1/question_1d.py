from poisson import *
import pandas as pd
import numpy as np

table = [["k","lambda","poisson(k,lambda)"]]
lam = 1
for i in range (0,6):
    table.append([i, 1, poisson(i,1)])
df = pd.DataFrame(table)
np.savetxt(r'/files/take-home-1/Exam/Question_1/results/poisson.txt', df.values, fmt='%s')