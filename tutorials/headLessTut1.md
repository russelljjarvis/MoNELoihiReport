
<h1 align="center">
      Guide for the Tutorial 
      Headless Linux for Hardware: Navigating the Intel Loihi Superhost 
</h1>

<h3 align="center">
    Russell Jarvis post-doctoral researcher at ICNS.
    r.jarvis@westernsydney.edu.au
</h3>

### Take Home Assessment
Weight: $ 30% $
Type of Collaboration: Individual
Submission: Weeks 9 by Friday 11:59pm (midnight) Turnit in, or a optionally Markdown file on Github.

Format: The report will consist of $1000-1200$ words and several figures. The purpose of this report is to demonstrate the completion of assigned preworks and labworks in programming Loihi. References, quotes, and appendices are not part of the word count.
Length: $1200$ words.


Todays tutorial is the easier of the two tutorials.

### Assessable parts of todays tutorial:


Most of the exercises are worth one mark if you describe them as in the report next week. The work we cover today will add up to 15 available points that will be marked on the final report.


### You have configured ssh on your personal computer, congratulations for that!


### Background

Ways to access POSIX compliant terminals: OSX Terminal, Ubuntu Terminal, GitBash (for Windows) or Windows sub-system for Linux (WSL), `Docker run -it`, the list goes on and on. Probably every major operating system supports either BASH, or some other POSIX compliant shell (Powershell is POSIX compliant). 

### For the first of two tutorials we will:
* Secure Shell (ssh). Note to "ssh" is meant as a verb in this context. We will ssh into the Intel superhost and navigate the Linux environment.
* Use secure copy (scp) and pip to install lava version tag 0.3.0 (the penultimate version).
* Hopefully run a trivial lava programm using SLURM=1.
* `scp` the output of a lava simulation back to our local computer so we can comment on it.


### Background:

### Why Headless Linux?
On High Performance Computers, Docker-containers, and resource restricted hardware environments: Raspberri-PI, NVIDIA Jetson Nano etc. A "head-less" Linux login is default interface for accessing the resource. There are multiple reasons for this:

* 1. A graphical Operating System (OS) acts as a large memory and CPU and load. On a raspberri-pi you will likely prefer to keep all the RAM and CPU for developing applications. Trying to use the graphical OS will likely be unresponsive and clunky anyway, as it is on the Nvidia Jetson Nano. 

* 2. On a super-computer, such as the Intel Superhost, login nodes are shared between groups of 10 or more users. Command Line Interface (CLI) access to the login node scales very well and consumes very little RAM. If and when someone runs an intensive computational job (a compute job), a schedular is able to properly distribute the computational load onto any of the available CPU nodes, or if no nodes are free, the scheduler can appropriate queue the job.

* 3. Automation! This is my favorite reason. Dockerfiles are basically glorified Bourne Again Shell (BASH) scripts. The CLI greatly enables what is referred to as powerusers, a poweruser is someone who has learned to efficiently address reoccuring problems using a script of bash commands. BTW, Dockerised containers empower the web, and they make up the brunt of large scale websites now. Amazon Web Services (AWS), are deeply founded on Dockercontainers.

### Why virtual environments?
Virtual environments allow you to setup multiple code projects with complicated dependencies, in a way that each projects dependencies is contained to the scope of the virtual environment. The benefit of this cheap containerisation is it stops the creation of circular dependencies.

### Anatomy of the Linux prompt:

Linux commands can seem duanting to the uninitiated so, lets find a long command and break it down into explainable parts.

In the long linux command below, everything to the left of `$` is the path and everything to the left of `@` is contextual.

```
(python3_venv) rjjarvis@ncl-edu:~/nxsdk-apps-20220419-142407/n2_apps/tutorials/nxnet$ SLURM=1 python tutorial_18b_learning.py
```


Ie the first braces () indicate that we are inside a virtual environment called `python3_venv`, `rjjarvis` is the users user name, in this case it is my username.

the `~` symbol means the home directory. Tip: you can return to home directory from anywhere with the simple command `cd ~`

`SLURM=1` is an a command specific to the Intel superhost that means give the user an interactively allocated CPU to play with here and now. The impact of running


### Why SLURM?

Slurm is a scalable cluster management and job scheduling system for Linux clusters. As a cluster workload manager, SLURM allocates compute nodes)to users for some duration of time so they can perform work. Second, it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes. SLURM arbitrates contention for resources by managing a queue of pending work.

