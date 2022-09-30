
<h1 align="center">
      Guide for the Tutorial 
      Headless Linux for Hardware: Navigating the Intel Loihi Superhost 
</h1>

<h3 align="center">
    Russell Jarvis post-doctoral researcher at ICNS.
    r.jarvis@westernsydney.edu.au
</h3>


## House Keeping on Last Weeks Tutorial

### Streamlit applications.

The streamlit module/object includes all of the methods that you would use to present things to the app screen. You can run python files that import the streamlit app, by running the command 

```BASH
streamlit run python_file.py
```

The following app code and repository does not depend on Lava (to make life easier for you). The app code is very simple to install as it only depends on numpy, streamlit, and matplot lib, its not actually doing network scale computations its just loading cached data. It is simple enough to run on your own machine, to run just do: 
```BASH 
pip install streamlit
git clone fun-zoological-computing/MoNELoihiTutorial
cd Loihi_hardware_tutorial
streamlit run app.py
```
Edit the file app.py in visual studio or to add figure captions or ISI and ISI_CV calculations.

### Caption 2 or More of 10 Different Figures. 

* If you choose to caption figures that belong to different network regimes you can refer back to the Ipython notebook to describe  reflect these four different conditions (Balanced, Critical and Critical Fixed).

The 12 network configurations belong to three different regimes you can refer back to the Ipython notebook to understand the properties of the three different conditions (Balanced, Critical and Critical Fixed).

* 


### Balanced
|             | Simulation Time 1000ms | Simulation Time 2000ms |  
| ----------- | ----------- | ----------- | 
| Network Size 100 | plot0 | plot1 | 
| Network Size 200 | plot2 | plot3 | 

### Critical

|             | Simulation Time 1000ms | Simulation Time 2000ms |  
| ----------- | ----------- | ----------- | 
| Network Size 100 | plot0 | plot1 | 
| Network Size 200 | plot2 | plot3 | 

### Critical Fixed 

|             | Simulation Time 1000ms | Simulation Time 2000ms |  
| ----------- | ----------- | ----------- |
| Network Size 100 | plot0 | plot1 | 
| Network Size 200 | plot2 | plot3 | 


### Streamlit application Interactive Web application 

#### Why Would You Develop an App?

Apps are great ways to share your tools and work with the outside world. Often you can use apps as examples in code portfolios. I have provided boiler plate code and established packages that calculate spike time co-efficient of variation $ CV $ and spike train distance. re-apply this template code on Loihi network simulator activity to regular periodic firing and irregular firing network activity. For low and high variability of spike times, comment on the ability of neurons to encode information if each unique interspike interval represents a unique feature or property.

The Coefficient of variation is: $ CV=\frac{Var(ISI_Vec)}{mean(ISI_Vec)} $


* Compute the inter-spike intervals of spike times.
  * If spike times are in an array, you want get the delta between ```spk_times[1]-spk_times[0], and spk_times[2]- spk_times[1], ..., spk_times[N]- spk_times[N-1]```.
    * Each of these deltas constructed from pairs will be the element of an array called ISI.
* Compute the coefficient of variation of Interspike intervals of spike trains. $var(ISI)/mean(ISI)$. This a measure of dispersal, ie spike interval irregularity.
* Get the mean CV of a population of cells.
* Regular asynchronous spiking.

### Bonus points 
Make the App Calculate $ ISI_{CV} $ on uploaded spikes.

### Other Background:
<h4> Resevoir Computing and Balanced E/I networks. </h4>

* Lava now supports STDP and "balanced" Excitatory/Inhibitory biological networks, however, whether any one can install and run them is a different question. I have managed the task of installing, these big packages using streamlit for you.

* Take the spike trains corresponding to cells 18 and 23 [](https://github.com/lava-nc/lava/blob/main/tutorials/end_to_end/tutorial02_excitatory_inhibitory_network.ipynb
) of the notebook. Flesch out the skeleton methods provided on [](https://github.com/fun-zoological-computing/MoNELoihiTutorial/blob/main/app.py#L101-L126) to compute the Interspike Interval arrays and the Coefficient of Variation of the spike trains.

Use your GitHub account to invite yourself to streamlit-cloud aka streamlit share.

![](https://streamlit.io/cloud)
Streamlit-share is able to build applications from git repositories

Edit the files in the web and flesch out the missing functions for computing $ CV_{ISI} $, caption some of or all of the raster plots in the app with the CV. 



[Functions are here:](https://github.com/russelljjarvis/lava/blob/main/app.py#L723-L738)

```python
def compute_ISI(spks):
    # hint spks is a 2D matrix, get a 1D Vector per neuron-id spike train.
    # [x for ind,x in enumerate(spks)]
    pass
    # return an array of ISI_arrays.

def compute_ISI_CV(ISI_array):
    # hint
    # [x for ind,x in enumerate(spks)]
    pass
    # return a vector of scalars: ISI_CV

def average(ISI_CV):
    # use numpy to mean the vector of ISI_CVs
    # return a scalar.
    pass
```





