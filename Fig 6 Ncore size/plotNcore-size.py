#######################################################################################
#
# Takes files made by findNNeededLV.py and records 
# number of particles needed to move
# from one well to the other as a function of strain
# along the hysteron. Plots as in Fig. 6
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

type = "size" # hyst or size

numPackingsList = []

folderList = ["size/N_7-NNeeded/", \
"size/N_17-NNeeded/", \
"size/N_31-NNeeded/", \
"size/N_61-NNeeded/", \
"size/N_127-NNeeded/", \
"size/N_257-NNeeded/", \
"size/N_509-NNeeded/", \
"size/N_1021-NNeeded/"]
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
        print(dirname)

        if "N_7" in dirname:
            N = 7
            N_list = [0,1,2,4,7]
        elif "N_17" in dirname:
            N = 17
            N_list = [0,1,2,4,8,17]
        elif "N_31" in dirname:
            N = 31
            N_list = [0,1,2,4,8,16,31]
        elif "N_61" in dirname:
            N = 61
            N_list = [0,1,2,4,8,16,32,61]
            print("61")
        elif "N_127" in dirname:
            N = 127
            N_list = [0,1,2,4,8,16,32,64,127]
        elif "N_257" in dirname:
            N = 257
            N_list = [0,1,2,4,8,16,32,64,128,257]
        elif "N_509" in dirname:
            N = 509
            N_list = [0,1,2,4,8,16,32,64,128,256,509]
        elif "N_1021" in dirname:
            N = 1021
            N_list = [0,1,2,4,8,16,32,64,128,256,512,1021]

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


labelsList = ["N=7", "N=17", "N=31", "N=61", "N=127", "N=257", "N=509", "N=1021"]
scaleList = [7,17,31,61,127,257,509,1021]
colorList = cm.get_cmap("plasma", len(folderList) + 1)

ref = (np.mean(np.array(totalList[0]),axis=0) - 1.0)
def func_rescale(x, c):
    return x / c

rescale_fit = []
rescale_fit.append(1.0)
for ii in range(len(totalList)-1):
    popt, pcov = curve_fit(func_rescale, (np.mean(np.array(totalList[ii+1]),axis=0) - 1.0), \
    ref, p0=np.asarray([1]))
    rescale_fit.append(popt[0])
x = np.linspace(7,1021,num=100)

plt.rcParams["figure.figsize"] = (3.4,2.4)
for ii in range(len(totalList)):

    print(labelsList[ii] + ": " + str(len(totalList[ii])))

    plt.plot(np.linspace(0,1,num=numBins), \
    ((np.mean(np.array(totalList[ii]),axis=0)-1)/(rescale_fit[ii]*a)), \
    'o-', color=colorList.colors[ii], markeredgecolor='k', \
    label=labelsList[ii])# + ", ave over " + str(numPackingsList[ii]))

plt.xlabel(r"$\gamma$")
plt.ylabel(r"$(N_{core}-1)/N$")
plt.legend()
plt.tight_layout()
plt.show()
plt.clf()
