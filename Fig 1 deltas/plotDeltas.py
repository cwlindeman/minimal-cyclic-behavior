#######################################################################################
# 
# Reads in data from deltaData.txt and plots a histogram as in Fig. 1b
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

d = np.loadtxt("deltaData.txt", dtype=np.longdouble, skiprows=1)[:,0]
d = np.ma.masked_equal(d,0.0)
bins = np.logspace(start=np.log10(np.min(d)), stop=np.log10(np.max(d)), num=50)

plt.hist(x=d, bins=bins, color='k')

plt.yscale("log")
plt.xscale("log")
plt.xlabel(r"|$\Delta E$|")
plt.ylabel(r"P(|$\Delta E$|)")
plt.tight_layout()
plt.show()
plt.clf()
