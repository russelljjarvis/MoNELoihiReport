import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
st.title("Lava Spike Train Processing Exercise...")

st.markdown("[Link to Code That Generated The Plots:](https://github.com/russelljjarvis/lava/blob/main/tutorials/end_to_end/tutorial02_excitatory_inhibitory_network.ipynb)")

files = glob.glob("pickle/*.p")



labels = "see file names?"
options = ["no","yes"]
radio_out_f = st.sidebar.radio(labels,options)

if radio_out_f=="yes":
    st.sidebar.markdown("# the List of Data Files:")

    st.sidebar.write(pd.DataFrame(pd.Series(files)))

labels = "tables or spike_raster?"
options = ["spk","tb"]
radio_out = st.sidebar.radio(labels,options)

labels = "regime: balanced, critical, critical_fixed?"
options = ["balanced","critical","critical_fixed"]
radio_out_r = st.sidebar.radio(labels,options)

def raster_plot(spks, stride=1, fig=None, color='b', alpha=1):
    """Generate raster plot of spiking activity.
    
    Parameters
    ----------
    
    spks : np.ndarray shape (num_neurons, timesteps)
        Spiking activity of neurons, a spike is indicated by a one    
    stride : int
        Stride for plotting neurons
    """
    if type(spks) is type(List):
        spks = np.array(spks)
    else:
        pass    

    num_time_steps = spks.shape[1]
    assert stride < num_time_steps, "Stride must be smaller than number of time steps"
    
    time_steps = np.arange(0, num_time_steps, 1)
    if fig is None:
        fig = plt.figure(figsize=(10,5))
    timesteps = spks.shape[1]
    
    plt.xlim(-1, num_time_steps)
    plt.yticks([])
    
    plt.xlabel('Time steps')
    plt.ylabel('Neurons')
    
    for i in range(0, dim, stride):
        spike_times = time_steps[spks[i] == 1]
        plt.plot(spike_times,
                 i * np.ones(spike_times.shape),
                 linestyle=' ',
                 marker='o',
                 markersize=1.5,
                 color=color,
                 alpha=alpha)
        
    return fig       

def load_files(files:[])->dict:

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
    return dict_of_spike_file_contents

dict_of_spike_file_contents = load_files(files)


def wrangle_frame(frame)->None:
    for c in frame.columns:
        frame[c].values[:] = pd.Series(frame[c])

    temp = frame.T
    if len(temp.columns)<2:       
        st.write(frame.T)
    else:
        st.markdown("""Print data not available""")



def plot_raster(spike_dict:dict)->None:
    st.markdown("### The raster plot:")

    fig = plt.figure()
    list_of_lists = []
    for ind,(neuron_id,times) in enumerate(spike_dict.items()):
        list_of_lists.append(times)
    plt.eventplot(list_of_lists)
    st.pyplot(fig)

def wrangle(spike_dict:dict)->[[]]:
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




uploaded_file = st.sidebar.file_uploader("Upload Spike Trains To Compute CV on.")
if uploaded_file is not None:
    spks_dict_of_dicts = pickle.loads(uploaded_file.read())
    st.write("spikes loaded")
    st.markdown(spks_dict_of_dicts)
else:
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
                try:
                    raster_plot(x[2])
                except:
                    st.markdown(x[2])
                    st.markdown(type(x[2]))
            spikes_in_list_of_lists_of_lists.append(wrangle(x[1]))


def compute_ISI(spks:[])->[]:
    """
    """
    # hint spks is a 2D matrix, get a 1D Vector per neuron-id spike train.
    # [x for ind,x in enumerate(spks)]
    # spkList = [x for ind,x in enumerate(spks)]

    # st.markdown(spkList)
    # st.pyplot()
    # pass
    # return an array of ISI_arrays.


def compute_ISI_CV(spks:[])->[]:
    ISIs = compute_ISI(spks)
    """
    """
    # hint
    # [x for ind,x in enumerate(spks)]
    pass
    # return a vector of scalars: ISI_CV


def average(ISI_CV:[])->float:
    """
    """
    # use numpy to mean the vector of ISI_CVs
    # return a scalar.
    pass