`python tutorial_18b_learning.py`, versus `SLURM=1 python tutorial_18b_learning.py` wont be felt by us. We use `SLURM=1` to preface out compute job as a courtesy to other users on the login node. If every uses SLURM=1 as etiquette the linux experience will be a bit less clunky for everyone. 

Running quick jobs occasionally without SLURM will not be noticed, but if a person where to not use SLURM at all, the system admins would probabaly notice and act on this.

CLI help with re-typing long commands. If you type the command `$history`, the whole terminal screen will fill up with the most recent commands typed.

### Exercises:


#### How to edit files on Headless Linux:

In order to edit files on headless Linux, you can use any of the three editors: nano, vim, emacs. Nano is often the begginers preferred choice as it has no learning curve, and there is always a cheat sheet down the bottom, VIM is often preffered by knowledgable linux users and power-users.

Once you have sshd into the Intel cloud superhost you should edit your `~/.bash_profile` file. If there is no `~/.bash_profile` file in your home directory, please create one with `touch ~/.bashrc`, you can then edit this empty file with `nano ~/.bash_profile`. In your `~/.bash_profile` file, add this line: `source /nfs/ncl/.bashrc`, as the 1st line, what this does is, it inherits an initialization script from an Intel template stored in the server root directory `/`, is the root directory. 

Source your `~/.bash_profile` file to load the changes with this command: source `~/.bash_profile`. Now test to see that you did it correctly. Here's some typical output when running `sinfo command:username@THE_NRC_VM ~ % sinfo`.


Create and populate a file `~/.bash_profile` 1/15 marks.

(1 mark) Create a functional lava virtual environment, and an alias for activating the virtual environment for in ~/.bash_profile called actlav (activate lava). Take a screenshot of the ~/.bash_profile. 

Type `source ~/.bash_profile` every time you change this file and you want the changes to take effect. Note logging in and out of ssh is also sufficient to "source" the file.

File `~/.bash_profile` contents:
```
source /nfs/ncl/.bashrc
# This is a BASH commment
# If you called your virtual environment lava_venv
# The alias below will activate the environment. 
alias activ='source ~/lava_venv/bin/activate' 
# to deactivate type the commmand`: deactivate
# create an alias, that automatically takes you to a long and hard to remember path:
alias tuts='cd /homes/rjjarvis/nxsdk-apps-20220419-142407/n2_apps/tutorials/nxnet'
```


```
source /nfs/ncl/.bashrc
```

### Upgrade pip
As soon you ssh into your Linux environment you will need to upgrade pip

```pip install --upgrade pip```


At some point it might be useful to know that your Intel Loihi organization is as follows: `export YOURORG="edu"`, THE_NRC_VM: ncl-edu


For example: `sinfo command:jdnuerf@ncl-edu ~ % sinfo`
... or: `sinfo command:drice@ncl-edu ~ % sinfo`


### Background:

#### At least **Five** major ways to program Loihi:
#### **Lava**, and older methods: NXSDK, NXNET, SNIPS (C code), Nengo-Loihi.
In-fact one of the motivations for Lava's existence is because methods for programming Loihi where becoming too fragmented, Lava is a glue language like Python. 

#### Importantly, Lava itself has several components: Lava-DL, Lava-DNF and Lava optimisation.

If there is time next Tuesday we will look at Lava-DNF and Lava Optimisation.

### Loihi Architecture Overview. 
Intel's Loihi research chip is an asynchronous, compute-in-memory neuromorphic processor optimized for the execution of Spiking Neural Networks. Loihi 1 consists of 128 neurocores, each of which supports up to `1024` neurons. Loihi is a fully digital architecture (some neuromorphic architectures are not).

A recurrent neural network is a directed graph, it is also a function of Vertices (neurons) and Edges (synapses):

 $ G(V, E) $

<!---![diagram_loihi_spike_trip.jpeg](diagram_loihi_spike_trip.jpeg)--->

## About Loihi Architecture.

Loihi 1 impliments a variant of the current-based synapse (CUBA) and leaky integrate and fire neuron model with two internal state variables:
* Synaptic  Current $ u_{i}(t) $ - the weighted sum of the input spikes and a constant bias. When you plot this, this is basically telling you how much or how many excitatory synaptic events the neuron is receiving.
* Membrane potential $v_{t}(t)$  a leaky (ie weakens over time) membrane voltage function, which sends a spike when the potential passes the firing threshold.


# Loihi supports graded spike amplitudes, and that makes certain things possible.

If you are programming in a manner where you record spike times, but not raw neuron voltages you may not notice that the simulated membrane potential of a current based Loihi neuron is unitless, and swings between: [−100,000,100,000]**. Remember that [-90,-50] $mV$ is a normal range of neuron membrane potential in biologically grounded models like the standard LIF model. On Loihi this range has been re-normalised to be $ [-2^{23}, 2^{23}-1].

  * Unusual property of $v_{t}(t)$ it has highly non-biological plausible values $ [-100,000, 100,000] mV$ is normal.

![Loihi_CUBA_model_param.png](loihi_fig/Loihi_CUBA_model_param.png)




### Exercises

When complete, deactivate the virtual environment with the simple command 
`deactivate`
   
Remember to activate virtual environments every time you `ssh` back in and do development work with lava, unless you have configured your `~/.bash_profile`, to do this for you. 


### Launch Python from the command line:
simply typing `python` with no arguments will launch Python.
To apply Python to a script file type:
`python script_file_name.py`

### Except we are on the Intel superhost, so remember to do:
`SLURM=1 python script_file_name.py`

### Gotcha: No Longer in the virtual environment.
Overnight, you might choose to sleep instead of code. In sleep you will time out from ssh, when you log back in again, you fail to notice that you are no longer in the Python virtual enviroment.

Often when starting a new day of code you will find you are logged out of the Intel superhost (you can't stay signed-in in the absence of activity, eventually your idle login will yield a: `pipe-broken` error).
When your last ssh session has ended, its common to forget that you may need to re-activate your virtual environment.

In fact, if you want to save yourself time and effort you might automatically activate the virtual environment using your: `bash_profile` script. Hint, you can borrow other peoples code and scripts
```
pwd
cd ../
cd jdnuerf/
cd ../drice/
ls -ltr
```
![](loihi_fig/spy_on_neighbours_code.png)

You may already know that pressing the up and down cursor buttons will enable you to cycle through your bash history. If you typped a very long command, many commands ago, it is prefferable to type history, so you can read up to where it was when you typed the command.

Optionally to repeat a line of your CLI history, you can type `![the numeric value of a history line number]`. For example `!121` will issue the command from line 121 of your history. An even more powerful option is to hold the short cut `CTRL-R`. This will do a recursive search of your command line history.

```
history
   11  ls -ltr
