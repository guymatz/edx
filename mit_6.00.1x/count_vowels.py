#!/usr/bin/env python

s = 'azcbobobegghakl'
ctr = 0
longest = ''
previous = 'a'
current_longest = ''
for c in s:
    if c >= previous: 
        current_longest += c
    else:
        current_longest = c

    if len(current_longest) > len(longest):
        longest = current_longest
    
    previous = c

print longest
