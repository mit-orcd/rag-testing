Engaging Cluster Documentation1. Loading Software Modules :: Engaging Cluster DocumentationEngaging Cluster Documentation1. Logging into the clusterLogging into Engaging Open OnDemandLogging into FastXLogging in via sshLogging in from a Linux or OSX hostLogging in from a Windows host2. Replacing or Adding an SSH KeySetup SSH Key Pair Authentication3. Slurm1. Cluster workflow2. Slurm Job Scheduler3. sbatch4. srun & salloc5. Slurm Job Arrays6. Determining Resources For Your Job4. Software1. Loading Software Modules2. Python Packages3. R Packages4. Compiling Software For Personal Use5. Compiling Miniconda For Personal Use6. Running Paraview in Client Server Mode via Slurm5. Storage1. The Home directory2. The Lustre File System3. NFS StorageFile Permissions6. Virtual Environments1. Jupyter Notebooks2. Python Packages3. Python Virtual Environments4. Anaconda Virtual Environments7. Best PracticesLustre Best Practices8. Frequently Asked QuestionsImprove this page>4. Software> 1. Loading Software Modules1. Loading Software ModulesSoftware Modules on the Engaging ClusterThere is a wide selection of software installed on the Engaging cluster that are available to be used. Software installed across the cluster are available asenvironmental modules.These modules enable the cluster to have multiple versions of the same software available. You can see all of the available environmental modules with:module availUsing Environment Module CommandsThe command to list available environment modules is shown above, and after you have found the module you would like to use you can load it with either:module add <name>module load <name>Both will perform the same action of loading a module. You can check the modules you currently have loaded with:module listThere are two options to remove modules:module purgemodule rm <name>Usingmodule purgewill �purge� all loaded modules (so that none are loaded). Using the module remove command will remove just one specified module.Loading Specific Module VersionMuch software has different versions, with modules existing for several different of these different versions for many packages. Some software have a default module, such asgcc. Usingmodule load gccwill load this default module, which happens to be �gcc/6.2.0�. To use a specific version of a software first check for what modules may be available usingmodule avail <name>. Once you find a version you want to use, such as �gcc/11.2.0�, pass the module name into the load command as follows:module load gcc/11.2.0Afterwards you can run amodule listto verify that the desired module is now loaded.Request Software To Be AddedIf you need software that is not listed with themodule availcommand, please reach out toorcd-help-engaging@mit.eduto inquire about getting software compiled as a module for your use. Please note that we may not compile software that is used by only one user, but we will assist you to compile it for your own personal use. Software to be compiled as a module must be utilized by more than one user in order for us to take the time to create an environmental module for it. For more information on compiling software for individual use, please seehere.4. Software2. Python Packages