#!/usr/bin/env python3
"""
This is an example of reduction and my own functions to do the reduction
"""

from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

data = np.array([1,2,3])

def mysum(x,y):
    return [a+b for a,b in zip(x,y)]

def mycoolfunc(x,y):
    return [a*b for a,b in zip(x,y)]

def myminfunc(x,y):
    return[min(a,b) for a,b in zip(x,y)]

# on each rank
print(name, ": I am rank" ,str(rank), "my data is : ", data)

# res = MPI.COMM_WORLD.reduce(data, root=root)
# res = MPI.COMM_WORLD.reduce(data, op=mysum, root=root)
# res = MPI.COMM_WORLD.reduce(data, op=mycoolfunc, root=root)
res = MPI.COMM_WORLD.reduce(data, op=myminfunc, root=root)


# ONLY run on the root
if rank == root:
    print("\n\n")
    print(name, ": I am rank" ,str(rank), "my data is : ", res)


