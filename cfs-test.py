#!/usr/bin/env python3
"""
This is a simple test of reading from the shared cluster system
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

data = np.load("/clusterfs/nparraytest.npy")

print(name, ": I am rank" ,str(rank), "my data is : ", data)
#print(data)



