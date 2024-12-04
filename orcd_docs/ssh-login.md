You can log into our systems via SSH through your local terminal. Using SSH in a terminal or command line window on your desktop is the traditional way to access HPC Systems. This method offers the most flexibility, allowing you to start interactive and batch jobs to run your code, download data, and install packages.

A terminal window is a window with a command line interface. 

To log into our systems, we use the terminal to SSH into the system. SSH (Secure Shell) is the primary way to log into remote systems. Once you initiate the SSH command, the shell in your terminal will no longer run on your computer but on the remote system. Authentication is required, either using a password or SSH keys. To set up SSH keys, please refer to the SSH Key Setup Page.

Follow the directions below based on your operating system:

Open Terminal by searching for it in Spotlight or by navigating to Applications > Utilities > Terminal.

Open Terminal from your Applications menu.

Windows systems offer multiple terminal options: Windows Terminal, Command Prompt, and PowerShell. The best way to get a terminal depends on your version of Windows. Starting at Windows 10, the Windows Subsystem for Linux (WSL) is available, allowing you to run Linux as an application in Windows. You can also use the Windows Command Prompt if you have SSH enabled. For older versions of Windows, install a terminal program that supports bash.

You have two options:  

To check if CMD has SSH enabled, run the command ssh. If SSH is not enabled, follow the instructions on this Page to set it up.

If you want to use WSL, follow the instructions on this Page to enable WSL and install a Linux distribution of your choice. If you don't have a preference, Ubuntu is a good place to start. If you have any questions about WSL, there is a good chance they are answered in their FAQ.

For older Windows versions, install a terminal that supports bash and SSH, such as MobaXterm. Follow the instructions on this Page to install MobaXterm and create a local shell.

Some programs may seem like valid terminals for accessing SuperCloud but are not ideal. Here are a few examples and why they are not recommended:

Once you have your terminal set up for your specific operating system, you can use SSH to access our HPC systems. Follow the commands below for your desired system.

The Engaging Cluster has 3 login nodes: 

To login via the command line, run the SSH command:
ssh [username]@[host]

Replace [username] with your MIT Kerberos username and [host] with the desired login node name (e.g., ssh your_name@eofe9.mit.edu).

Connecting to eofe9 or eofe10 requires Two-Factor Authentication.

Note

You will be prompted to enter your MIT Kerberos password if you have not set up SSH keys. To set them up, please refer to our SSH Key Setup Page.

Satori has 2 login nodes:  

To login via the command line, run the SSH command:
ssh [username]@[host]

Replace [username] with your MIT Kerberos username and [host] with the desired login node name (e.g., ssh your_name@satori-login-001.mit.edu).

Note

You will be prompted to enter your MIT Kerberos password if you have not set up SSH keys. To set them up, please refer to our SSH Key Setup Page.

Accessing the SuperCloud system through SSH requires that your public ssh-key has been added to the authorized_keys file in your SuperCloud account. Follow the instructions on this page to create your keys and add them to your account.

If you have any issues connecting to the system, please send an email to supercloud@mit.edu.

To connect to SuperCloud once your SSH keys are setup, follow these steps:  

To login to OpenMind, you must first be connected to the MIT Wi-Fi or MIT VPN. For further instructions, refer to this page.

To login to OpenMind via the command line, run the SSH command:
ssh [username]@openmind.mit.edu

Replace [username] with your MIT Kerberos username. 

Note

You will be prompted to enter your MIT Kerberos password if you have not set up SSH keys. To set them up, please refer to our SSH Key Setup Page.

