Engaging Cluster DocumentationLogging in from a Linux or OSX host :: Engaging Cluster DocumentationEngaging Cluster Documentation1. Logging into the clusterLogging into Engaging Open OnDemandLogging into FastXLogging in via sshLogging in from a Linux or OSX hostLogging in from a Windows host2. Replacing or Adding an SSH KeySetup SSH Key Pair Authentication3. Slurm1. Cluster workflow2. Slurm Job Scheduler3. sbatch4. srun & salloc5. Slurm Job Arrays6. Determining Resources For Your Job4. Software1. Loading Software Modules2. Python Packages3. R Packages4. Compiling Software For Personal Use5. Compiling Miniconda For Personal Use6. Running Paraview in Client Server Mode via Slurm5. Storage1. The Home directory2. The Lustre File System3. NFS StorageFile Permissions6. Virtual Environments1. Jupyter Notebooks2. Python Packages3. Python Virtual Environments4. Anaconda Virtual Environments7. Best PracticesLustre Best Practices8. Frequently Asked QuestionsImprove this page>1. Logging into the cluster>Logging in via ssh> Logging in from a Linux or OSX hostLogging in from a Linux or OSX hostHow to login to the engaging cluster from a Linux or OSX host:All Logins are done via MIT Kerberos account credentials.Users are free to manage and use ssh keys at their own discretion but this is not supported directly by the Engaging admins.You will need to point your chosen SSH client to one of the following login nodes.eofe7.mit.edu (CentOS 7)eofe8.mit.edu (CentOS 7)eofe9.mit.edu (CentOS 7)eofe10.mit.edu (Rocky 8)To login via the command line from a Linux or OSX host, simply run the ssh commandssh [username]@[host], replacing �[username]� with your MIT Kerberos username and �[host]� with the desired login node name i.e.ssh your_name@eofe9.mit.edu.Connecting to either eofe9 or eofe10 requires Two-Factor Authentication.If you have any problems logging in, please contactorcd-help-engaging@mit.edu.Logging in via sshLogging in from a Windows host