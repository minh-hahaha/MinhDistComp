#!/usr/bin/env python3
"""
This will go through a list and find the maximum value
"""

from mpi4py import MPI
import numpy as np
import random

# build our list
scale = 10**6
threads = 24
nElements = scale * threads

data = []
for i in range(nElements):
    data.append(random.random())

# look for the max in the list
max = data[0]
for num in data:
    if (num > max):
        max = num


#print(data)

print("\nMax is: ", max)
#comm = MPI.COMM_WORLD
#size = comm.Get_size()
#rank = comm.Get_rank()
#name = MPI.Get_processor_name()

#root = 0

