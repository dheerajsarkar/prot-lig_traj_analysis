#!/usr/bin/env python
# coding: utf-8

# In[1]:


from htmd.ui import *
import pyemma

# In[2]:
import matplotlib
import matplotlib.pyplot as plt
def save_figure(name):
    # change these if wanted
    do_save = True
    if do_save:
        plt.savefig(name, bbox_inches='tight', dpi=300)


# In[3]:
get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:
import os, glob
sims = simlist(glob.glob("/mnt/labbit1/Work_dir/HTMD/CaverDock/run_htmd_2/filtered_traj/*/")[:900], ("/mnt/labbit1/Work_dir/HTMD/CaverDock/run_htmd_2/filtered_traj/filtered.pdb"))


# In[29]:
metr = Metric(sims)
metr.set(MetricDistance('protein and name CA', 'resname DBE and noh', periodic='selections', metric='distances'))
data = metr.project()


# In[30]:
data.fstep = 0.1
data.map[:10]


# In[31]:
tica = TICA(data, 3, units='ns')
dataTica = tica.project(3)


# In[32]:
dataBoot = dataTica.bootstrap(0.8)


# In[33]:
dataBoot.cluster(MiniBatchKMeans(n_clusters=1000))


# In[34]:
model = Model(dataBoot)


# In[35]:
model = Model()


# In[36]:
model.load('/home/dheeraj/Work_Dir/Schemes/CaverDock/CaverDock_final/run_htmd_2/htmd/model_s4_r3.dat')


# In[38]:
its = model.plotTimescales(nits=10, results=True)


# In[39]:
model.markovModel(20, 7, units='ns')


# In[13]:
path = "/home/dheeraj/Work_Dir/Schemes/CaverDock/CaverDock_final/run_htmd_0/htmd/spectral-seperation/bi_directional_tpt/"
model.save(path + "model_s4_r1.dat")


# In[27]:
Nsim = 15016.0  # number of water molecules in our simulation
Nstd = 55.55  # number of water molecules in standard volume
conc = Nstd / Nsim
print(conc)


# In[40]:
kin = Kinetics(model, temperature=310, concentration=0.0037561)
r = kin.getRates()
print(r)


# In[20]:
kin.mfptGraph()
from matplotlib import pyplot as plt
import matplotlib
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
matplotlib.rcParams['legend.fontsize'] = 30


# In[18]:
model.viewStates(ligand="resname DBE and noh", numsamples=50, wrapsel='protein')