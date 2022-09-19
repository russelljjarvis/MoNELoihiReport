
<h1 align="center">
      Guide for the Tutorial 
      Headless Linux for Hardware.
      and Navigating the Intel Loihi Superhost 
</h1>

<h3 align="center">
    Russell Jarvis post-doctoral researcher at ICNS.
    r.jarvis@westernsydney.edu.au
</h3>

### Take Home Assessment
Weight: $ 30% $
Type of Collaboration: Individual
Submission: Weeks 9 by Friday 11:59pm (midnight) Turnit in, and optionally an additional Overleaf link.
Format: The report will consist of 1000-1200 words and several figures. The purpose of this report is to demonstrate the completion of assigned preworks and labworks in programming Loihi. References, quotes, and appendices are not part of the word count.
Length: $1200$ words


# For the first of two tutorials we will:
* Secure Shell (ssh). Note to "ssh" is meant as a verb in this context. We will ssh into the Intel superhost and navigate the Linux environment.
* Use secure copy (scp) and pip to install lava version tag 0.3.0 (the penultimate version).
* Hopefully run a trivial lava programm using SLURM=1.


# Why Headless Linux?
On High Performance Computers, Docker-containers, and resource restricted hardware environments: Raspberri-PI, NVIDIA Jetson Nano etc. A "head-less" Linux login is default interface for accessing the resource. There are multiple reasons for this:

* 1. A graphical Operating System (OS) acts as a large memory and CPU and load. On a raspberri-pi you will likely prefer to keep all the RAM and CPU for developing applications. Trying to use the graphical OS will likely be unresponsive and clunky anyway, as it is on the Nvidia Jetson Nano. 

* 2. On a super-computer, such as the Intel Superhost, login nodes are shared between groups of 10 or more users. Command Line Interface (CLI) access to the login node scales very well and consumes very little RAM. If and when someone runs an intensive computational job (a compute job), a schedular is able to properly distribute the computational load onto any of the available CPU nodes, or if no nodes are free, the scheduler can appropriate queue the job.

* 3. Automation! This is my favorite reason. Dockerfiles are basically glorified Bourne Again Shell (BASH) scripts. The CLI greatly enables what is referred to as powerusers, a poweruser is someone who has learned to efficiently address reoccuring problems using a script of bash commands. BTW, Dockerised containers empower the web, and they make up the brunt of large scale websites now. Amazon Web Services (AWS), are deeply founded on Dockercontainers.

# Why virtual environments?
Virtual environments allow you to setup multiple code projects with complicated dependencies, in a way that each projects dependencies is contained to the scope of the virtual environment. The benefit of this cheap containerisation is it stops the creation of circular dependencies.


# Anatomy of the Linux prompt:

Linux commands can seem duanting to the uninitiated so, lets find a long command and break it down into explainable parts.

In the long linux command below, everything to the left of `$` is the path and everything to the left of `@` is contextual.

```
(python3_venv) rjjarvis@ncl-edu:~/nxsdk-apps-20220419-142407/n2_apps/tutorials/nxnet$ SLURM=1 python tutorial_18b_learning.py
```


Ie the first braces () indicate that we are inside a virtual environment called `python3_venv`, `rjjarvis` is the users user name, in this case it is my username.

the `~` symbol means the home directory. Tip: you can return to home directory from anywhere with the simple command `cd ~`

`SLURM=1` is an a command specific to the Intel superhost that means give the user an interactively allocated CPU to play with here and now. The impact of running


# Why SLURM?

Slurm is a scalable cluster management and job scheduling system for Linux clusters. As a cluster workload manager, SLURM allocates compute nodes)to users for some duration of time so they can perform work. Second, it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes. SLURM arbitrates contention for resources by managing a queue of pending work.

`python tutorial_18b_learning.py`, versus `SLURM=1 python tutorial_18b_learning.py` wont be felt by us. We use `SLURM=1` to preface out compute job as a courtesy to other users on the login node. If every uses SLURM=1 as etiquette the linux experience will be a bit less clunky for everyone. 

Running quick jobs occasionally without SLURM will not be noticed, but if a person where to not use SLURM at all, the system admins would probabaly notice and act on this.

CLI help with re-typing long commands. If you type the command `$history`, the whole terminal screen will fill up with the most recent commands typed.


```
source /nfs/ncl/.bashrc
```



# At least **Five** major ways to program Loihi:
**NXSDK, NXNET, SNIPS (C code), Nengo-Loihi and Lava**.

Lava itself has several components: Lava-DL, Lava-DNF and Lava optimisation.

* **Nengo-Loihi**

