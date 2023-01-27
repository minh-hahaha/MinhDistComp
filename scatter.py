#!/usr/bin/env python3
"""
This is going to demonstrate how scatter works...
"""

from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

# this is the empty sending buffer of data
sendbuff = []

# this will only run on the root process (0)
if rank == root:
    m = np.random.randn(size, 4)
    print(m)
    sendbuff = m
    # print(sendbuff)

# this will run on every rank
data = comm.scatter(sendbuff,root)

print(name, ": I am rank" ,str(rank), "my data is : ", data)
