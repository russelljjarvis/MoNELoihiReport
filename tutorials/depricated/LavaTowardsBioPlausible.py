
import pandas as pd

from lava.proc.lif.process import LIF
from lava.lib.dnf.connect.connect import connect
from lava.lib.dnf.operations.operations import Weights
from lava.magma.core.run_configs import Loihi1SimCfg #Loihi simulator, not  Loihi itself.
from lava.magma.core.run_conditions import RunSteps
from lava.proc.monitor.process import Monitor
from lava.proc.monitor.models import PyMonitorModel
from lava.lib.dnf.utils.plotting import raster_plot
import numpy as np
import elephant
import os
import matplotlib as mpl
haveDisplay = "DISPLAY" in os.environ
if not haveDisplay:
    mpl.use('Agg')

from tutorial06_hierarchical_processes import *
# # Pretend Cortical Model Specs:
# ## These numbers are nominal. 
# * The numbers simply fit the performance of a resource limited laptop
# * 2 columns.
# * 4 layers
# * 1 **E** pop and 1 **I** pop per layer.
# * 85 cells per population 170 cells per layer.

# 
# ### Create layerwise cell populations 

"""
ncolumns=2

# Ex excitatory
ly_2_3_ex = np.ndarray((ncolumns),dtype=object)
ly_4_ex = np.ndarray((ncolumns),dtype=object)
ly_5_ex = np.ndarray((ncolumns),dtype=object)
ly_6_ex = np.ndarray((ncolumns),dtype=object)

# In inhibitory
ly_2_3_in = np.ndarray((ncolumns),dtype=object)
ly_4_in = np.ndarray((ncolumns),dtype=object)
ly_5_in = np.ndarray((ncolumns),dtype=object)
ly_6_in = np.ndarray((ncolumns),dtype=object)

ncells = 10
for i in range(0,ncolumns):
    ly_2_3_ex[i] = LIF(shape=(ncells,))
    ly_4_ex[i] = LIF(shape=(ncells,))
    ly_5_ex[i] = LIF(shape=(ncells,))
    ly_6_ex[i] = LIF(shape=(ncells,))


    ly_2_3_in[i] = LIF(shape=(ncells,))
    ly_4_in[i] = LIF(shape=(ncells,))
    ly_5_in[i] = LIF(shape=(ncells,))
    ly_6_in[i] = LIF(shape=(ncells,))

    


# <h1 align="center"> Create the connectivity pattern </h1>
# 
# <h3> 
# There are three obvious ways to define connectivity:
#     * One to One
#     * Connectivity Matrix.    
# </h3>
# 
# <h4> 
# * First I apply the repeated/stereotyped connections whithin and between layers:
# </h4>


connections=[]

for i in range(0,ncolumns):
    
    one2onec = connect(ly_4_ex[i].s_out, ly_4_ex[i].a_in, ops=[Weights(1.0)])
    connections.append(one2onec)
    one2onec = connect(ly_5_ex[i].s_out, ly_5_ex[i].a_in, ops=[Weights(1.0)])
    connections.append(one2onec)

    one2onec = connect(ly_6_ex[i].s_out, ly_6_ex[i].a_in, ops=[Weights(1.0)])
    connections.append(one2onec)


# ## One to one synapse projections between layers


for i in range(0,ncolumns):
    #ly_2_3_in[i] 2 ly_2_3_in[i]
    one2onec = connect(ly_2_3_in[i].s_out, ly_2_3_in[i].a_in, ops=[Weights(-1.0)])
    connections.append(one2onec)
    #ly_4_in[i] 2 ly_4_in[i]
    one2onec = connect(ly_4_in[i].s_out, ly_4_in[i].a_in, ops=[Weights(-1.0)])
    connections.append(one2onec)
    #ly_5_in[i] 2 ly_5_in[i]
    one2onec = connect(ly_5_in[i].s_out, ly_5_in[i].a_in, ops=[Weights(-1.0)])
    connections.append(one2onec)
    #ly_6_in[i] 2 ly_6_in[i]
    one2onec = connect(ly_6_in[i].s_out, ly_6_in[i].a_in, ops=[Weights(-1.0)])
    connections.append(one2onec)

for i in range(0,ncolumns):
    #ly_2_3_ex[i] 2 ly_2_3_in[i]
    one2onec = connect(ly_2_3_ex[i].s_out, ly_2_3_in[i].a_in, ops=[Weights(1.0)])
    connections.append(one2onec)
    #ly_4_ex[i] 2 ly_4_in[i]
    one2onec = connect(ly_4_ex[i].s_out, ly_4_in[i].a_in, ops=[Weights(1.0)])
    connections.append(one2onec)
    #ly_5_ex[i] 2 ly_5_in[i]
    one2onec = connect(ly_5_ex[i].s_out, ly_5_in[i].a_in, ops=[Weights(1.0)])
    connections.append(one2onec)
    #ly_6_ex[i] 2 ly_6_in[i]
    one2onec = connect(ly_6_ex[i].s_out, ly_6_in[i].a_in, ops=[Weights(1.0)])
    connections.append(one2onec)

for i in range(0,ncolumns):
    #ly_2_3_in[i] 2 ly_2_3_exc[i]
    one2onec = connect(ly_2_3_in[i].s_out, ly_2_3_ex[i].a_in, ops=[Weights(-1.0)])
    connections.append(one2onec)
    #ly_4_in[i] 2 ly_4_exc[i]
    one2onec = connect(ly_4_in[i].s_out, ly_4_ex[i].a_in, ops=[Weights(-1.0)])
    connections.append(one2onec)
    #ly_5_in[i] 2 ly_5_exc[i]
    one2onec = connect(ly_5_in[i].s_out, ly_5_ex[i].a_in, ops=[Weights(-1.0)])
    connections.append(one2onec)
    #ly_6_in[i] 2 ly_6_exc[i]
    one2onec = connect(ly_6_in[i].s_out, ly_6_ex[i].a_in, ops=[Weights(-1.0)])
    connections.append(one2onec)



for i in range(0,ncolumns):
    one2onec = connect(ly_4_ex[i].s_out, ly_2_3_ex[i].s_out, ops=[Weights(1.0)])
    connections.append(one2onec)
    one2onec = connect(ly_4_ex[i].s_out, ly_5_ex[i].a_in, ops=[Weights(1.0)])
    connections.append(one2onec)
    one2onec = connect(ly_5_ex[i].s_out, ly_6_ex[i].a_in, ops=[Weights(1.0)])
    connections.append(one2onec)



one2onec = connect(ly_2_3_ex[0].s_out, ly_2_3_ex[1].s_out, ops=[Weights(1.0)])
connections.append(one2onec)
"""
ncells = 100
dim=(ncells,ncells)
weights0 = 0.0125*np.random.rand(ncells,ncells)
weights1 = weights0
#instantiate 2 DenseLayers
layer0 = DenseLayer(shape=dim,weights=weights0, bias=4, vth=10)
layer1 = DenseLayer(shape=dim,weights=weights1, bias=4, vth=10)
#connect layer 0 to layer 1
layer0.s_out.connect(layer1.s_in)

