#######################################################################################
# 
# Reads in data from about rearrangement paris and plots the data in Fig. 2
#
#######################################################################################

import numpy as np
#import pyCudaPacking as pcp
#import npquad
import sys
import time
import matplotlib
import matplotlib.pyplot as plt
import os
import csv
#from scipy.optimize import curve_fit
import scipy.stats as ss
from matplotlib import cm

matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
plt.rcParams["figure.figsize"] = (3.4,2.2)

N_list = [7, 17, 31, 61, 127, 257, 509, 1021]
for ii in range(len(N_list)):
    x = np.loadtxt("N_" + str(N_list[ii]) + "-strains.txt", usecols=1, skiprows=2)
    a = float(len(x))
    plt.plot(N_list[ii], 200/(a + 200), 'o', color="teal", markeredgecolor="k")

plt.ylim([0,0.8])
plt.xscale("log")
plt.xlabel(r"$N$")
plt.ylabel("P(pair)")
plt.tight_layout()
plt.show()
plt.clf()


N_list = [31]
for ii in range(len(N_list)):
    x = np.loadtxt("N_31-periodicEndsData.txt", skiprows=1, usecols=6)[::2]
    L_31 = x.astype(float)
    P = ss.expon.fit(L_31)
    rX = np.linspace(np.min(L_31),np.max(L_31),1000)
    rP = ss.expon.pdf(rX, *P)
    #NPointsPerBin = 10
    #bins = np.unique(np.hstack([np.sort(L_31)[::NPointsPerBin], np.max(L_31)]))
    plt.hist(x=L_31, bins=100, density=True, log=False, histtype="step", \
    linewidth=1.5, label="N=31", color='teal')
    plt.plot(rX, rP, '--', color='k', label="exponential fit")
#plt.plot((bins[1:]+bins[:-1])/2.0, n, 'o', color='teal', markeredgecolor='k')
#plt.plot(rX, rP, '--', linewidth=1.0, color='k', label="fit")
plt.xlabel(r"$\gamma_h$")
plt.ylabel(r"P($\gamma_h$)")
plt.yscale("log")
plt.ylim([10,5.5e2])
plt.xlim([0,0.03])
plt.tight_layout()
plt.show()
plt.close()


lambdas = []
N_list = [7, 17, 31, 61, 127, 257, 509, 1021]
for ii in range(len(N_list)):
    x = np.loadtxt("N_" + str(N_list[ii]) + "-periodicEndsData.txt", skiprows=1, usecols=6)[::2]
    x = x.astype(float)
    P = ss.expon.fit(x)
    lambdas.append(P[1])
plt.plot(N_list, lambdas, 'o', color="teal", markeredgecolor="k")
plt.xlabel(r"$N$")
plt.ylabel(r"$\lambda$")
plt.xscale("log")
plt.yscale("log")
plt.tight_layout()
plt.show()
plt.clf()

