NVHPC is an integrated collection of software tools and libraries distributed by NVidia. An overview document describing nvhpc 
can be found here.
The aim of the NVHPC team is to provide up to date, preconfigured suites of compilers, libraries and tools that are 
specifically optimized for NVidia GPU hardware. It supports single and multi-GPU execution.

This example shows steps for using NVHPC to run a simple test MPI program, written in C, that communicates between two GPUs.
The detailed steps, that can be executed in an interactive Slurm session, are explained 
below.  A complete Slurm job example is shown at the end.

Prerequisites

This example assumes you have access to a Slurm partition with GPU resources and if using Engaging are working with a Rocky Linux environment.

The NVHPC environment is installed as a module and can be made visible in a session using the command

this will add a specific version of the nvhpc software (version 23.3 released in 2023 for Engaging and version 21.5 released in 2021 for Satori) to a shell or batch script. The
software added includes compilers for C, C++ and Fortran; base GPU optimized numerical libraries for linear algebra, Fourier
transforms and others; GPU optimized communication libraries supporting MPI, SHMEM and NCCL APIs.

An environment variable, NVHPC_ROOT, is also set. This can be used in scripts to reference the locations of libraries
when needed.

Here we use the module environment variable, NVHPC_ROOT, to set environment variables
that have paths needed for compilation and linking of code.

The next step is to create a file holding C code that uses MPI to send information between two GPUs 
running in different processes. Paste the C code below into a file called test.c.

Here we use nvhpc MPI wrapper to compile. The two environment variables we set earlier (cuincdir and culibdir) are used to
let the compile step know where to find the relevant CUDA header and library files. The CUDA runtime library (cudart) is added
as a location for finding CUDA functions the code utilizes.

Once code has been compiled the mpiexec command that is part of the nvhpc module can be used to run the test program.
The nvhpc module defaults to using its builtin version of OpneMPI. The OpenMPI option btl_openib_warn_no_device_params_found
is passed into the OpenMPI runtime library. This option suppresses a warning that OpenMPI can generate when it encounters
a network device card that is not present in a built-in list that OpenMPI has historically included.

Note the salloc command is only needed to run interactively from the login node. If you are running in a batch job or are already in an interactive job on a compute node you will not need to first run salloc.

Running this program using the command above should produce the following output.

First create a file called "test.c" containing the example C program above. The job script file below will run all the steps described above for "test.c". It can be submitted to Slurm using the command sbatch followed by the filename holding the job script.