#many2onec = connect(ly_2_3_in[i].s_out, layer0.s_in, ops=[Weights(0.025)])
#one2onec = connect(ly_2_3_ex[0].s_out, ly_2_3_ex[1].s_out, ops=[Weights(1.0)])
#connections.append(one2onec)

dim=(ncells,ncells)
weights0 = 0.0125*np.random.rand(ncells,ncells)
weights1 = weights0
#instantiate 2 DenseLayers
layer0 = DenseLayer(shape=dim,weights=weights0, bias=4, vth=10)
layer1 = DenseLayer(shape=dim,weights=weights1, bias=4, vth=10)
#connect layer 0 to layer 1

layer0.s_out.connect(layer1.s_in)
many2onec = connect(layer0.s_out, layer0.s_in, ops=[Weights(-0.15)])
#connections.append(many2onec)

#many2onec = connect(ly_2_3_ex[i].s_out, layer0.s_in, ops=[Weights(0.05)])
#connections.append(many2onec)

#many2onec = connect(ly_2_3_ex[i].s_out, layer0.s_in, ops=[Weights(0.05)])
#connections.append(one2onec)

# # Create tonic input for the network.

# # Run the preliminary Potjans model on CPU for 250ms
# 
# One awesome property of the Lava paradigm you only have to run a segment of the model to run the whole model.
# 
# Model segments seem to have parent child relationships with other segments if they are connected with network connections, and the Loihi compiler seems to understand that.