```
The quickest practical solution is to type: `history`
and fish out the command where you activate the virtual environment.
One caveat make sure that you are in the $HOME directory when you do this.
```
  513  source python3_venv/bin/activate
```

```
alias intel="ssh rjjarvis@ncl-edu.research.intel-research.net"
PROMPT_COMMAND='history -a'
```

Exercises:
Execute the following BASH code and explain what it does in a few sentences (1 mark):
```
cd ~;
mkdir lava
cd lava
python3 -m venv lava_nx_env
source lava_nx_env/bin/activate
pip install --upgrade pip # already done above.
cp /nfs/ncl/lava/releases/v0.4.0/lava-nc-loihi-0.4.0.tar.gz ./.
pip install lava-nc-loihi-0.4.0.tar.gz
```
### Exercises Continued...
#### In BASH:
the `echo` command is analogous to `print` in Python, except it echo requires no braces for its arguments to print. `>>` means redirect. Redirection means instead of printing something to the screen, print the stdout to a file instead.

#### Exercises:
Continued from above execute the following BASH code and explain what it does in a few sentences (same 1 as above mark):
```
echo export SLURM=1  >> ~/.bashrc
echo export C_INCLUDE_PATH=\$C_INCLUDE_PATH:$(python3 -c "import nxcore; print(nxcore.__path__[0])")/include >> ~/.bashrc
echo export C_INCLUDE_PATH=\$C_INCLUDE_PATH:$(pwd)/lava-nc-loihi-0.4.0/tutorials/end_to_end >> ~/.bashrc
```


#### Be Careful With the Following: 
* **Don't** execute the following, but for one mark explain what it does.


```
​echo export BOARD=ncl-ext-og-04  >> ~/.bashrc
echo export PARTITION=oheogulch  >> ~/.bashrc
```

```
cd lava-nc-loihi-0.4.0):
SLURM=1 LOIHI_GEN=N3B3 PARTITION=oheogulch RUN_LOIHI_TESTS=1 RUN_IT_TESTS=1 python -m unittest -v tests/lava/integration/<test_python_script>.py
```
```
(lava_nx_env) rjjarvis@ncl-edu:~$ SLURM=1 BOARD=ncl-ext-og-04 PARTITION=oheogulch python lava_test.py
```

Finally for 2 marks open VIM or Nano, instance those respective programs with a file name such as test lava: `vim lava_test.py`
`nano lava_test.py`

paste the following contents into the file:

```
    # Instantiate Lava processes to build network
    from lava.proc.dense.process import Dense
    from lava.proc.lif.process import LIF
    import numpy as np

    # declare a layer of Leaky Integrate and Fire Neurons of size 1.
    lif1 = LIF(shape=(1, ))
    # declare a layer of random valued weights of size 1.
    dense = Dense(weights=np.random.rand(1, 1))
    # declare a layer of Leaky Integrate and Fire Neurons of size 1.
    lif2 = LIF(shape=(1, ))

    # Connect processes via their directional input and output ports
    lif1.out_ports.s_out.connect(dense.in_ports.s_in)
    dense.out_ports.a_out.connect(lif2.in_ports.a_in)

    # Execute process lif1 and all processes connected to it for fixed number of steps
    from lava.magma.core.run_conditions import RunSteps
    from lava.magma.core.run_configs import Loihi2HwCfg

    lif1.run(condition=RunSteps(num_steps=10), run_cfg=Loihi2HwCfg())
    lif1.stop()
