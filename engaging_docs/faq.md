Engaging Cluster Documentation8. Frequently Asked Questions :: Engaging Cluster DocumentationEngaging Cluster Documentation1. Logging into the clusterLogging into Engaging Open OnDemandLogging into FastXLogging in via sshLogging in from a Linux or OSX hostLogging in from a Windows host2. Replacing or Adding an SSH KeySetup SSH Key Pair Authentication3. Slurm1. Cluster workflow2. Slurm Job Scheduler3. sbatch4. srun & salloc5. Slurm Job Arrays6. Determining Resources For Your Job4. Software1. Loading Software Modules2. Python Packages3. R Packages4. Compiling Software For Personal Use5. Compiling Miniconda For Personal Use6. Running Paraview in Client Server Mode via Slurm5. Storage1. The Home directory2. The Lustre File System3. NFS StorageFile Permissions6. Virtual Environments1. Jupyter Notebooks2. Python Packages3. Python Virtual Environments4. Anaconda Virtual Environments7. Best PracticesLustre Best Practices8. Frequently Asked QuestionsImprove this page> 8. Frequently Asked QuestionsPasswordsLogging Into The ClusterSoftware On The ClusterStorageCluster Workflow and Slurm8. Frequently Asked QuestionsThis is a compilation of the most frequently asked questions by users when using the engaging cluster.PasswordsHelp! I forgot my password to login to the cluster!Engaging uses MIT Kerberos authentication by default. Please seeIS&Tif you have forgotten your MIT Kerberos password.Logging Into The ClusterHow do I login to the cluster from my Linux/Mac computer?To login via the command line on a Linux or Mac computer, please follow the stepshere.How do I login to the cluster from my Windows computer?To login to the cluster on a Windows computer, you can use PuTTY or MobaXterm by following the instructionshere.How do I login to FastX?To login to the cluster using FastX, follow the instructions foundhere.How do I login to Engaging Open OnDemand?To login to Engaging Open OnDemand, follow the instructions foundhere.Software On The ClusterWhat software is available on the cluster?To see what software is available for use on the cluster, you can use the commandmodule availwhen logged into one of the login nodes. For more information on software available, please seehere.What operating systems do the compute nodes use on the cluster?The nodes on the Engaging cluster run CentOS 7, an older operating system that is no longer supported, with newer machines running Rocky 8.I�m trying to install a python package with the pip command but keep getting a permission denied error. How do I install a python package on the cluster?To install python packages on the cluster with pip, please follow the instructionshere.How do I install R Packages on the cluster?To install R packages on the cluster for personal use, please follow the instructionshere.Software that I need for my job isn�t listed when using themodule availcommand. How do I install the software I need?If you need software that is not available as a module, or if you need a specific version of software for your job, you will need to compile it yourself for use. To compile software for personal use, follow the instructions foundhere.StorageWhere can I store files on the cluster?Users have 3 locations they can store files in on the engaging cluster.Their home directory. More information on the home directory can be foundhere./nobackup1, this is a Lustre File System. For more information on /nobackup1, please seehere./pool001, this is an NFS File System. For more information on /pool001, please seehere.I want to share files with another user, how do I do that?You can edit your file permissions to allow other users to copy or edit your files. Please seeherefor information on how to edit file permissions.Cluster Workflow and SlurmHow is the cluster workflow structured?The slurm cluster workflow can be described in an infographic foundhere.What is Slurm?Slurm is a job scheduling software that the cluster uses to submit jobs to the compute nodes. Slurm�s purpose is to fairly and efficiently allocate resources amongst the compute nodes available on the cluster. It is imperative that you run your job on the compute nodes by submitting the job to the job scheduler with either sbatch or srun.How do I write an sbatch script?For instructions on how to write an sbatch script, please seehere.How do I run an interactive job with slurm?For instructions on how to use srun to run an interactive job, please seehere.How do I see which partitions I can submit to?You can see which partitions you have access to with the commandsinfoHow do I view detailed information about a partition, such as the number of nodes in the partition or the partition�s wall time?You can view detailed information about a partition with the commandscontrol show partition [PARTITION_NAME]How do I see all the nodes in a specific partition?You can see all the nodes that are part of a partition with the commandsinfo -p [partition_name]Some of the nodes in the partition are listed as �drained� or �down�. What does this mean?When a node is drained or down, it means this node requires servicing done by one of the engaging admins. If a node is drained, it means we have looked at it and are most likely waiting for hardware to arrive or have scheduled a servicing period for this node. If a node is down, slurm has determined something is wrong with this node and an admin hasn�t had the chance to look at it yet.How do I see information about my job once I submit it?Once you submit a job with an sbatch script, slurm will output your job�s JOB_ID. You can use this JOB_ID to see information about your job with the commandscontrol show jobid [JOB_ID]How many jobs can I have at once?You can run up to 500 jobs at once on the engaging cluster.How do I view the status of 1 of my jobs in the queue?You can view your job�s status with the commandsqueue -j [JOB_ID]How do I view the status of all of my jobs in the queue?You can view all of your job�s statuses in the queue with the commandsqueue -u [USERNAME]where USERNAME is your engaging username.My job has been pending for a long time, when can I expect it to start?You can view the estimated time your job will start, along with any reasons why it is waiting in the queue with the commandsqueue -u [USERNAME] --startMy job has been pending and says the reason is �Resources�. What does this mean?If your job is pending for resources, it means that it is waiting for the resources your job has requested to free up in order for your job to run.My job has been pending and it says the reason is �Priority�. What does this mean?If your job is pending for priority, it means that jobs with a higher priority score are waiting for compute nodes to free up so that they can run. Once these jobs with a higher priority run, yours will move up in line and be run when the resources you requested are available.My job has been pending and it says the reason is �ReqNodeNotAvail�. What does this mean?If your job is pending for Requested Nodes Not Available, this means the compute nodes requested by the job are not available. This might be due to things such as cluster maintenance, nodes being down/offline or the config you requested just doesn�t exist. If you request more nodes than are in a partition, or if you request more CPUs than there are per node, your job will not be able to run since there is insuffienet resources.How do I get information on a job once it has completed?Once a job has finished, you can view information about it with the commandsacct -j <jobid> --format=JobID,JobName,Elapsed,StateHow do I cancel a job?You can cancel a job with the commandscancel JOB_IDHow do I view information about a specific node, such as how many CPUs it has?You can view detailed information about a node with the commandscontrol show node node[NODE_NUMBER]. You can also pass a list of nodes to this command, such as node[001-010].Lustre Best Practices1. Logging into the cluster