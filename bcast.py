#!/usr/bin/env python3
"""
This is an example of how to use broadcast
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

if rank==root:
    data = {'a':1,'b':2,'c':3}
else:
    data = None 

data = comm.bcast(data,root)

print(name, ": I am rank" ,str(rank), "my data is : ", data)
