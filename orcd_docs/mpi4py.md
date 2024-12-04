MPI for Python (mpi4py) provides Python bindings for the Message Passing Interface (MPI) standard, allowing Python applications to exploit multiple processors on workstations, clusters and supercomputers.

You can learn about mpi4py here: https://mpi4py.readthedocs.io/en/stable/.

The support team has installed mpi4py in an Anaconda module. You can load the module and do not need to install anything,
 module load openmind/anaconda/3-2022.05


If you want to use Anaconda in your directory, refer to section 3 on this page to set it up, then install mpi4py, 
 conda install -c conda-forge mpi4py


First, load an Anaconda module on a CentOS 7 head node (such as eofe7 or eofe8),
 module load anaconda3/2023.07

 then install mpi4py, 
 conda create -n mpi
source activate mpi
conda install mpi4py


Prepare your Python codes. Example 1: The following is a code for sending and receiving a dictionary. Save it in a file named p2p-send-recv.py.
p2p-send-recv.pyfrom mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
    print(rank,data)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print(rank,data)


Example 2: The following is a code for sending and receiving an array. Save it in a file named p2p-array.py.
p2p-array.pyfrom mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# passing MPI datatypes explicitly
if rank == 0:
    data = numpy.arange(1000, dtype='i')
    comm.Send([data, MPI.INT], dest=1, tag=77)
    print(rank,data)
elif rank == 1:
    data = numpy.empty(1000, dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print(rank,data)

# automatic MPI datatype discovery
if rank == 0:
    data = numpy.arange(100, dtype=numpy.float64)
    comm.Send(data, dest=1, tag=13)
    print(rank,data)
elif rank == 1:
    data = numpy.empty(100, dtype=numpy.float64)
    comm.Recv(data, source=0, tag=13)
    print(rank,data)


Prepare a job script. The following is a job script for running mpi4py codes on 8 CPU cores of one node. Save it in a file named p2p-job.sh.
 p2p-job.sh#!/bin/bash -l
#SBATCH -N 1
#SBATCH -n 8

module load openmind/anaconda/3-2022.05

mpirun -np $SLURM_NTASKS python p2p-send-recv.py
mpirun -np $SLURM_NTASKS python p2p-array.py


Note

If you use Anaconda in your directory, do not load the Anaconda module. 

Finally submit the job,
 sbatch p2p-job.sh


Prepare a job script. The following is a job script for running mpi4py codes on 8 CPU cores of one node. Save it in a file named p2p-job.sh.
 p2p-job.sh#!/bin/bash -l
#SBATCH -N 1
#SBATCH -n 8

module load anaconda3/2023.07

source activate mpi
mpirun -np $SLURM_NTASKS python p2p-send-recv.py

source activate mpi
mpirun -np $SLURM_NTASKS python p2p-array.py


Finally submit the job,
 sbatch p2p-job.sh


