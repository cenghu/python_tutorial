# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:01:12 2018

@author: ChenHu
"""
# import some packages for computing and plotting
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# part 1: data analysis
#import csv datafile, sep: delimiter to use, skiprows: number of lines to be skiped
database_4D=pd.read_csv('database_4D.csv', sep=';', skiprows=2)

#sort the dataframe by value of the column with header "Pmax"
database_4D=database_4D.sort_values(by=['Pmax'])

Pmax=database_4D.iloc[:,3] # put column index number 3 into Pmax, index starts from 0
KSt=database_4D.iloc[:,4] # put column index number 4 into KSt

# use polyfit for fitting Pmax and KSt using 2nd order polynomial by least squared errors
fit, residual, _, _, _ = np.polyfit(Pmax,KSt,2,full=True) #play around with polynomial orders

# fit_fn the fit function
fit_fn = np.poly1d(fit)

#calculate the fit values based on the approximation function
KSt_approx=fit_fn(Pmax)

# relative error of max and mean
rel_error_max=max(abs(KSt_approx-KSt)/KSt)
rel_error_mean=np.mean(abs(KSt_approx-KSt)/KSt)


# part 2: data plot
#set all the font size 20
font = {'size'   : 20}
plt.rc('font', **font)
plt.rc('figure', figsize=(6.4, 4.8))
cm = plt.cm.get_cmap('RdYlBu') #get red yellow blue color map
#plot    
plt.clf() # clear the current figure

#scattered plot, s: marker size, c: marker color, cmap: color map, alpha: between 0(transparent) and 1 (opaque)
sc=plt.scatter(Pmax,KSt, s=database_4D.iloc[:,1]*2.5, 
               c=database_4D.iloc[:,2], alpha=0.4, edgecolors='k', cmap=cm)

plt.plot(Pmax,fit_fn(Pmax), color='k',linestyle='-',lw=2) # fit plot
#plot the data from the current experiment

plt.colorbar(sc)
plt.xlabel('Pmax [bar]')
plt.ylabel('KSt [bar m/s]')

# text of color color map name, xy: point to annotate, xycoords: fraction of figure from lower left
plt.annotate(r'moisture content [%]',
             xy=(0.7, 1.03), xycoords='axes fraction',
              fontsize=15)

plt.grid(True,linestyle='dashed')
# fix the tickers
ax = plt.gca()
ax.minorticks_on()
ax.tick_params(axis='both',direction='in', which='minor',length=5,width=1,labelsize=18)
ax.tick_params(axis='both',direction='in', which='major',length=8,width=1,labelsize=18)

#automatically fit the content within figure
plt.tight_layout()
plt.savefig("PmaxKStStatistic.jpg",format='jpg', dpi=1000)
plt.savefig("PmaxKStStatistic.png",format='png', dpi=1000)
plt.savefig('PmaxKStStatistic.eps',format='eps', dpi=1000)
plt.show()
