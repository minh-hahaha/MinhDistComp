#!/usr/bin/env python3
"""
This is my distributed version of mean-std
"""

from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

# each rank read the data
sendbuff = []

data = np.load("/clusterfs/unranked_data.npy")

data = comm.scatter(sendbuff,root)




# each rank gets a mean on its portion of the data

# return means to the root and get population mean

# broadcast result to all ranks

# each rank gets a sums of squares on its portion of the data

# return sums of squares to the root and get the sum of the sums of squares 

# root can calculate the std



