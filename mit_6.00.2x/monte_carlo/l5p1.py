#!/usr/bin/env python

import random
import sys

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    num_picks = 3
    total_count_of_3_of_same = 0
    for t in range(numTrials):
        #bucket = ['r','r','g','g']
        bucket = ['r','r','r','g','g','g']
        for n in range(num_picks):
            pick = random.choice(range(len(bucket)))
            ball = bucket.pop(pick)
            #print ball,
        #print
        #if bucket.count('g') == 3 or bucket.count('r') == 3:
        if bucket.count('g') == num_picks or bucket.count('r') == num_picks:
            total_count_of_3_of_same  += 1

    return total_count_of_3_of_same / float(numTrials)
            
print noReplacementSimulation(int(sys.argv[1]))
