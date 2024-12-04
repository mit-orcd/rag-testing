VSCode is a convenient IDE for development, and one of its nicest features is its ability to run on a remote system using its RemoteSSH extension. This means you can have the VSCode window on your computer, while the files and anything you run will be on the remote system you are connected to.

Once you've installed the RemoteSSH extension this is fairly easy to set up. However, it is also very easy to set up in such a way that it is not only slow for you, but it also puts excess load on the login nodes and in turn slows things down for others on that node. Luckily, with a few extra steps you can run VSCode on a compute node where it can have more resources to run and won't impact others as much.

Click the "Open a Remote Window" button in the bottom left corner of your VSCode window (It is a small blue rectangle labeled with ><). In the bar at the top of the page select "Connect to Host...", then "Configure SSH Hosts", and select first option, which will differ depending on your operating system. This will open your config file in a VSCode tab.

To run on a compute node you will need at least 2 entries in this file. The first will be a login node that you'll "jump" through and the second will be the compute node that is your final destination.

Note

If you are using one of the login nodes that requires 2-Factor authentication be ready to receive your default 2-Factor prompt when you connect. If you do not respond right away the connection will time out.

Note

To use VSCode on a compute node, an SSH key is necessary. If you haven't set up SSH keys yet, refer to this Engaging guide.

Note

To use VSCode on a compute node, an SSH key is necessary. While Satori documentation is unavailable, you can follow the same steps as outlined on Engaging.

Note

To use VSCode on a compute node, an SSH key is necessary. If you haven't set up SSH keys yet, refer to this Open Mind guide.

Replace USERNAME with your username on the system you are connecting to. We will fill in "nodename" later.

Each time you sit down to do remote work through VSCode you will have three steps:

We go through these steps in detail below.

Open a terminal window and ssh into the login node. If you are not used to doing this you can open a terminal in VSCode and run:

Use the name you have used for the login Host in your config file if different than the one above. The example screenshot below shows logging into one of the Engaging login nodes with ssh in a VSCode terminal window.



Once you are logged in start an interactive session. If you are planning to only edit files a single core may be sufficient, but if you plan to run code or Jupyter Notebooks you may want to allocate more resources accordingly. Refer to the documentation for your system on how to request an interactive job:

Engaging's Documentation for Running Jobs

Satori's Documentation for Running Jobs

SuperCloud's Documentation for Running Jobs

OpenMind's Documentation for Running Jobs

Once your job has started you can run the hostname command to get the name of the node your interactive job is running on. You can also run the squeue --me command to list all your running jobs and get the hostname from the last column.

The screenshot below shows requesting a single interactive core for 1 hour on Engaging:



Note that the scheduler will also tell you which node you are allocated in its output. In this screenshot my node name is node020.

Update the HostName of your compute node entry in your config file. If your config file is not open, follow the instructions above to open it again. Then replace whatever you have for HostName in your config file with the output of the hostname command you ran in your interactive session, or got from squeue --me.

If your compute node is node1234 then your config file should look something like:

Where USERNAME is replaced by your username.

This screenshot shows updating the config file for an interactive job running on Engaging:



Since the interactive job in my screenshot is running on node020, I have updated HostName to node-020 for the eofe-compute entry in my config file.

You are ready to connect to the compute node you have allocated through your interactive job from VSCode. Select the "Open a Remote Window" button in the bottom left corner of your VSCode window. In the bar at the top of the page select "Connect to Host..." and select the Host for the compute node that you have created.

In the example config file above this would be eofe-compute.

In the example config file above this would be satori-compute.

In the example config file above this would be om-compute.

Here is what this might look like for Engaging:



