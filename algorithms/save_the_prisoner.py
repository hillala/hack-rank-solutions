#!/bin/python

import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    t2=m%n
    val=t2+s-1
    if val<n+1:
        if val==0:
            return n
        else:
            return val
    else:
        return val-n
t = int(raw_input().strip())
for a0 in xrange(t):
    n, m, s = raw_input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

