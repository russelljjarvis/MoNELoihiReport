import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
st.title("Lava Spike Train Processing Exercise...")

st.markdown("[Link to Code That Generated The Plots:](https://github.com/russelljjarvis/lava/blob/main/tutorials/end_to_end/tutorial02_excitatory_inhibitory_network.ipynb)")

st.markdown("# the List of Data Files:")
files = glob.glob("pickle/*.p")


labels = "see file names?"
options = ["no","yes"]
radio_out_f = st.sidebar.radio(labels,options)

if radio_out_f=="yes":
    st.sidebar.write(pd.DataFrame(pd.Series(files)))

labels = "tables or spike_raster?"
options = ["spk","tb"]
radio_out = st.sidebar.radio(labels,options)

labels = "regime: balanced, critical, critical_fixed?"
options = ["balanced","critical","critical_fixed"]
radio_out_r = st.sidebar.radio(labels,options)

dict_of_spike_file_contents = {}
dict_of_spike_file_contents.setdefault('balanced', [])
dict_of_spike_file_contents.setdefault('critical', [])
dict_of_spike_file_contents.setdefault('critical_fixed', [])

for f in files:
    with open(str(f),"rb") as fto:
        file_contents = pickle.load(fto)
        if len(file_contents[1].keys())>98:
            if str("pickle_0_") in f:
                if radio_out_r=="balanced":
                    dict_of_spike_file_contents["balanced"].append(file_contents)
            if str("pickle_1_") in f:
                if radio_out_r=="critical":
                    dict_of_spike_file_contents["critical"].append(file_contents)
            if str("pickle_2_") in f:
                if radio_out_r=="critical_fixed":
                    dict_of_spike_file_contents["critical_fixed"].append(file_contents)



def wrangle_frame(frame)->None:
    for c in frame.columns:
        frame[c].values[:] = pd.Series(frame[c])

    temp = frame.T
    if len(temp.columns)<2:       
        st.write(frame.T)
    else:
        st.markdown("""Print data not available""")

def plot_raster(spike_dict)->None:
    st.markdown("### The raster plot:")

    fig = plt.figure()
    list_of_lists = []
    for ind,(neuron_id,times) in enumerate(spike_dict.items()):
        list_of_lists.append(times)
    plt.eventplot(list_of_lists)
    st.pyplot(fig)

def wrangle(spike_dict)->[[]]:
    list_of_lists = []
    maxt=0
    for ind,(neuron_id,times) in enumerate(spike_dict.items()):
        list_of_lists.append(times)
        if np.max(times)> maxt:
            maxt = np.max(times)
    st.markdown("#### The Network Dimensions are as follows, Number of cells:")
    st.markdown(np.shape(list_of_lists))
    st.markdown("## Simulation Time Duration (ms):")
    st.markdown(maxt)
    return list_of_lists




spikes_in_list_of_lists_of_lists = []

for keys,values in dict_of_spike_file_contents.items():
    for x in values:
        st.markdown("## Network Regime: "+str(keys))
        #st.markdown(v)
        if radio_out == "tb":
            st.markdown("### The spike raster plot matrix as a table (column items cell index, row items spike times):")
            wrangle_frame(x[0])
        if radio_out == "spk":
            plot_raster(x[1])
        spikes_in_list_of_lists_of_lists.append(wrangle(x[1]))


def compute_ISI(spks):
    """
    Damien's code.
    """
    # hint spks is a 2D matrix, get a 1D Vector per neuron-id spike train.
    # [x for ind,x in enumerate(spks)]
    # spkList = [x for ind,x in enumerate(spks)]

    # st.markdown(spkList)
    # st.pyplot()
    # pass
    # return an array of ISI_arrays.


def compute_ISI_CV(spks):
    ISIs = compute_ISI(spks)
    # hint
    # [x for ind,x in enumerate(spks)]
    pass
    # return a vector of scalars: ISI_CV


def average(ISI_CV):
    # use numpy to mean the vector of ISI_CVs
    # return a scalar.
    pass

