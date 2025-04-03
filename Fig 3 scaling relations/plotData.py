#######################################################################################
# 
# Reads in rearrangement data and plots on log-log scales as in Fig. 3
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

dE = -1*np.loadtxt("N=31 paired/nearTop-dE-test.txt")
hyst = np.loadtxt("N=31 paired/nearTop-hyst-test.txt")
PR = np.loadtxt("N=31 paired/nearTop-PR-test.txt")
RMS = np.loadtxt("N=31 paired/nearTop-RMS-test.txt")

plt.plot(hyst, dE, 'o', color = "lightgrey", label="paired", markeredgecolor='k')
plt.plot(hyst[PR<1.5], dE[PR<1.5], 'o', color = "purple", label="paired", markeredgecolor='k')

plt.yscale("log")
plt.xscale("log")
plt.xlabel(r"|$\gamma_h$|")
plt.ylabel(r"P(|$\Delta E$|)")
plt.tight_layout()
plt.show()
plt.clf()

u_dE = -1*np.loadtxt("N=31 nonpaired/nearRearr-dE.txt")
u_RMS = np.loadtxt("N=31 nonpaired/nearRearr-RMS.txt")

plt.plot(dE, RMS, 'o', color = "lightgrey", label="paired", markeredgecolor='k')
plt.plot(dE[PR<1.5], RMS[PR<1.5], 'o', color = "purple", label="paired", markeredgecolor='k')
plt.plot(u_dE, u_RMS, '.', color = "orange", label="unpaired", markeredgecolor='k')
plt.yscale("log")
plt.xscale("log")
plt.xlabel(r"P(|$\Delta E$|)")
plt.ylabel(r"P(|$\Delta$|)")
plt.tight_layout()
plt.show()
plt.clf()
