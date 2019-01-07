# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 10:01:12 2018

@author: ChenHu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#set all the font size 20
font = {'size'   : 20}
plt.rc('font', **font)
plt.rc('figure', figsize=(6.4, 4.8))

database_4D=pd.read_csv('database_4D.csv', sep=';', skiprows=0, header=0,encoding='windows-1252')

database_4D=database_4D.sort_values(by=['Pmax'])

Pmax=database_4D.iloc[:,3]
KSt=database_4D.iloc[:,4]
# use polyfit for fitting Pmax and KSt by least squared errors
fit, residual, _, _, _ = np.polyfit(Pmax,KSt,2,full=True)

# fit_fn the fit function
fit_fn = np.poly1d(fit)

KSt_approx=fit_fn(Pmax)

# relative error of max and mean
rel_error_max=max(abs(KSt_approx-KSt)/KSt)
rel_error_mean=np.mean(abs(KSt_approx-KSt)/KSt)


cm = plt.cm.get_cmap('RdYlBu')
#plot    
plt.clf()

#fill_colors = ['#4169e1' if MC<=5. else '#000000' for MC in list(databasePmaxKst_yesD50_yesMc['MC'])]
sc=plt.scatter(Pmax,KSt, s=database_4D.iloc[:,1]*2.5, 
               c=database_4D.iloc[:,2], alpha=0.4, edgecolors='k', cmap=cm)

plt.plot(Pmax,fit_fn(Pmax), color='k',linestyle='-',lw=2)
#plot the data from the current experiment

plt.colorbar(sc)
plt.xlabel('$P_\mathrm{max}$ [bar]')
plt.ylabel('$K_{St}$ [bar$\cdot$m/s]')
#lgd=plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0., fontsize='small')

plt.annotate(r'moisture content [%]',
             xy=(0.7, 1.03), xycoords='axes fraction',
              fontsize=15)
#plt.axis([0, 10, 0, 200])
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
