This page contains the most common steps for setting up and getting
started with your ORCD system account. We provide this page as a
convenient reference to get started. Each system has its own in-depth documentation which can be found on the ORCD Systems page.

Sections that are system-specific will be shown under a list of tabs. Click on the tab for the system you are using and the rest of the page will show the information for that system.

If you don't already have an account, click on the tab for the system you are interested in and follow the instructions.

Login into the respective OnDemand Portal https://engaging-ood.mit.edu using your MIT kerberos credentials. The system will then be prompted to create your account automatically. Wait couple minutes for the system to create all the pieces for your account before submitting your first job.

Login into the respective OnDemand Portal https://satori-portal.mit.edu/ using your MIT kerberos credentials. The system will then be prompted to create your account automatically. Wait couple minutes for the system to create all the pieces for your account before submitting your first job.

Follow the instructions on the Account Request Page.

OpenMind will be available to the general MIT Community starting 2024. Those currently eligible can follow the instructions on the Getting an Account page.

The first thing you should do when you get a new account is verify that
you can log in. The different ORCD systems provide multiple ways to log in, including both ssh and web portals. Links to instructions for the different systems are below.

See the Logging into Engaging page for full documentation.

See the Logging into Satori page for full documentation.

See the Logging into SuperCloud page for full documentation.

See the Logging into OpenMind page for full documentation.

Engaging has four login nodes: eofe7, eofe8, eofe9, and eofe10. Replace USERNAME below with your Kerberos username and use the login node you would like to log in with, the example below is using eofe10.

If you are prompted for a password enter your Kerberos password.  You can add an ssh key if you do not want to enter your Kerberos password at login. eofe9 and eofe10 also require Two-Factor Authentication.

Satori has two login nodes: satori-login-001 and satori-login-002. Replace USERNAME below with your Kerberos username and use the login node you would like to log in with, the example below is using satori-login-001.

If you are prompted for a password enter your Kerberos password. You can add an ssh key if you do not want to enter your Kerberos password at login.

In order to log into SuperCloud with ssh you will need to add ssh keys to your account on the Web Portal. Follow the instructions on the SuperCloud Getting Started page to add your keys.

Then you can log in with ssh using the following command, where USERNAME is your username on the MIT SuperCloud system:

Log into OpenMind with the following command in a terminal window. Replace USERNAME below with your Kerberos username.

If you are prompted for a password enter your Kerberos password. You can add an ssh key if you do not want to enter your Kerberos password at login.

You can log into OnDemand Web Portal with the link: https://engaging-ood.mit.edu. For full detailed instructions please see the Engaging Documentation.

You can log into the OnDemand Web Portal with the link: https://satori-portal.mit.edu. For full detailed instructions please see the Satori Documentation.

You can log into the SuperCloud Web Portal with the link: https://txe1-portal.mit.edu. For full detailed instructions please see the SuperCloud Documentation.

OpenMind does not currently have a web portal, but there are plans to add one in the future. Check back, and in the meantime check out OpenMind's documentation on the FastX Remote Desktop. You may find it provides what you are looking for.

Each ORCD system is a shared HPC cluster. You are sharing this
resources with a number of other researchers, staff, and students so it
is important that you read this page and use the system as intended.

Being a cluster, there are several machines connected together with a
network. We refer to these as nodes. Most nodes in the cluster are
referred to as compute nodes, this is where the computation is done
on the system (where you will run your code). When you ssh into the
system you are on a special purpose node called the login node. The
login node, as its name suggests, is where you log in and is for editing
code and files, installing packages and software, downloading data, and
starting jobs to run your code on one of the compute nodes.

Each job is started using a piece of software called the scheduler,
which you can think of as a resource manager. You let it know what
resources you need and what you want to run, and the scheduler will find
those resources and start your job on them. When your job completes
those resources are relinquished. The scheduler is what ensures that no
two jobs are using the same resources, so it is very important not to
run anything unless it is submitted properly through the scheduler.

The first thing you may want to do is make sure the system has the
software and packages you need. We have installed a lot of software and
packages on the system already, even though it may not be immediately
obvious that it is there. Review the page for the system you are using paying particular attention to the section on modules and installing packages for the language that you use:

Engaging Software Documentation Page

Satori Software Documentation Page

SuperCloud Software Documentation Page

OpenMind Software Documentation Page

