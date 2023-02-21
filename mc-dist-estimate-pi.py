#!/usr/bin/env python3
"""
This script will use Monte Carlo method to estimate Pi
"""
import random
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

pairs = 10**7 
x = []
y = []
count = 0

for i in range(0,pairs):
    x.append(random.random())
    y.append(random.random())

# print(x)
# print(y)

for i in range(0,pairs):
    if( (x[i]**2 + y[i]**2)**(1/2) <= 1 ):
        count = count + 1
    
# pi = 4* count/(pairs)

pi = comm.reduce(count,root = root)

if rank == root:
    estpi = (pi/pairs) * 4
    print(estpi)
    print("percent error : ", (np.pi - pi)/np.pi , "%")
    
print (estpi)



# how many pairs

# generate pairs of random x , y range [0,1)

# find distance of pair from the origin (0,0)

# if it is <= 1, count 

# find Pi by dividing the count by total number of pairs and multiply by 4
