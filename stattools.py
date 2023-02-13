from math import sqrt

def getMean(lst) -> float:
    """getMean will get the mean of a list"""
    sum = 0
    for x in lst:
        sum += x
    return sum/len(lst)

def sumsquares(lst,mu) -> float:
    """sumsquares will take a list and mu (the mean) and get the syms of the distance between the two values"""
    ss = 0
    for x in lst:
        ss += (x-mu)**2
    return ss

def stdev(sumofsquares,n) -> float:
    """This function will take a sums of squares and an N and return the standard deviation"""
    return sqrt(sumofsquares/n)

