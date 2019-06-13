#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    d=str(n)
    counter=0
    for i in d:
        if int(i)>0:
            if n % int(i) ==0:
                counter=counter+1
    print(counter)            