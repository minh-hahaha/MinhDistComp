#!/usr/bin/env python3
"""
This script will use Monte Carlo method to estimate Pi
"""
import random
import numpy as np

pairs = 10**5 
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
    
pi = 4 * count/(pairs)

print (pi)
print("percent error : ", (np.pi - pi)/np.pi , "%")




# how many pairs

# generate pairs of random x , y range [0,1)

# find distance of pair from the origin (0,0)

# if it is <= 1, count 

# find Pi by dividing the count by total number of pairs and multiply by 4
