from question_2b import *
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



def graph(f, n, xmin, xmax, resolution=1001):
    '''Plot the graph of interpolated points, f = function, n = nb points, xmin = begin plot, xmax = end plot, save the result in a png file with the function as a name'''
    xp = []
    yp = []
    interval = xmin
    while interval <=xmax:
        xp.append(interval)
        yp.append(f.subs(x_var,interval))
        interval += (xmax-xmin)/(4)         #Estimate with 5 points (/4) in our array
    interval_for_interpolation = xmin
    points = []
    for i in range(n):
        points.append([interval_for_interpolation,p_L(interval_for_interpolation, xp, yp)])
        interval_for_interpolation += (xmax-xmin)/(n-1)
    x = [i[0] for i in points]
    y = [i[1] for i in points]
    plt.scatter(x,y)
    plt.title(f'Lagrange interpolation of {f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(f'/files/take-home-1/Exam/Question_2/results/PLOT_{f}.png')
    plt.close()
    plt.savefig(sys.stdout.buffer)
