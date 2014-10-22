#!/usr/bin/env python

import math

def genPrimes():
  n = 2
  yield n
  n = 3
  yield n
  while True:
    n += 2
    if is_prime(n):
      yield n

def is_prime(n):
  if n % 2 == 0:
    return False
  for i in range(3, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

g = genPrimes()

for n in range(15):
  print g.next()