# # Set up the experimental recording rig


time_steps = 105
monitor_layer0 = Monitor()
monitor_layer0.probe(target=layer0.s_out, num_steps=time_steps)
monitor_ly_2_3_ex = Monitor()
#monitor_ly_2_3_ex.probe(target=ly_2_3_ex[0].s_out, num_steps=time_steps)
#monitor_ly_2_3_in = Monitor()
#monitor_ly_2_3_in.probe(target=ly_2_3_in[0].s_out, num_steps=time_steps)
#monitor_ly_4_ex = Monitor()
#monitor_ly_4_ex.probe(target=ly_4_ex[0].s_out, num_steps=time_steps)
#monitor_input_1 = Monitor()
#monitor_input_1.probe(spike_generator_1.s_out, time_steps)
#other_column = Monitor()
#other_column.probe(ly_2_3_ex[1].s_out, time_steps)
layer0.amplitude = 100
layer0.run(condition=RunSteps(num_steps=time_steps),
        run_cfg=Loihi1SimCfg(select_tag='floating_pt'))



data_input1 = monitor_input_1.get_data()[spike_generator_1.name][spike_generator_1.s_out.name]
#data_ly_2_3_ex = monitor_ly_2_3_ex.get_data()[ly_2_3_ex[0].name][ly_2_3_ex[0].s_out.name]
#data_ly_2_3_in = monitor_ly_2_3_in.get_data()[ly_2_3_in[0].name][ly_2_3_in[0].s_out.name]
#data_ly_4_ex = monitor_ly_4_ex.get_data()[ly_4_ex[0].name][ly_4_ex[0].s_out.name]
#data_ly_4_ex = monitor_ly_4_ex.get_data()[ly_4_ex[0].name][ly_4_ex[0].s_out.name]

data_l1=monitor_layer0.get_data()[layer0.name][layer0.s_out.name]




raster_plot(data_input1.T)
cv = compute_cv(data_input1)
print("The coefficient of variation is {0}".format(cv))


# In[19]:


raster_plot(data_l1.T)
cv = compute_cv(data_l1.T)

print("The coefficient of variation is {0}".format(cv))


# In[20]:


raster_plot(data_ly_2_3_ex.T)
cv = compute_cv(data_ly_2_3_ex)
print("The coefficient of variation is {0}".format(cv))


# In[21]:


raster_plot(data_ly_4_ex.T)
cv = compute_cv(data_ly_4_ex)
print("The coefficient of variation is {0}".format(cv))
total = np.hstack([data_ly_2_3_ex.T,data_ly_4_ex.T])
raster_plot(total)


# In[22]:


raster_plot(data_ly_2_3_in.T)
cv = compute_cv(data_ly_2_3_in)
print("The coefficient of variation is {0}".format(cv))


# In[23]:


raster_plot(data_ly_2_3_ex.T)
cv = compute_cv(data_ly_2_3_ex)
print("The coefficient of variation is {0}".format(cv))


# * Check to see spiking activity propogated from one column to the other via a dedicated connection

# In[24]:


data_ly_2_3_ex_other = other_column.get_data()    [ly_2_3_ex[1].name][ly_2_3_ex[1].s_out.name]
raster_plot(data_ly_2_3_ex_other.T)
cv = compute_cv(data_ly_2_3_ex_other)
print("The coefficient of variation is {0}".format(cv))

