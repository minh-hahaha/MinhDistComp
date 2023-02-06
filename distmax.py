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
# nElements = scale * threads

data = []
sendbuff = []
recvbuff = []

if rank == root:
    nElements = scale * threads
    for i in range(nElements):
        data.append(random.random())
    sendbuff = np.array(data, dtype = float)
    sendbuff = sendbuff.reshape((threads, scale))
#    print(sendbuff)

# look for the max in the list
# max = data[0]
# for num in data:
#     if (num > max):
#         max = num


#print(data)

#print("\nMax is: ", max)


# this is the empty sending buffer of data

# this will only run on the root process (0)
# if rank == root:
#     m = np.random.randn(size, 4)
#     print(m)
#     sendbuff = m
#     # print(sendbuff)


# this will run on every rank

data = comm.scatter(sendbuff,root)

print(name, ": I am rank" ,str(rank), "my data is : ", data)

# finding max on the rank
max_num = []
rank_max = data[0]
for num in data:
    if (num > rank_max):
        rank_max = num
        max_num.append(rank_max)
# print(name, ": I am rank" ,str(rank), "my max is : ", rank_max)
print(max_num) 

# finding max of the everything
# max = max_num[0]
# for num in max_num:
#     if (num > max):
#         max = num
# print(max)


# gathering data to receive buffer
recvbuff = comm.gather(data,root)
if rank == root:
    recvbuff = np.stack(recvbuff)
    print("I am root and I have this data: ", recvbuff)
    






