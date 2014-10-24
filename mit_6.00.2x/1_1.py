#!/usr/bin/env python

import sys
import re
import pylab

def highs_lows(infile):
    highs = []
    lows = []
    
    temp_regex = re.compile(r'\d+\s+\d+\s+\d+')
    with open(infile) as file:
        for line in file:
            if not temp_regex.match(line):
                pass
            else:
                day, high, low = line.strip().split()
                #print day, high, low; raw_input()
                highs.append(int(high))
                lows.append(int(low))
    
    return (highs, lows)

def diffTemps(list_a, list_b):
    diff_list = []
    for n in range(len(list_a)):
        diff_list.append(list_a[n] - list_b[n])
    return diff_list

def avgTemps(list_a, list_b):
    avg_list = []
    for n in range(len(list_a)):
        avg_list.append((list_a[n] + list_b[n]) / 2 )
    return avg_list

def producePlot(highs, lows):
    pylab.figure(1)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.plot(range(0, len(highs)), diffTemps(highs, lows))
    pylab.plot(range(0, len(highs)), avgTemps(highs, lows), 'go')
    pylab.show()

    
if __name__ == '__main__':
    temps = highs_lows(sys.argv[1])
    producePlot(temps[0], temps[1])
