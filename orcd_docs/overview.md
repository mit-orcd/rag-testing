Each ORCD system has its own software stack. Many basic and commonly used software and libraries are already installed, so it is good to check before spending the time to install it yourself. This page discusses the general overview of what kinds of software are supported and points you to how to use them and what to do if what you need isn't there.

While the software stack will be different on each system, there are three general classes of software:

Each individual ORCD system may not label or organize their software in this way. However, this is the support model that will be used going forward. Engaging, in particular, will organize its software in this way.

Here are some general notes by system on this for Engaging and SuperCloud. Click on the tab for the system you are interested in:

Engaging nodes are one of two operating systems: Centos 7 and Rocky 8. Each operating system has its own software stack.

Centos 7 has been around for longer, so it has more software installed. These nodes have a very large list of modules, older ones that no longer work have not necessarily been removed but can be considered deprecated. Centos 7 nodes will either be retired or migrated to Rocky 8 in the near future, so when given the choice use Rocky 8 nodes.

Rocky 8 nodes have a significantly shorter list of modules and are organized into core, community, and deprecated. Core software will be displayed by default, community and deprecated software will require a "module use" command to display. See the page on modules for more information.

The SuperCloud software stack is managed by the Lincoln Laboratory Supercomputing Center. The modules listed are considered "core" software. Deprecated software that was part of the core stack is removed from the system. "Community" software is provided in the llgrid_beta directory in the groups location. Anyone can use them but they are not officially supported.

One of the first steps for getting a workflow running on a new system is to set up any software or packages needed to run it. Here are a few steps to do that on an ORCD system.

As mentioned above, there is a lot of software already installed. Using the software we've installed saves you time. This software may also perform better or be better configured to use the system. For example, it may be installed in a faster part of the filesystem or configured to use special hardware available on the cluster.

For software check the module avail command (see the page on modules for more information). Some software is available without a module, you can check if a particular command is available using the which command at the command line. For example, run which git to see if the git command is available. If it is, the path to the git command will print to the screen.

Common languages like Python, Julia, and R are provided through modules as well. Packages for these are sometimes provided along with the installation. A quick way to check if a package is available is to try to import it.

If we don't have the software you need, you can often install it yourself. You will need to install them in your home directory or another directory you have access to. You will not be able to install software in any of the system-wide directories, as changes to these affect everyone using the system (for example you will not be able to install in any location that requires sudo).

The sudo command is used to make system-wide administrator-level changes. On a system where you are the only user this is usually fine, the only person you can affect is yourself. On large shared systems with many users any command that uses sudo has the potential to affect the workflow of other researchers and potentially cause harm, even when it is not intentional. For this reason only trained system administrators have the ability to use sudo.

You should not need sudo to install packages in your own space. For software installs, the sudo is only used to put the installation files in the system-wide directory, so it is not needed to install in your own directories. The Installing Software page covers how to specify installation directories for some of the more common build systems. 

Sometimes you can find pre-built binaries for the software you want. These are the easiest to install. Often you will need to build the software you need. See the page on Installing Software for more information. You may also check the Recipes section of these pages to see if there is an existing recipe for installing the software you are interested in.

For Python, Julia, and R packages, each of these have their own package managers for installing packages. See the respective documentation pages linked above for each of these.

Note

Satori is unique in that its nodes have a different architecture than those in other ORCD systems. They are IBM machines with the ppc64le architecture. There is some software that does not support this architecture. When selecting pre-built software, be sure to select the one for ppc64le.

If you are having trouble installing software you can reach out to orcd-help@mit.edu or one of the other lists on Getting Help for help. You can also stop by office hours if you prefer. Depending on the software and the system you are using, we may help walk you through installing it for yourself or install it in a community location.