```

Now apply Python to this script with:
`SLURM=1 python lava_test.py`


For the rest of the marks do the following:

We want to profile the run time of the whole script. 

Paste the following code statements at select locations in the code

```
import cProfile
def main():
        """
        wrap the whole code chunk in the function definition main.
        """
        return None
if __name__ == '__main__':
    cProfile.run('main()')
```


Now make a copy of the file:
`cp lava_test.py bigger_lava_test.py`



Now we want to make the network bigger, and we want to explore how making the network bigger slows down CPU performance.

Figure out which three lines of code you would need to change to increase the number of neurons per layer by an order of 1000 then run the profiled code.
`SLURM=1 python bigger_lava_test.py`

Finally copy this new profiled code into a file: simulated_lava_test
`cp bigger_lava_test.py simulated_lava_test.py`

Place the line:
```
from lava.magma.core.run_configs import Loihi1SimCfg
sim_run_cfg = Loihi1SimCfg()
```
before the line 
```
lif1.run(condition=RunSteps(num_steps=10), run_cfg=Loihi2HwCfg())
```
Now edit the above line so that it the Loihi hardware executor uses a simulated backend instead of the real Loihi hardware.

create a bash alias to run your file: 
```~/.bash_profile```

```alias runl='SLURM=1 BOARD=ncl-ext-og-04 PARTITION=oheogulch python simulated_lava_test.py'```

You can also pipe the result to `less` using:

```SLURM=1 BOARD=ncl-ext-og-04 PARTITION=oheogulch python simulated_lava_test.py | less```
. Note that BASH's pipe operator is the true meaning and origin of pipelines in data science.

exit your ssh session by typing exit. Log back in again and confirm that the alias works.

### Submit as part of the final written report In the lab report answer the following questions, due in 2 weeks.

When running the simulated Loihi, is a the network faster or slower for a simulated network of 1023 layer 1 by 1023 neurons layer 2 (all to all connectivity), versus 1 by 1 neuron (all to all connectivity). Was the speed difference as significant as you would have thought? 

Using the `Loihi2HwCfg()` hardware executor compare the same job run on both machines, using network sizes 1by1, and 10 by 10 in hardware. Compare the speeds of these two sizes of network simulation on hardware.

Is using the hardware faster or slower than the simulator? In your answer include a discussion about software to hardware communication. Also note that the type of job we gave the hardware did not involve causing the network to spike, or communication of spikes between neurocores on Loihi. Given that there was no production of or communication of spikes, what extra steps might we include to make the hardware simulation faster than the software simulation? 
## Preview:

### Next week we will look at installing Lava from source code.
We will look at running less trivial examples, this may include installing lava from source code on your local machine, or the Intel Superhost as appropriate. 

First create a virtual environment.

```
cd ~ 
python3 -m venv lava_from_src
source lava_from_src/bin/activate
git tag -n # to list the second latest tag 0.3.0
git checkout # enter tag number from above.
```
Then git checkout the release corresponding to tag 0.3.0 using the command git checkout


git clone will not work there but git generally works. We can scp the github version of lava onto the Loihi superhost.


#### Next Week will Look into using scp or rsync too:

Note `scp` is like `cp` and `ssh` combined into the same statement.

```
scp run_lava_dl.py ncl-edu.research.intel-research.net:~
```

Note `~` is home in any bash environment.
```
scp -r local_folder_name ncl-edu.research.intel-research.net:~/
```
