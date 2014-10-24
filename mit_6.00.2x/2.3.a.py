#!/usr/bin/env python

"""
Write a deterministic program, deterministicNumber, that
returns an even number between 9 and 21.
"""

import random

def deterministicNumber():
  while 1:
    r = random.choice(range(10,21,2))
    return r


print deterministicNumber()
