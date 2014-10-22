#!/usr/bin/env python 

def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    i,j,k=0,0,0
    for i in range((n / 6) + 1):
        if 6 * i + 9 * j + 20 * k == n:
            return (i,j,k)
        for j in range((n / 9) +1):
            if 6 * i + 9 * j + 20 * k == n:
                return (i,j,k)
            for k in range((n / 20) + 1):
                if 6 * i + 9 * j + 20 * k == n:
                    return (i,j,k)
    return False

if McNuggets(15):
  print("%i %i %i" % McNuggets(15))

if McNuggets(66):
  print("%i %i %i" % McNuggets(66))
