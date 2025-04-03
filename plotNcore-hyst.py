#######################################################################################
#
# Takes files made by findNNeededLV.py and records
# number of particles needed to move
# from one well to the other as a function of strain
# along the hysteron. Plots as in Fig. 4a
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
from scipy.optimize import curve_fit

#folderName = str(sys.argv[1])

matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
#plt.rcParams["figure.figsize"] = (3.4,2.2)
plt.rcParams["figure.figsize"] = (5,3)
#plt.rcParams['text.usetex'] = True

tol = 1e-15
#will append relative hysteron position and NList

headerLen = 2
numBins = 10

numPackingsList = []
folderList = ["hyst/1e-3-NNeeded-large/", \
"hyst/1e-3-NNeeded-small/", \
"hyst/1e-4-NNeeded-small/", \
"hyst/1e-5-NNeeded-small/"]
totalList = []
hystList = []
weirdCount = 0
numPackings = 0
totalCount = 0
for kk in range(len(folderList)):
    
    Ncore = []
    hysts = []
    dirname = folderList[kk]
    for filename in os.listdir(dirname):

        N = 31
        N_list = [0,1,2,4,8,16,31]

        nNeededList = []
        if "Upward" in filename:
            totalCount += 1
            with open(dirname + filename) as csvfile:
                data = csv.reader(csvfile, delimiter='\t')
                a = 0
                weird = False
                for row in data:
                    a += 1
                    if a > headerLen:
                        counter = 0
                        for ii in range(len(row) - 3):
                            if np.abs(float(row[ii+1]) - float(row[1])) < tol:
                                counter += 1
                            elif float(row[ii+1]) > tol:
                                weird = True
                            if ii==0 and float(row[ii+1])<tol and a < 13:
                                weird = True
                        if a==headerLen + 1:
                            botStrain = float(row[0])
                        elif a==headerLen + 11:
                            topStrain = float(row[0])
                        nNeededList.append(N_list[counter])
                hysts.append(topStrain-botStrain)
                nNeededList.pop(-1)
                removeList = []
                for mm in range(len(nNeededList)):
                    if nNeededList[mm] == 0:
                        print("got a zero, packing " + str(filename))
                        removeList.append(mm)
                for nn in range(len(removeList)):
                    nNeededList.pop(len(removeList) - 1 - nn)

                if (weird==False):
                    numPackings += 1
                    Ncore.append(nNeededList)
                    #plt.plot(nNeededList, 'o')
                    #plt.show()
                    #plt.clf()

                elif (weird==True):
                    #print("weird in file " + str(filename))
                    weirdCount += 1

    totalList.append(Ncore)
    hystList.append(hysts)

#print(float(weirdCount)/float(totalCount))

bins = 10
x = np.linspace(0, 1, bins)


shapeList = ['x-', 'o-', '^-', 's-']
cmap = cm.get_cmap("viridis")
colorList = [cmap(0.125), cmap(0.375), cmap(0.625), cmap(0.875)]

plt.rcParams["figure.figsize"] = (3.4,2.4)
a = 0
for ii in range(len(totalList)):

    print(len(totalList[ii]))

    ave = np.mean(hystList[ii])
    plt.plot(np.linspace(0,1,num=numBins), \
    np.mean(np.array(totalList[ii]),axis=0), \
    "-o", color=colorList[ii], markeredgecolor='k', \
    label=r"$\langle \gamma_h \rangle$ = {a:.1E}".format(a=ave))

plt.legend()
plt.xlabel(r"$\gamma^*$")
plt.ylabel(r"$N_{core}$")
plt.tight_layout()
plt.show()
plt.clf()
