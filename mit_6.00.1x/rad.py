#!/usr/bin/env python

import math
import sys

def radiationExposure(start, stop, step):
  total = 0.0
  ctr = start
  #for i in range(start, stop, step):
  while ctr < stop:
     print("At %i, total = %0.2f" % (ctr, total))
     total = total + ( f(ctr) * step )
     ctr += step

  print total

def f(t):
  #return t - 1 + math.log(t)
  return 10 * math.e ** (math.log(0.5)/5.27 * t)

print(tuple(map(int, sys.argv[1:4])))
radiationExposure(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
