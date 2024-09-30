#!/usr/bin/env python
# coding: utf-8

# In[461]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib import ticker

# caculation of distance counts from variuos schemes
rep1 = pd.read_csv("/home/dheeraj/Work_Dir/Schemes/All_Dist/epoch_20/scheme-4/dist_e20_s4_r1.csv", header=0)
rep2 = pd.read_csv("/home/dheeraj/Work_Dir/Schemes/All_Dist/epoch_20/scheme-4/dist_e20_s4_r2.csv", header=0)
rep3 = pd.read_csv("/home/dheeraj/Work_Dir/Schemes/All_Dist/epoch_20/scheme-4/dist_e20_s4_r3.csv", header=0)

x1 = rep1.iloc[:, 20].dropna()
x2 = rep2.iloc[:, 20].dropna()
x3 = rep3.iloc[:, 20].dropna()

ranges = [0,5,19,100]

print("Total values for rep1: ", x1.count())
print("counts of distances for rep1: ", x1.groupby(pd.cut(x1, ranges)).count())

print("Total values for rep2: ", x2.count())
print("counts of distances for rep2: ", x2.groupby(pd.cut(x2, ranges)).count())

print("Total values for rep3: ", x3.count())
print("counts of distances for rep3: ", x3.groupby(pd.cut(x3, ranges)).count())


# In[1]:

# Plot histogram

rep1 = pd.read_csv("/home/dheeraj/Work_Dir/Schemes/All_Dist/scheme-1/dist_s1_r1.csv", header=0)
rep2 = pd.read_csv("/home/dheeraj/Work_Dir/Schemes/All_Dist/scheme-1/dist_s1_r2.csv", header=0)
rep3 = pd.read_csv("/home/dheeraj/Work_Dir/Schemes/All_Dist/scheme-1/dist_s1_r3.csv", header=0)

shade = shade = np.arange(0.0, 200000, 10)

rep1 = rep1.iloc[:, 20].dropna()
rep2 = rep2.iloc[:, 20].dropna()
rep3 = rep3.iloc[:, 20].dropna()

ticks = ['0','20k', '40k', '60k', '80k', '100k', '120k']

# shared_bins = np.histogram_bin_edges(x1, bins='auto', range=(x1.min(), x1.max()))
# bins=x1.max() # for bins
fig, ax = plt.subplots(figsize=(9,6))
plt.style.use('default')
plt.hist(rep1, bins=54, histtype='step', label='replicate 1', color='blue')
plt.hist(rep2, bins=54, histtype='step', label='replicate 2', color='green')
plt.hist(rep3, bins=55, histtype='step', label='replicate 3', color='magenta')


plt.xlabel('Catalytic COM $\Leftrightarrow$ DBE COM $(\AA)$', fontsize=18)
plt.ylabel('Count', fontsize=22)
plt.xlim(0.0, 60.0)
plt.ylim(0.0, 125000)
# plt.ylim(0.0, 100000)
plt.fill_betweenx(shade, 0.0, 5, where=None, facecolor='gold', alpha=0.4)
plt.fill_betweenx(shade, 5, 14, where=None, facecolor='salmon', alpha=0.3)
plt.fill_betweenx(shade, 14, 19, where=None, facecolor='salmon', alpha=0.1, hatch='///', zorder=0, edgecolor="r", linewidth=1.0)
plt.fill_betweenx(shade, 19, 60, where=None, facecolor='white', alpha=0.2)

plt.grid(axis='y', linestyle = "--", zorder=0)
plt.xticks(fontsize=18)
ax.xaxis.set_minor_locator(MultipleLocator(5))
ax.yaxis.set_major_formatter(ticker.FixedFormatter(ticks))
plt.yticks(fontsize=18)
plt.legend(loc="upper center", ncol=5, fontsize=15, bbox_to_anchor=(0,0,1,1.11))
# plt.legend(fontsize=18)
# plt.title("Bulk", fontweight=10, fontsize=18, color="k", y=1.0, pad=15)
plt.tight_layout()
plt.savefig('/home/dheeraj/Work_Dir/Schemes/All_Dist/scheme-1/CatalCOM_DBECOM_Counts_scheme-1.png', dpi=300)

