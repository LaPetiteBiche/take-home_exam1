import pandas as pd
import numpy as np


def meterstoyards():
    table = [["Meters","Yards"]]
    for i in range(0,110,10):
        yards = i*1.09361
        table.append([i,yards])
    df = pd.DataFrame(table)
    np.savetxt(r'/files/take-home-1/Exam/Question_1/results/meters_to_yards.txt', df.values, fmt='%s')

meterstoyards()