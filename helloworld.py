#!/usr/bin/env python3

"""
# This is our hello world example
"""

from mpi4py import MPI

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()

name = MPI.Get_processor_name()

print("Hello, World! I am process %2d of %2d on %s" % (rank,size,name))


