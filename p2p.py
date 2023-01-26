#!/usr/bin/env python3
"""
Trying to show how point to point communication works
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

# let's create an array on each rank/process 
outgoing_data = np.array([rank]*100, dtype=float)

if rank == root:
    comm.send(outgoing_data,dest =(rank+1)%size)

if rank > root:
    comm.send(outgoing_data,dest =(rank+1)%size)
    data = comm.recv(source=(rank-1) % size) 

if rank == root:
    data = comm.recv(source=size-1)

print("I am rank" ,str(rank))
print("my data is :")
print(data)

