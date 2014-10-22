#!/usr/bin/env python

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    s1_len = len(s1)
    s2_len = len(s2)

    s3 = ''
    for n in range(min(s1_len, s2_len)):
        s3 += s1[n] + s2[n]
        
    if s1_len > s2_len:
        s3 += s1[len(s2):]
    else:
        s3 += s2[len(s1):]

    print s3

laceStrings('abcd', 'efgh')
laceStrings('abcdijklm', 'efgh')
laceStrings('abcd', 'efghopqrs')
