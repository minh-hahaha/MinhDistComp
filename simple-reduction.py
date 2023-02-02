#!/usr/bin/env python3
"""

"""

#from mpi4py import MPI
#import numpy as np

from functools import reduce

#comm = MPI.COMM_WORLD
#size = comm.Get_size()
#rank = comm.Get_rank()
#name = MPI.Get_processor_name()

#root = 0

data = [1,2,3,4,5]  

def my_add(a,b):
    result = a+b
    print(f"{a} + {b} = {result}")
    return result

def my_mult(a,b):
    result = a*b
    print(f"{a} * {b} = {result}")
    return result


x = my_add(5,5)
print(x)

print("\n\n")

x= reduce(my_mult,data) 
print(x)



