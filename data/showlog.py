import os
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
import numpy as np


def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


def func(x, c,d):
    #return d * np.log(x) + e
    #return d/np.array(x,dtype=np.float32)**2 + e
    return x**c*d


f = open("log", "r")

x = []
y = []

for l in f.readlines():
    d = l.split()
    nx = len(y)+100
    ny = float(d[3])

    x.append(nx)
    y.append(ny)


yy3 = smooth(y, 1000)

# pr, pc = curve_fit(func, x[-200000:], yy3[-200000:])
pr, pc = curve_fit(func, x, yy3)
print(pr)

yy2 = func(x , pr[0], pr[1])

plt.ylim(0, 2)
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.1))
plt.scatter(x[100:], y[100:], 0.1)
plt.plot(x[100:], yy3[100:], color="#ff0000", linewidth=0.25)
plt.plot(x[100:], yy2[100:], color="#00ff00", linewidth=1)


plt.grid(True, axis="y")
plt.savefig('log.png', dpi=800)
plt.show()
