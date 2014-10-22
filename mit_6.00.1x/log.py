#!/usr/bin/env python

def myLog(x, b):

    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    ctr = 1
    while True:
        prev_ctr =  ctr - 1
        if b ** ctr <= x:
            ctr += 1
        else:
            break

    return prev_ctr


print myLog(16, 2)
print myLog(15, 3)
print myLog(27, 3)

