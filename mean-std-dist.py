#!/usr/bin/env python3
"""
This is my distributed version of mean-std
"""

from mpi4py import MPI
import numpy as np
import stattools as st


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

# each rank read the data

data = np.load("/clusterfs/ranked_data.npy")
# print (rank, " : ", data[rank,0])


# each rank gets a mean on its portion of the data
rank_mean = st.getMean(data[rank])
# print(rank, " : " , rank_mean)


# return means to the root (gather) and get population mean
recvbuff = comm.gather(rank_mean,root)

if rank == root:
    recvbuff = np.stack(recvbuff)
    global_mean = st.getMean(recvbuff) 
    print("global_mean", " : " ,global_mean) 
else:
    global_mean = None


# broadcast result to all ranks
mean = comm.bcast(global_mean,root)

# each rank gets a sums of squares on its portion of the data
rank_sos = st.sumsquares(data[rank],mean)
    
# return sums of squares to the root (reduce) and get the sum of the sums of squares 
res = MPI.COMM_WORLD.reduce(rank_sos,root = root)

if rank == root:
    #print("sum of sum of squares : " , res)
    std = st.stdev(res, (len(data) * len(data[0])))
    print("std : ", std)
# root can calculate the std