### Loihi Architecture Overview. 
Intel's Loihi research chip is an asynchronous, compute-in-memory neuromorphic processor optimized for the execution of Spiking Neural Networks. Loihi consists of 128 neurocores, each of which supports up to 1024 neurons

* Loihi is a fully digital architecture (some neuromorphic architectures are not).

A recurrent neural network is a directed graph, it is also a function of Vertices (neurons) and Edges (synapses):

 $ G(V, E) $

<!---![diagram_loihi_spike_trip.jpeg](diagram_loihi_spike_trip.jpeg)--->

# Loihi supports graded spike amplitudes, and that makes certain things possible.

Deep learning networks are feedforward (although errors are backprogated), this is a different feedback signal.

![diagram_loihi_spike_trip.jpeg](for_tutorial.png)


**Note unitless. [−100,000,100,000]**

[-90,-50] $mV$ is a normal, range of neuron membrane potential in biologically grounded models like the standard LIF model. On Loihi this range has been re-normalised to be $ [-2^{23}, 2^{23}-1]  $


```
scp run_lava_dl.py ncl-edu.research.intel-research.net:~
```

Note ~ is home on the remote.
```
scp -r local_folder_name ncl-edu.research.intel-research.net:~/
```

Syncing with rsync¶
If you work on your local machine and push changes to multiple remote superhosts, it is worth spending some time to set up a robust solution for syncing files between your local machine and the superhosts.
The basic command that is most useful is
```
rsync -rtuv --exclude=*.pyc ncl-edu.research.intel-research.net ~/
```
-r recurses into subdirectories

-t copies and updates file modifications times

-u replaces files with the most up-to-date version as determined by modification time

-v adds more console output to see what has changed


# Only Neuron-Local Information
As discussed in "Simultaneous unsupervised and supervised learning of cognitive functions in biologically plausible spiking neural networks" by Bekolay et al., the effect of the PES learning rule on the decoders $ Δdi   $ is formulated as:

$ \Delta di=\Kappa Eai $

$E$ is the error vector is mapped onto individual neurons which also represent vectors of the same dimension. Biologically, the error vector is theorized to be dopamine levels.
ai is each neuron activity level, which in the NEF is defined as a combination of the neuron's encoder and it's activation function. See Principle 1 of the NEF for more detail.
κ is the error scaling factor




In fact the reason for the existence of Lava is to address fragmentation in the field.
<!---![loihi_nxnet_compiler.png](loihi_nxnet_compiler.png) --> 
I am just going to focus on Nengo, since its the only package that is stable and functional on the Loihi education server atm.


Loihi implaments a variant of the current-based synapse (CUBA) and leaky integrate and fire neuron model with two internal state variables:
* Synaptic  Current $ u_{i}(t) $ - the weighted sum of the input spikes and a constant bias. When you plot this, this is basically telling you how much or how many excitatory synaptic events the neuron is receiving.
* Membrane potential $v_{t}(t)$  a leaky (ie weakens over time) membrane voltage function, which sends a spike when the potential passes the firing threshold.
  * Unusual property of $v_{t}(t)$ it has highly non-biological plausible values $ [-100,000, 100,000] mV$ is normal.





Below is a diagram of the Potjan's cortical model. This model can be thought of as the composition of many weighted directed graphs, therefore we will use Lava a supported interface to begin to build a cortical model with the Python Loihi simulator.

### Insert a picture of a directed network graph from Loihi lecture Mark found.

### Setting up SSH Public Key Auth and SSH Proxies for the Neuromorphic Research Cloud Welcome to the Neuromorphic Research Cloud.

Setting up `SSH` Public Key Auth and `SSH` Proxies Please set up SSH jump host support and/or ssh public key auth. It is assumed that you are on a machine you control (you have some administrative privlige). Make two ssh keys, change the paths to match yours. Empty passphrases are fine. 

### Using OSX Terminal, Ubuntu Terminal, GitBash (for Windows) or Windows sub-system for Linux (WSL).

At your command prompt enter:
`username@yourowncomputer$ssh-keygen`   

Generating public/private rsa key pair. Enter file in which to save the key `(/home/username/.ssh/id_rsa)`: `/home/username/.ssh/vlab_gateway_rsa`   

Enter passphrase (empty for no passphrase): 
Enter same passphrase again: Your identification has been saved in `/home/username/.ssh/vlab_gateway_rsa`. 

Your public key has been saved in `/home/username/.ssh/vlab_gateway_rsa.pub`.   
The key fingerprint is: REDACTED The key's randomart image is:  REDACTED 
`username@yourowncomputer$ssh-keygen`  Generating public/private rsa key pair. Enter file in which to save the key (`/home/username/.ssh/id_rsa`): `/home/username/.ssh/vlab_ext_rsa` Enter passphrase (empty for no passphrase): Enter same passphrase again: Your identification has been saved in `/home/username/.ssh/vlab_ext_rsa`. Your public key has been saved in `/home/username/.ssh/vlab_ext_rsa.pub`.   The key fingerprint is: REDACTED The key's randomart image is: REDACTED Then you'll want to make your `~/.ssh/config` follow the pattern below.  


