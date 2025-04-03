#######################################################################################
# 
# Reads in dx and dE during minimization and fits a cubic as in Fig. 8
#
#######################################################################################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import time
import sys
import os
from matplotlib import cm


matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
plt.rcParams["figure.figsize"] = (3.4,2.2)

data = np.loadtxt("dx-vs-dE.txt")

def func_cubic(x, a, b, c, d):
    return a*np.power(x, 3.0) + b*np.power(x, 2.0) + c*x + d

dr = data[:,0]
de = data[:,1]

coeffs = []
error = []
x_error = []
for ii in range(len(dr)-10):
    x = dr[:ii+10]
    y = de[:ii+10]
    x_error.append(x[-1]/dr[-1])
    coeffs.append(np.polyfit(x, y, 3))
    fitfunc = func_cubic(x, coeffs[-1][0], coeffs[-1][1], \
    coeffs[-1][2], coeffs[-1][3])
    error.append(np.linalg.norm(fitfunc - y))
thresh = np.min(error) + (np.max(error) - np.min(error))/20 # 5 of total error increase
aa = np.argmin(np.abs(np.array(error) - thresh))
x = np.linspace(np.min(dr), np.max(dr), num=100)
p1 = (dr[aa]-dr[0])/(dr[-1]-dr[0]) # percent of data well fit by cubic

plt.plot(x_error, error, '.')
plt.xlabel("fraction of distance fit")
plt.ylabel("error")
plt.plot(x_error, np.ones((len(error)))*thresh, '-', color='k')
plt.tight_layout()
plt.show()
plt.clf()

plt.plot(dr, de, 'o', color='teal')
x = np.linspace(np.min(dr), np.max(dr), num=100)
plt.plot(x, func_cubic(x, coeffs[aa][0], coeffs[aa][1], coeffs[aa][2], coeffs[aa][3]), \
          '-', label="cubic fit", color='k')

plt.ylim([np.min(de),np.max(de)])
plt.xlabel("dx")
plt.ylabel("dE")
plt.tight_layout()
plt.show()
plt.clf()
