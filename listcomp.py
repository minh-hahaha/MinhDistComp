#!/usr/bin/env python3
"""
This will demonstrate list comprehension
"""

# from mpi4py import MPI
# import numpy as np


# comm = MPI.COMM_WORLD
# size = comm.Get_size()
# rank = comm.Get_rank()
# name = MPI.Get_processor_name()

# root = 0

data = [1,2,3,4,5,6,7,8,9]

for element in data:
    print(5*element)

newlist = [a*5 for a in data if a%2 ==0]
print(newlist)