If on Windows, you can do all of this using Powershell and Notepad (which is POSIX compliant).

```
Host ssh.intel-research.netUser=username 
IdentityFile /home/username/.ssh/vlab_gateway_rsa 
Host *.research.intel-research.netHostName %h User=username
ProxyCommand= ssh -W %h:%p ssh.intel-research
netIdentityFile /home/username/.ssh/vlab_ext_rsa
``` 

Install lava from source using 

git tag -n to get the second latest tag 0.3.0

Then git checkout the release corresponding to tag 0.3.0 using the command git checkout


git clone will not work there but git generally works


For users connecting from Windows and using PowerShell or OpenSSH, the "`ProxyCommand ssh`" line needs a full path to the ssh command:   
`ProxyCommand= C:\Windows\System32\OpenSSH\ssh.exe -W %h:%p ssh.intel-research.net`

Next, send your public keys to `nrc_support@intel-research`.netand we will add them for you. Once Intel have notified that they have your keys,

export YOURORG="edu"

You should be able to ssh directly into: 
`ncl-edu.research.intel-research.net`

If you can't you can debug your config file with `-vv`.

```bash
ssh -vv ncl-edu.research.intel-research.net
```

Once you have sshd into the Intel cloud environment you can set the environment variables by editing your `~/.bashrc` file. If there is no .bashrc file in your home directory, please create one. In your `~/.bashrc` file, add this line: source `/nfs/ncl/.bashrc`

Note, there are variants of the shells available, here we use `.bashrc` as an example.    

## Important
Source your `~/.bashrc` file to load the changes with this command: source `~/.bashrc`. Now test to see that you did it correctly. Here's some typical output when running `sinfo command:username@THE_NRC_VM ~ % sinfo` 

For example: ``sinfo command:rjjarvis@ncl-edu ~ % sinfo`


### Next Confiigure your Loihi Cloud Experience

# Gotcha downgrade numpy

# Gotcha, upgrade pip


`cd ~ 
b.python3 -m venv python3_venv 
c.source python3_venv/bin/activate` 

4. Complete all following steps within the virtual environment 5.Copy Release artifacts: a.
5. `cp /nfs/ncl/releases/<latest_version>/* .`
6. .i. Note the “dot” at the end oft his command is necessary 7. Install NxSDK:
   a. `python -m pip install nxsdk-<latest_version>.tar.gz.` 
   
   Ignore the “Failedbuilding wheel for nxsdk” and the associated “Failed to build nxsdk.” This is a known error and pip will retry with setup.py.7.Unzip Tutorials, Docs, and Modules in your home directory:
   a. `mkdir nxsdk-apps && tar xzf nxsdk-apps-<latest_version>.tar.gz -C nxsdk-apps –stripcomponents 1`
   8. Refer to the 0.7 release notes for additional details, e.g. running tutorials
   a. `cd nxsdc-apps/docs`
   b.Refer to README.html scp README.html back to your machine.
   
   9. When complete, deactivate the virtual environ
   10. Remember to activate virtual environments every time you ssh back in and do development work with NXSDK.



# Gotcha's
The second latest version of nxsdk-2.0.0 needs a numpy downgrade.
Finally we need to do   
```pip install --upgrade numpy==1.20.1```
because most of the actual applications in apps, assume an older version of numpy that has a method `ascalar`, if we use a newer version of numpy, our applications will throw an `as_scalar` error.



you time out from ssh, when you log back in again, you fail to notice that you are no longer in the Python virtual enviroment.
```
rjjarvis@ncl-edu:~/nxsdk-apps-20220419-142407/n2_apps/tutorials/nxnet$ SLURM=1 python tutorial_23_noisy_winner_takes_all.py
  File "tutorial_23_noisy_winner_takes_all.py", line 4
SyntaxError: Non-ASCII character '\xc2' in file tutorial_23_noisy_winner_takes_all.py on line 4, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
rjjarvis@ncl-edu:~/nxsdk-apps-20220419-142407/n2_apps/tutorials/nxnet$ history
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

source /nfs/ncl/.bashrc
```
alias activ='cd ~; source python3_venv/bin/activate; cd ../'
alias tuts='cd /homes/rjjarvis/nxsdk-apps-20220419-142407/n2_apps/tutorials/nxnet'
```

Investigating the contribution of Scale to Loihi Speed


2.4.2 Practical

 


 