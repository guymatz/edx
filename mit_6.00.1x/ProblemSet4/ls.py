#!/usr/bin/env python
def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

print linearSearch([1,2,3,4,5,6],1)
print linearSearch([1,2,3,4,5,6],2)
