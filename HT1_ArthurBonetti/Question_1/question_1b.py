import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the file
path = "/files/take-home-1/Exam/Question_1/results/meters_to_yards.txt"
f = open(path, 'r')

table = []
for line in f:
    col = line.split()  # split line in columns by space
    if len(col) == 0:
        continue        # ignore blanck lines
    elif col[0] == 'Meters':
        continue        # ignore first line
    met = float(col[0])
    yar = float(col[1])
    table.append([met, yar])
f.close()
print('File in array:',table)

meters = [i[0] for i in table]
yards = [i[1] for i in table]
plt.scatter(meters, yards)
plt.title("Meter-Yard conversion", fontweight='bold')
plt.xlabel('Meters')
plt.ylabel('Yards')
plt.savefig('/files/take-home-1/Exam/Question_1/results/M_Y_conversion.png')
plt.close()
plt.savefig(sys.stdout.buffer)


