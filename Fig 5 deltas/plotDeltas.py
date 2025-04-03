#######################################################################################
# 
# Reads in data from deltaData.txt and plots a histogram as in Fig. 5
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

d = np.loadtxt("deltaData.txt", dtype=np.longdouble, skiprows=1)[:,1]
d = np.ma.masked_equal(d,0.0)
bins = np.logspace(start=np.log10(np.min(d)), stop=np.log10(np.max(d)), num=50)

plt.hist(x=d, bins=bins, color='k')

plt.yscale("log")
plt.xscale("log")
plt.xlabel(r"$D^2_{min}$")
plt.ylabel(r"P($D^2_{min}$)")
plt.tight_layout()
plt.show()
plt.clf()

d = -1*np.loadtxt("deltaData.txt", dtype=np.longdouble, skiprows=1)[:,2]
d = np.ma.masked_equal(d,0.0)
bins = np.logspace(start=np.log10(np.min(d[d>0])), stop=np.log10(np.max(d[d>0])), num=50)

plt.hist(x=d[d>0], bins=bins, color='k')

plt.yscale("log")
plt.xscale("log")
plt.xlabel(r"$\Delta E_{seq}$")
plt.ylabel(r"P($\Delta E_{seq}$)")
plt.tight_layout()
plt.show()

d = np.loadtxt("deltaData.txt", dtype=np.longdouble, skiprows=1)
plt.plot(d[:,1],d[:,0],'.', color='k')
plt.xlabel(r"$D^2_{min}$")
plt.ylabel(r"|$\Delta E$|")
plt.xscale("log")
plt.yscale("log")
plt.tight_layout()
plt.show()
plt.clf()
