Engaging Cluster Documentation2. Python Packages :: Engaging Cluster DocumentationEngaging Cluster Documentation1. Logging into the clusterLogging into Engaging Open OnDemandLogging into FastXLogging in via sshLogging in from a Linux or OSX hostLogging in from a Windows host2. Replacing or Adding an SSH KeySetup SSH Key Pair Authentication3. Slurm1. Cluster workflow2. Slurm Job Scheduler3. sbatch4. srun & salloc5. Slurm Job Arrays6. Determining Resources For Your Job4. Software1. Loading Software Modules2. Python Packages3. R Packages4. Compiling Software For Personal Use5. Compiling Miniconda For Personal Use6. Running Paraview in Client Server Mode via Slurm5. Storage1. The Home directory2. The Lustre File System3. NFS StorageFile Permissions6. Virtual Environments1. Jupyter Notebooks2. Python Packages3. Python Virtual Environments4. Anaconda Virtual Environments7. Best PracticesLustre Best Practices8. Frequently Asked QuestionsImprove this page>4. Software> 2. Python Packages2. Python PackagesInstalling Python Packages Locally with PipPython packages, such as Numpy, pandas, or matplotlib, must be installed on a user by user basis. This process assumes that you have loaded a Python module with the commandmodule load python/[version]. As python is included in anaconda, using an anaconda module will work too.You can install python packages with the command:pip install --user [package_name]Please note that you MUST use the �user flag, otherwise you will get a permissions error since it will try to install the python package across the cluster instead of for just your user account.If you have any questions or problems installing python packages, please emailorcd-help-engaging@mit.edu1. Loading Software Modules3. R Packages