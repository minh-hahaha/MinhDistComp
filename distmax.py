#!/usr/bin/env python3
"""
This will go through a list and find the maximum value
"""

from mpi4py import MPI
import numpy as np
import random


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

# build our list
scale = 2
threads = 24
nElements = scale * threads

data = []

if rank == root:
    for i in range(nElements):
        data.append(random.random())

sendbuff = np.array(data)

# look for the max in the list
# max = data[0]
# for num in data:
#     if (num > max):
#         max = num


#print(data)

#print("\nMax is: ", max)


# this is the empty sending buffer of data
recvbuff = []

# this will only run on the root process (0)
# if rank == root:
#     m = np.random.randn(size, 4)
#     print(m)
#     sendbuff = m
#     # print(sendbuff)


# this will run on every rank
recvbuff = comm.scatter(sendbuff.reshape((threads,scale)),root)

print(name, ": I am rank" ,str(rank), "my data is : ", recvbuff)


