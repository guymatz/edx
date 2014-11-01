#!/usr/bin/env python

"""
Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty.
"""

def mean(l):
    total_len = 0
    for s in l:
        total_len += len(s)
    mean =  total_len/float(len(l))
    return mean

def stdDevOfLengths(L):

    if len(L) == 0:
        return float('NaN')
    else:
        total_len = 0
        for s in L:
            total_len += len(s)
        mu =  total_len/float(len(L))
        
        sigma_total = 0
        for l in L:
            sigma_total += (len(l) - mu)**2
    
        return (sigma_total/len(L))**.5

l= []
print stdDevOfLengths(l)
l= ['a','r','p']
print stdDevOfLengths(l)
l= ['hello','you','thing']
print stdDevOfLengths(l)
l = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(l)
