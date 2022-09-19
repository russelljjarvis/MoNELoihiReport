
from tutorial06_hierarchical_processes import *
import numpy as np
from lava.magma.core.run_configs import RunConfig, Loihi1SimCfg
from lava.magma.core.run_conditions import RunSteps
from lava.proc.io import sink, source

dim = (30, 30)
# Create the weight matrix.
weights0 = np.zeros(shape=dim)
weights0[1,1]=1
weights1 = weights0
# Instantiate two DenseLayers.
layer0 = DenseLayer(shape=dim, weights=weights0, bias_mant=4, vth=10)
layer1 = DenseLayer(shape=dim, weights=weights1, bias_mant=4, vth=10)
# Connect the first DenseLayer to the second DenseLayer.
layer0.s_out.connect(layer1.s_in)

print('Layer 1 weights: \n', layer1.weights.get(),'\n')
print('\n ----- \n')

rcfg = Loihi1SimCfg(select_tag='floating_pt', select_sub_proc_model=True)

for t in range(100):
    # Run the entire network of Processes.
    layer1.run(condition=RunSteps(num_steps=1), run_cfg=rcfg)
    print('t: ',t)
    #print('Layer 0 v: ', layer0.v.get())
    #print('Layer 1 u: ', layer1.u.get())
    #print('Layer 1 v: ', layer1.v.get())
    #print('Layer 1 spikes: ', layer1.spikes.get())
    #print('\n ----- \n')
print("did we stop?")
layer1.stop()