If you are ever unsure if we have a particular
software, and you cannot find it, please send us an email and ask before
you spend a lot of time trying to install it. If we have it, we can
point you to it, provide advice on how to use it, and if we don't have
it we can often give pointers on how to install it. Further, if a lot of
people request the same software, we may consider adding it to the
system image.

Every ORCD system runs Linux, so much of what you do on the cluster
involves the Linux command line. That doesn't mean you have to be a
Linux expert to use the system! However the more you can get comfortable
with the Linux command line and a handful of basic commands, the easier
using the system will be. If you are already familiar with Linux, feel
free to skip this section, or skim as a refresher.

Most Linux commands deal with directories and files. A
directory, synonymous to a folder, contains files and other
directories. The list of directories that lead to a particular directory
or file is called its path. In Linux, directories on a path are
separated by forward slashes /. It is also important to note that
everything in Linux is case sensitive, so a file myScript.sh is not
the same as the file myscript.sh. When you first log in you are in you
home directory. Your home directory is where you can put all the
code and data you need to run your job. Your home directory is not
accessible to other users, if you need a space to share files with other
users, let us know and we can make a shared group directory for you.

The path to your home directory on Satori is /home/<USERNAME>, where <USERNAME> is your username. The character ~ is also shorthand for your home directory in any Linux commands.

The path to your home directory on Satori is /home/<USERNAME>, where <USERNAME> is your username. The character ~ is also shorthand for your home directory in any Linux commands.

The path to your home directory on SuperCloud is /home/gridsan/<USERNAME>, where <USERNAME> is your username. The character ~ is also shorthand for your home directory in any Linux commands.

The path to your home directory on OpenMind is /home/<USERNAME>, where <USERNAME> is your username. The character ~ is also shorthand for your home directory in any Linux commands.

Anytime after you start typing a Linux command you can press the "Tab"
button your your keyboard. This called tab-complete, and will try to
autocomplete what you are typing. This is particularly helpful when
typing out long directory paths and file names. Pressing "Tab" once
will complete if there is a single completion, pressing it twice will
list all potential completions. It is a bit difficult to explain in
text, but you can try it out yourself and watch the short demonstration
here.

Finally, click on the box below for a list of Linux Commands. If you are new to Linux try them out for yourself at the command line.

One of the first tasks is to get your code, data, and any other files
you need into your home directory on the system. If your code is in
github you can use git commands on the system to clone your repository
to your home directory. You can also transfer your files to your home
directory from your computer by using the commands scp or rsync. Read
the page on Transferring Files for the system you are using to learn
how to use these commands and transfer what you need to your home
directory.

You can use scp or rsync from the command line on your local computer for any ORCD system. Both commands work similarly to the cp command, following the pattern <command> <source> <destination>, the only difference being that you will need to include the hostname of the system you are transferring to or from. For this reason you must run this command from the terminal on your computer before you've logged in.

To transfer a file from your computer to the ORCD system:

(You can use any of the login nodes listed above)

(You can use any of the login nodes listed above)

To transfer a file from an ORCD system to your computer:

(You can use any of the login nodes listed above)

(You can use any of the login nodes listed above)

Similar to cp, use the -r flag to copy over an entire directory and its contents. 

(You can use any of the login nodes listed above)

(You can use any of the login nodes listed above)

The rsync command can be used similarly and has some additional flags you can use. It also can be used to transfer only new or modified files to the destination, which makes it easy to keep a directory in "sync".

For more information on transferring files and additional methods please see the documentation page for your system:

Engaging Transferring Files Documentation Page Coming Soon

Satori Transferring Files Documentation Page

SuperCloud Transferring Files Documentation Page

OpenMind Transferring Files Documentation Page

At this point you may want to do a test-run of your code. You always
want to start small in your test runs, so you should choose a small
example that tests the functionality of what you would ultimately like
to run on the system. If your test code is serial and runs okay on a
moderate personal laptop or desktop you can request an interactive
session to run your code in by executing the command:

After you run this command you will be on a compute node and you can do
a test-run of your code. This command will allocate one core to your
job. If your test code is multithreaded or parallel, uses a lot of
memory, or requires a GPU you should request additional resources as needed. Not requesting the resources you will be using can negatively impact others on the system.

Please see your system's documentation pages for more information on requesting more resources for running interactive jobs, and how to run batch jobs.

Engaging's Documentation for Running Jobs

Satori's Documentation for Running Jobs

SuperCloud's Documentation for Running Jobs

OpenMind's Documentation for Running Jobs

