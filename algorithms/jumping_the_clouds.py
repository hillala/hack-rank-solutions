#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
count=0
jumps=0
while count<n-1:
    if count+2<=n-1:
        if c[count+2]==0:
            jumps=jumps+1
            count=count+2
        else:
            jumps=jumps+1
            count=count+1
    else:
        count=count+1
        jumps=jumps+1
                
            
print(jumps)