#!/usr/bin/env python3
"""
This script will get the mean and standard deviation for a numpy array read from file
"""

# from mpi4py import MPI
import numpy as np
from math import sqrt
from stattools import *


# comm = MPI.COMM_WORLD
# size = comm.Get_size()
# rank = comm.Get_rank()
# name = MPI.Get_processor_name()

# root = 0


data = np.load("/clusterfs/unranked_data.npy")

# get results and print....
nElements = len(data)
mean = getMean(data)
sos = sumsquares(data,mean)
std = stdev(sos,nElements)


print("nElements:\t", nElements)
print("Mean:\t", mean)
print("Standard Deviation:\t", std)


#print(getMean(data))
#print(sumsquares(data,getMean(data)))
#print(stdev(sumsquares(data,getMean(data)),len(data)))

# read in data, know what data is there and generate a 
