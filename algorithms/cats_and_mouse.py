#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    d1=abs(x-z)
    d2=abs(y-z)
    if d1==d2:
        print('Mouse C')
    if d1>d2:
        print('Cat B')
    if d2>d1:
        print('Cat A')