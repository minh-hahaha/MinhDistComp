#!/usr/bin/env python3
"""
This is an example of a reduction
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

data = np.array([rank*1,rank*2,rank*3,rank*4])
    
print(data) 

recvbuff = comm.reduce(data, root = 0, op=MPI.SUM)

if rank == root:
    print(recvbuff)
